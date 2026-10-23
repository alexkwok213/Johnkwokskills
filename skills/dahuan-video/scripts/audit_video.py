#!/usr/bin/env python3
"""Pre-delivery audit for a vertical video: integrated loudness, silent stretches, first frame, contact sheet.
usage: audit_video.py video.mp4 [--times 1.5 7 20 ...] [--quiet-db -35]"""
import sys, re, subprocess, argparse, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("--times", type=float, nargs="*", default=[])
ap.add_argument("--quiet-db", type=float, default=-35.0); A = ap.parse_args()
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", A.video, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
I = re.findall(r"I:\s+(-?[\d.]+) LUFS", r); P = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)
print("integrated loudness:", I[-1] if I else "?", "LUFS (target about -14)", "| true peak:", P[-1] if P else "?", "dBFS")
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", A.video, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(float) / 32768; w = int(16000 * .3)
db = [20 * np.log10(np.sqrt(np.mean(x[i:i + w] ** 2)) + 1e-9) for i in range(0, len(x) - w, w // 2)]
q = [(round(i * .15, 2), round(d, 1)) for i, d in enumerate(db) if d < A.quiet_db]
print(f"quiet 0.3s windows (< {A.quiet_db} dBFS):", q or "none", "| duration", round(len(x) / 16000, 2), "s")
ts = [0.0] + A.times
from PIL import Image
ims = []
for t in ts:
    png = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", A.video, "-frames:v", "1", "-vf", "scale=270:-1", "-f", "image2", "-c:v", "png", "-"], capture_output=True).stdout
    import io; ims.append(Image.open(io.BytesIO(png)).convert("RGB"))
W, H = ims[0].size; sheet = Image.new("RGB", (W * len(ims), H))
for i, im in enumerate(ims): sheet.paste(im, (i * W, 0))
out = A.video.rsplit(".", 1)[0] + "_audit.jpg"; sheet.save(out, quality=85)
print("contact sheet (first frame + --times):", out)
