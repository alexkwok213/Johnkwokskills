#!/usr/bin/env python3
"""Render an HTML composition implementing window.TL.dur and window.render(t)."""
import argparse
import io
import math
from pathlib import Path
import subprocess
import sys
import tempfile


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['preview', 'full'])
    parser.add_argument('times', nargs='*', type=float, help='preview timestamps in seconds')
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--width', type=int, default=1080)
    parser.add_argument('--height', type=int, default=1920)
    parser.add_argument('--browser', help='optional Chrome/Chromium executable path')
    parser.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    if not args.html.is_file():
        parser.error('--html must be an existing HTML file')
    if not 1 <= args.fps <= 120 or min(args.width, args.height) < 2:
        parser.error('fps must be 1–120 and dimensions must be at least 2')
    if args.width % 2 or args.height % 2:
        parser.error('dimensions must be even for yuv420p')
    if args.mode == 'full' and args.times:
        parser.error('timestamps are only valid in preview mode')
    return args


# render(t) may return a Promise. Then wait for media seeks and a browser paint.
SETTLE = """async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(async img => {
        if (!img.complete) await new Promise((resolve, reject) => {
            img.addEventListener('load', resolve, {once:true});
            img.addEventListener('error', () => reject(Error('Image failed: '+img.src)), {once:true});
        });
        if (!img.naturalWidth) throw Error('Image failed: '+img.src);
        await img.decode();
    }));
    await new Promise((resolve, reject) => {
        const start = performance.now();
        function poll() {
            const media = [...document.querySelectorAll('video,audio')].filter(m => m.currentSrc || m.src);
            if (media.some(m => m.error)) return reject(Error('Media failed to load'));
            if (media.every(m => !m.seeking && m.readyState >= 2)) return resolve();
            if (performance.now()-start > 15000) return reject(Error('Media load/seek timed out'));
            setTimeout(poll, 10);
        }
        poll();
    });
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
}"""


def shot(page, t):
    page.evaluate('async t => { await window.render(t); }', t)
    page.evaluate(SETTLE)
    return page.screenshot(type='jpeg', quality=93, animations='disabled')


def encode(page, args, duration):
    output = args.output_dir / 'video_noaudio.mp4'
    temporary = args.output_dir / '.video_noaudio.rendering.mp4'
    frames = math.ceil(duration * args.fps)
    command = [args.ffmpeg, '-y', '-v', 'error', '-f', 'image2pipe', '-framerate', str(args.fps),
               '-c:v', 'mjpeg', '-i', '-', '-an', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
               '-crf', '17', '-preset', 'medium', str(temporary)]
    try:
        with tempfile.TemporaryFile() as errors:
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=errors)
            try:
                for i in range(frames):
                    process.stdin.write(shot(page, i / args.fps))
                process.stdin.close()
                status = process.wait()
            except BaseException:
                process.kill()
                process.wait()
                process.stdin.close()
                errors.seek(0)
                detail = errors.read().decode(errors='replace').strip()
                if detail:
                    print(detail, file=sys.stderr)
                raise
            if status:
                errors.seek(0)
                raise RuntimeError(f'ffmpeg exited {status}: {errors.read().decode(errors="replace").strip()}')
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'done {output} ({frames} frames, {frames / args.fps:.3f}s, no audio)')


def main():
    args = arguments()
    from playwright.sync_api import sync_playwright
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        options = {'args': ['--allow-file-access-from-files']}
        if args.browser:
            options['executable_path'] = args.browser
        browser = p.chromium.launch(**options)
        try:
            page = browser.new_page(viewport={'width': args.width, 'height': args.height}, device_scale_factor=1)
            page.goto(args.html.resolve().as_uri(), wait_until='networkidle')
            duration = page.evaluate('() => { if (typeof window.render !== "function") throw Error("Missing window.render(t)"); return window.TL?.dur; }')
            if not isinstance(duration, (int, float)) or isinstance(duration, bool) or not math.isfinite(duration) or duration <= 0:
                raise ValueError('window.TL.dur must be a positive finite duration in seconds')
            if args.mode == 'preview':
                from PIL import Image
                times = args.times or [0, duration / 2, max(0, duration - 1 / args.fps)]
                if any(not math.isfinite(t) or not 0 <= t < duration for t in times):
                    raise ValueError('preview timestamps must satisfy 0 <= t < TL.dur')
                width = min(360, args.width)
                height = round(width * args.height / args.width)
                sheet = Image.new('RGB', (width * len(times), height))
                for i, t in enumerate(times):
                    with Image.open(io.BytesIO(shot(page, t))) as frame:
                        sheet.paste(frame.convert('RGB').resize((width, height)), (i * width, 0))
                output = args.output_dir / 'preview.jpg'
                sheet.save(output, quality=88)
                print(output)
            else:
                encode(page, args, duration)
        finally:
            browser.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Render failed: {error}', file=sys.stderr)
        sys.exit(1)
