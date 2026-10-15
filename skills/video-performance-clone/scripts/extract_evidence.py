#!/usr/bin/env python3
"""Extract visual/audio evidence with source timestamps; infer no performance."""
import argparse
import array
import hashlib
import json
import math
import re
import subprocess
import sys
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True)


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def times(log):
    return [float(t) for t in re.findall(r"\bn:\s*\d+.*?pts_time:([\d.eE+\-]+)", log)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--fps", type=float, default=2)
    parser.add_argument("--start", type=float, default=0)
    parser.add_argument("--end", type=float)
    args = parser.parse_args()
    source = args.video.resolve()
    metadata = json.loads(run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(source)
    ]).stdout)
    video = next(s for s in metadata["streams"] if s["codec_type"] == "video")
    duration = float(video.get("duration", metadata["format"]["duration"]))
    end = duration if args.end is None else args.end
    if not (args.fps > 0 and 0 <= args.start < end <= duration):
        parser.error("Need fps > 0 and 0 <= start < end <= video duration")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        parser.error("Output must be empty; use a new directory for event detail")
    digest = hashlib.sha256()
    with source.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    save(out / "metadata.json", metadata)
    selection = (
        f"gte(t,{args.start})*lt(t,{end})*"
        f"(isnan(prev_selected_t)+gt(floor((t-{args.start})*{args.fps}+0.000001),"
        f"floor((prev_selected_t-{args.start})*{args.fps}+0.000001)))"
    )
    log = run([
        "ffmpeg", "-hide_banner", "-i", str(source), "-map", f"0:{video['index']}",
        "-vf", f"select='{selection}',showinfo,scale=640:-2",
        "-fps_mode", "vfr", "-an", str(out / "frame-%06d.jpg")
    ]).stderr
    timestamps = times(log)
    frames = sorted(out.glob("frame-*.jpg"))
    if not frames or len(timestamps) != len(frames):
        raise RuntimeError("Frame count and showinfo timestamp count disagree")
    cut_log = run([
        "ffmpeg", "-hide_banner", "-i", str(source), "-map", f"0:{video['index']}",
        "-vf", f"select='gte(t,{args.start})*lt(t,{end})*gt(scene,0.20)',showinfo",
        "-an", "-f", "null", "-"
    ]).stderr
    cuts = times(cut_log)
    # Include last source frame in the selected interval to preserve tail coverage.
    tail_log = run([
        "ffmpeg", "-hide_banner", "-i", str(source), "-map", f"0:{video['index']}",
        "-vf", f"select='gte(t,{args.start})*lt(t,{end})',showinfo", "-an", "-f", "null", "-"
    ]).stderr
    tail = times(tail_log)[-1]
    if tail > timestamps[-1] + 0.0001:
        path = out / f"frame-{len(frames) + 1:06d}.jpg"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(source),
            "-ss", str(tail), "-frames:v", "1", "-vf", "scale=640:-2", str(path)
        ])
        frames.append(path)
        timestamps.append(tail)
    font = ImageFont.load_default(size=22)
    sheets = []
    for first in range(0, len(frames), 12):
        group = frames[first:first + 12]
        with Image.open(group[0]) as im:
            height = im.height
        canvas = Image.new("RGB", (2560, (height + 34) * 3), "#181818")
        draw = ImageDraw.Draw(canvas)
        for offset, frame in enumerate(group):
            x, y = offset % 4 * 640, offset // 4 * (height + 34)
            with Image.open(frame) as im:
                canvas.paste(im, (x, y + 34))
            draw.text((x + 10, y + 5), f"{timestamps[first + offset]:.3f}s | {frame.stem}", fill="white", font=font)
        path = out / f"sheet-{first // 12 + 1:03d}.jpg"
        canvas.save(path, quality=90)
        sheets.append(path.name)
    audio = next((s for s in metadata["streams"] if s["codec_type"] == "audio"), None)
    audio_info = None
    if audio:
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(source),
            "-ss", str(args.start), "-t", str(end - args.start), "-map", f"0:{audio['index']}",
            "-vn", "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", str(out / "audio.wav")
        ])
        rms = []
        with wave.open(str(out / "audio.wav"), "rb") as f:
            index = 0
            while raw := f.readframes(320):
                samples = array.array("h", raw)
                if sys.byteorder != "little":
                    samples.byteswap()
                energy = math.sqrt(sum(s * s for s in samples) / len(samples)) / 32768
                rms.append({"time": round(args.start + index / 16000, 5), "rms_dbfs": round(20 * math.log10(max(energy, 1e-9)), 2)})
                index += len(samples)
        save(out / "audio-energy.json", {"window_seconds": 0.02, "interpretation": "Energy only; not dialogue, impacts, music or emotion", "points": rms})
        audio_info = {"file": "audio.wav", "source_offset": args.start, "energy": "audio-energy.json"}
    save(out / "manifest.json", {
        "source": str(source), "sha256": digest.hexdigest(), "video_duration": duration,
        "range": [args.start, end], "sampling_fps_requested": args.fps,
        "timestamps": "Source PTS in seconds; auto-rotation follows FFmpeg",
        "frames": [{"file": p.name, "time": t} for p, t in zip(frames, timestamps)],
        "sheets": sheets, "cut_candidates": cuts,
        "cuts_status": "Unverified; check adjacent source frames visually", "audio": audio_info
    })
    print(json.dumps({"out": str(out), "frames": len(frames), "sheets": len(sheets), "cut_candidates": cuts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
