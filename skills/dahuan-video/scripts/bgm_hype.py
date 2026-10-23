#!/usr/bin/env python3
"""Energetic 128-bpm bed for 视频号 voice-over videos -> WAV (48k mono).
Sections: intro build -> drop A (at --drop1, e.g. the hook slam) -> half-time tension (--break-start..--break-end)
-> snare-roll build -> drop C (at --drop2) -> end at --dur.
usage: bgm_hype.py --dur 59.3 --drop1 2.2 --break-start 41.0 --break-end 49.5 --drop2 53.3 --out bgm.wav"""
import os, json, numpy as np
import scipy.io.wavfile as wf
from scipy.signal import butter, sosfilt, sawtooth, lfilter

import argparse
ap = argparse.ArgumentParser()
for a in ("--dur", "--drop1", "--break-start", "--break-end", "--drop2"): ap.add_argument(a, type=float, required=True)
ap.add_argument("--out", default="bgm.wav"); ap.add_argument("--seed", type=int, default=11)
A = ap.parse_args()
SR = 48000
DUR = A.dur; N = int(SR * (DUR + 1.0))
rng = np.random.default_rng(A.seed)

BPM = 128; BEAT = 60 / BPM; BAR = 4 * BEAT
T0 = A.drop1
B_START, B_END = A.break_start, A.break_end
BUILD_END = A.drop2

def tt(d): return np.arange(int(SR * d)) / SR
def lp(x, f, o=2): return sosfilt(butter(o, min(f, SR / 2 - 100), btype="low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, btype="high", fs=SR, output="sos"), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], btype="band", fs=SR, output="sos"), x)
def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
def put(buf, t, x, g=1.0):
    i = int(round(t * SR)); j = min(len(buf), i + len(x))
    if i < 0: x = x[-i:]; i = 0
    if i < len(buf): buf[i:j] += g * x[: j - i]

def supersaw(f, d, voices=7, det=0.011):
    t = tt(d); x = np.zeros_like(t)
    for k, s in enumerate(np.linspace(-1, 1, voices)):
        x += sawtooth(2 * np.pi * f * (1 + s * det) * t + rng.uniform(0, 2 * np.pi))
    return x / voices

PROG = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]   # Am F C G
ROOT = [45, 41, 48, 43]

pads = np.zeros(N); bass = np.zeros(N); lead = np.zeros(N)
kick = np.zeros(N); perc = np.zeros(N); fx = np.zeros(N)
pump = np.ones(N)

def kick_hit(t0, g=1.0):
    t = tt(0.42); f = 48 + 110 * np.exp(-t * 32)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5)
    click = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 400) * 0.35
    put(kick, t0, np.tanh((body + click) * 1.6) * g)
    i = int(t0 * SR); env = 1 - 0.6 * np.exp(-tt(BEAT) * 11)
    j = min(len(pump), i + len(env))
    if 0 <= i < len(pump): pump[i:j] = np.minimum(pump[i:j], env[: j - i])
def clap(t0, g=0.5):
    x = np.zeros(int(0.35 * SR))
    for k, dly in enumerate((0, 0.011, 0.022)):
        t = tt(0.35 - dly); n = bp(rng.standard_normal(len(t)), 900, 4500) * np.exp(-t * (60 if k < 2 else 16))
        x[int(dly * SR):int(dly * SR) + len(n)] += n
    put(perc, t0, x * g)
def snare(t0, g=0.4):
    t = tt(0.2); x = bp(rng.standard_normal(len(t)), 1200, 6000) * np.exp(-t * 28) + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * 0.6
    put(perc, t0, x * g)
def hat(t0, open_=False, g=0.12):
    d = 0.22 if open_ else 0.05; t = tt(d)
    put(perc, t0, hp(rng.standard_normal(len(t)), 8000) * np.exp(-t * (14 if open_ else 90)) * g)
def crash(t0, g=0.35):
    t = tt(2.2); put(fx, t0, hp(rng.standard_normal(len(t)), 5200) * np.exp(-t * 2.2) * g)
def riser(t0, d, g=0.3):
    t = tt(d); n = rng.standard_normal(len(t)); out = np.zeros_like(n); seg = int(0.05 * SR)
    for s in range(0, len(n), seg):
        frac = s / len(n); out[s:s + seg] = hp(n[s:s + seg + 200], 300 + 6000 * frac ** 2)[:len(out[s:s + seg])]
    sweep = sawtooth(2 * np.pi * np.cumsum(110 * 2 ** (3 * t / d)) / SR) * 0.15
    put(fx, t0, (out * 0.6 + lp(sweep, 3000)) * (t / d) ** 2 * g)
def roll(t0, t1, g0=0.12, g1=0.55):
    t = t0
    while t < t1 - 0.01:
        f = (t - t0) / (t1 - t0); snare(t, g0 + (g1 - g0) * f ** 1.5)
        t += BEAT / 2 if f < 0.4 else (BEAT / 4 if f < 0.75 else BEAT / 8)

def chord_bar(t0, ci, cutoff, g=0.22, length=BAR):
    x = np.zeros(int(SR * (length + 0.2)))
    for m in PROG[ci] + [PROG[ci][0] + 12]:
        s = supersaw(hz(m), length + 0.2); x[:len(s)] += s
    t = tt(length + 0.2); env = np.minimum(1, t / 0.02) * np.minimum(1, (length + 0.2 - t) / 0.2)
    put(pads, t0, lp(x, cutoff, 2) * env * g)
def bass_bar(t0, ci, mode="drive"):
    f = hz(ROOT[ci] - 12)
    if mode == "drive":            # offbeat 8ths + 16th push, saw + sub
        for e in range(8):
            if e % 2 == 0: continue
            t = tt(BEAT / 2 * 0.95); s = (sawtooth(2 * np.pi * f * 2 * t) * 0.5 + np.sin(2 * np.pi * f * t)) * np.exp(-t * 3)
            put(bass, t0 + e * BEAT / 2, lp(s, 700) * 0.55)
        for e in (0, 4):
            t = tt(BEAT / 2); put(bass, t0 + e * BEAT / 2, np.sin(2 * np.pi * f * t) * np.exp(-t * 6) * 0.35)
    else:                           # sustained sub
        t = tt(BAR); put(bass, t0, np.sin(2 * np.pi * f * t) * np.minimum(1, t / 0.05) * np.minimum(1, (BAR - t) / 0.1) * 0.5)
def lead_bar(t0, ci, g=0.1):
    notes = PROG[ci] + [PROG[ci][0] + 12, PROG[ci][1] + 12]
    pat = [0, 2, 4, 2, 3, 2, 4, 1, 0, 2, 4, 2, 3, 4, 2, 1]
    for e, k in enumerate(pat):
        t = tt(0.24); f = hz(notes[k] + 12)
        s = (sawtooth(2 * np.pi * f * t) + 0.5 * sawtooth(2 * np.pi * f * 2.003 * t)) * np.exp(-t * 11)
        put(lead, t0 + e * BEAT / 4, lp(s, 5200) * g * (1.0 if e % 4 == 0 else 0.75))

# ---- intro build: 0 -> T0
pre = max(0.0, T0)
if pre > 0.3:
    t = tt(pre); x = np.zeros_like(t)
    for m in PROG[0]: x += supersaw(hz(m), pre)[:len(t)]
    cut = 400 + 3500 * (t / pre) ** 2; y = np.zeros_like(x); seg = int(0.04 * SR)
    for s in range(0, len(x), seg): y[s:s + seg] = lp(x[s:s + seg + 400], cut[s])[:len(y[s:s + seg])]
    put(pads, 0, y * (0.3 + 0.7 * t / pre) * 0.18)
    riser(0, pre, 0.32); roll(max(0, pre - 1.6), pre, 0.08, 0.45)

# ---- drop A: T0 -> B_START
def groove(a, b, drop_cut=4200, lead_on=True, crash_first=True, fills=True):
    k = 0; t0 = a
    while t0 < b - 0.05:
        ci = k % 4; full = min(BAR, b - t0)
        chord_bar(t0, ci, drop_cut, 0.2, full); bass_bar(t0, ci, "drive")
        if lead_on and k >= 2: lead_bar(t0, ci, 0.085)
        for q in range(4):
            tb = t0 + q * BEAT
            if tb >= b: break
            kick_hit(tb, 0.9)
            if q in (1, 3): clap(tb, 0.42)
            hat(tb + BEAT / 2, True, 0.11)
            for s16 in (1, 3): hat(tb + s16 * BEAT / 4, False, 0.05)
        if fills and k % 8 == 7: roll(t0 + 3 * BEAT, t0 + BAR, 0.15, 0.4)
        if (k % 8 == 0 and (k > 0 or crash_first)): crash(t0, 0.3)
        k += 1; t0 += BAR
groove(T0, B_START)

# ---- half-time tension: cold scene
k = 0; t0 = B_START
while t0 < B_END - 0.05:
    ci = k % 4; full = min(BAR, B_END - t0)
    chord_bar(t0, ci, 900, 0.16, full); bass_bar(t0, ci, "sub")
    kick_hit(t0, 0.75); snare(t0 + 2 * BEAT, 0.3)
    if t0 + 3.5 * BEAT < B_END: kick_hit(t0 + 3.5 * BEAT, 0.45)
    for q in range(8): hat(t0 + q * BEAT / 2, False, 0.035)
    k += 1; t0 += BAR

# ---- build: reinv scene -> drop C
bl = BUILD_END - B_END
t = tt(bl); x = np.zeros_like(t)
for m in PROG[3]: x += supersaw(hz(m), bl)[:len(t)]
cut = 700 + 4500 * (t / bl) ** 2; y = np.zeros_like(x); seg = int(0.04 * SR)
for s in range(0, len(x), seg): y[s:s + seg] = lp(x[s:s + seg + 400], cut[s])[:len(y[s:s + seg])]
put(pads, B_END, y * 0.2)
q = 0
while B_END + q * BEAT < BUILD_END - 0.05: kick_hit(B_END + q * BEAT, 0.6 + 0.3 * q * BEAT / bl); q += 1
roll(B_END, BUILD_END, 0.1, 0.6); riser(B_END, bl, 0.35)

# ---- drop C: end scene
groove(BUILD_END, DUR - 0.3, fills=False)
crash(BUILD_END, 0.38)
kick_hit(DUR - 0.3, 1.0); crash(DUR - 0.3, 0.3)

# ---- mixdown
delay = int(SR * BEAT * 0.75); lead_d = lead.copy(); lead_d[delay:] += 0.32 * lead[:-delay]
music = (pads * pump * 1.35 + bass * pump * 0.65 + lead_d * (0.6 + 0.4 * pump) * 1.6) + kick * 0.62 + perc * 1.15 + fx * 1.1
music = hp(music, 30)
music = np.tanh(music * 1.25) / 1.25
music /= np.max(np.abs(music)) + 1e-9
music = music[: int(SR * DUR)] * 0.95
wf.write(A.out, SR, (music * 32767).astype(np.int16))
print(A.out, round(len(music) / SR, 2), "s  T0", round(T0, 2), "break", round(B_START, 2), "-", round(B_END, 2), "dropC", round(BUILD_END, 2))
