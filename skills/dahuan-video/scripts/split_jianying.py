#!/usr/bin/env python3
"""Split a 剪映 audio-only export whose narration clips start at 0, SLOT, 2*SLOT ... seconds
into <out>/N1..Nn.wav (trimmed, long pauses tightened) + durs.json (duration + pause midpoints per line).
usage: split_jianying.py export.wav --n 8 --slot 15 --out voice"""
import os, sys, json, subprocess, argparse, numpy as np
import scipy.io.wavfile as wf
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--n", type=int, default=8)
ap.add_argument("--slot", type=float, default=15.0); ap.add_argument("--out", default="voice")
A = ap.parse_args(); OUT = A.out; os.makedirs(OUT, exist_ok=True)
SR = 48000; SLOT = A.slot
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", A.src, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float64) / 32768
print(f"export length {len(x)/SR:.1f}s")
durs = {}
for i in range(A.n):
    k = f"N{i+1}"; seg = x[int(i * SLOT * SR): int((i + 1) * SLOT * SR)]
    hop = int(SR * 0.01); e = np.array([np.sqrt(np.mean(seg[j:j + hop] ** 2)) for j in range(0, len(seg) - hop, hop)])
    db = 20 * np.log10(e + 1e-9); on = np.where(db > db.max() - 40)[0]
    if len(on) == 0: raise SystemExit(f"{k}: no audio found in slot {i*SLOT:.0f}-{(i+1)*SLOT:.0f}s — check clip positions")
    a = max(0, on[0] * hop - int(0.03 * SR)); b = min(len(seg), (on[-1] + 1) * hop + int(0.06 * SR)); y = seg[a:b].copy()
    # gently tighten pauses longer than 0.35s to 0.22s
    h2 = int(SR * 0.02); e2 = np.array([np.sqrt(np.mean(y[j:j + h2] ** 2)) for j in range(0, len(y) - h2, h2)])
    q = 20 * np.log10(e2 + 1e-9) < (20 * np.log10(e2.max() + 1e-9) - 35); runs = []; st = None
    for kk, bb in enumerate(q):
        if bb and st is None: st = kk
        if not bb and st is not None:
            if (kk - st) * 0.02 > 0.35: runs.append((st * h2, kk * h2))
            st = None
    for r0, r1 in reversed(runs):
        keep = int(0.22 * SR); c0 = r0 + keep // 2; c1 = r1 - keep // 2; xf = int(0.02 * SR)
        if c1 - c0 > xf:
            y = np.concatenate([y[:c0 - xf], y[c0 - xf:c0] * np.linspace(1, 0, xf) + y[c1:c1 + xf] * np.linspace(0, 1, xf), y[c1 + xf:]])
    f = int(0.01 * SR); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    wf.write(os.path.join(OUT, f"{k}.wav"), SR, (np.clip(y, -1, 1) * 32767).astype(np.int16))
    h3 = int(SR * 0.01); e3 = np.array([np.sqrt(np.mean(y[j:j + h3] ** 2)) for j in range(0, len(y) - h3, h3)])
    q3 = 20 * np.log10(e3 + 1e-9) < (20 * np.log10(e3.max() + 1e-9) - 30); pz = []; st = None
    for kk, bb in enumerate(q3):
        if bb and st is None: st = kk
        if not bb and st is not None:
            if kk - st >= 7 and st > 5: pz.append(round((st + kk) / 2 * 0.01, 3))
            st = None
    durs[k] = {"dur": round(len(y) / SR, 3), "pauses": pz}
    print(k, f"{durs[k]['dur']:.2f}s  pauses {pz}")
json.dump(durs, open(os.path.join(OUT, "durs.json"), "w"), indent=1)
