"""Integration checks; DAHUAN_BROWSER selects an installed browser."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/render_frames.py'
BROWSER = os.environ.get('DAHUAN_BROWSER')


class RendererTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.output = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def run_renderer(self, mode='full', html=None, extra=()):
        command = [sys.executable, str(SCRIPT), mode, '--html', str(html or ROOT / 'assets/starter/index.html'),
                   '--output-dir', str(self.output), '--width', '360', '--height', '640', '--fps', '10']
        if BROWSER:
            command += ['--browser', BROWSER]
        return subprocess.run(command + list(extra), capture_output=True, text=True, timeout=90)

    def test_missing_html(self):
        result = self.run_renderer(html=self.output / 'missing.html')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('existing HTML file', result.stderr)
        self.assertNotIn('done ', result.stdout)

    @unittest.skipUnless(BROWSER, 'set DAHUAN_BROWSER for actual browser rendering')
    def test_two_seconds_and_preview(self):
        result = self.run_renderer()
        self.assertEqual(result.returncode, 0, result.stderr)
        probe = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                                '-show_entries', 'stream=width,height,nb_read_frames:format=duration',
                                '-of', 'json', str(self.output / 'video_noaudio.mp4')], capture_output=True, text=True, check=True)
        data = json.loads(probe.stdout)
        self.assertEqual(data['streams'][0]['nb_read_frames'], '20')
        self.assertEqual(data['streams'][0]['width'], 360)
        self.assertEqual(data['streams'][0]['height'], 640)
        self.assertAlmostEqual(float(data['format']['duration']), 2, places=2)
        preview = self.run_renderer(mode='preview')
        self.assertEqual(preview.returncode, 0, preview.stderr)
        from PIL import Image
        with Image.open(self.output / 'preview.jpg') as image:
            self.assertEqual(image.size, (1080, 640))
            # Deterministic moving dot must produce visually different time samples.
            self.assertNotEqual(image.crop((0, 0, 360, 640)).tobytes(), image.crop((720, 0, 1080, 640)).tobytes())

    @unittest.skipUnless(BROWSER, 'set DAHUAN_BROWSER for actual browser rendering')
    def test_encoder_failure_preserves_existing_output(self):
        target = self.output / 'video_noaudio.mp4'
        target.write_bytes(b'previous successful output sentinel')
        result = self.run_renderer(extra=['--ffmpeg', '/usr/bin/false'])
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('done ', result.stdout)
        self.assertEqual(target.read_bytes(), b'previous successful output sentinel')
        self.assertFalse((self.output / '.video_noaudio.rendering.mp4').exists())

    @unittest.skipUnless(BROWSER, 'set DAHUAN_BROWSER for actual browser rendering')
    def test_video_seek_settles_before_capture(self):
        video = self.output / 'colors.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i',
                        'color=c=red:s=360x640:r=10:d=0.5', '-f', 'lavfi', '-i',
                        'color=c=blue:s=360x640:r=10:d=0.5', '-filter_complex',
                        '[0:v][1:v]concat=n=2:v=1:a=0', '-c:v', 'libx264',
                        '-pix_fmt', 'yuv420p', str(video)], check=True)
        html = self.output / 'seek.html'
        html.write_text('<body style="margin:0"><video src="colors.mp4" preload="auto" '
                        'style="width:100vw;height:100vh"></video><script>'
                        'window.TL={dur:1}; window.render=t=>{document.querySelector("video").currentTime=t;};</script>')
        result = self.run_renderer(mode='preview', html=html)
        self.assertEqual(result.returncode, 0, result.stderr)
        from PIL import Image
        with Image.open(self.output / 'preview.jpg') as image:
            red = image.getpixel((180, 320))
            blue = image.getpixel((900, 320))
            self.assertGreater(red[0], 200)
            self.assertLess(red[2], 30)
            self.assertGreater(blue[2], 200)
            self.assertLess(blue[0], 30)

    @unittest.skipUnless(BROWSER, 'set DAHUAN_BROWSER for actual browser rendering')
    def test_broken_image_fails(self):
        html = self.output / 'broken.html'
        html.write_text('<img src="missing.png"><script>window.TL={dur:0.1}; window.render=t=>{};</script>')
        result = self.run_renderer(html=html)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Image failed', result.stderr)
        self.assertFalse((self.output / 'video_noaudio.mp4').exists())


if __name__ == '__main__':
    unittest.main()
