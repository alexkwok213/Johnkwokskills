#!/usr/bin/env python3
"""Warm, uplifting 100-bpm piano-pop bed (original, synthesized) arranged to plan.json -> bgm.wav.
Sections: soft intro (keys + pad) -> groove from the hook result -> stripped break ("then")
-> lift for the advice + ending, closing on a held chord.
Expects plan.json with scenes "hook" (cue "rev"), "then", "vg"; edit T0/B_START/LIFT for other projects."""
import os, json, numpy as np
import scipy.io.wavfile as wf
from scipy.signal import butter, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
PL = json.load(open(os.path.join(HERE, "plan.json")))
DUR = PL["dur"]; N = int(SR * (DUR + 1.5))
SC = {s["id"]: s for s in PL["scenes"]}
rng = np.random.default_rng(7)

BPM = 100; BEAT = 60 / BPM; BAR = 4 * BEAT
T0 = SC["hook"]["cues"]["rev"]
B_START, B_END = SC["then"]["a"], SC["vg"]["a"]
LIFT = SC["vg"]["a"]

def tt(d): return np.arange(int(SR * d)) / SR
def lp(x, f, o=2): return sosfilt(butter(o, min(f, SR / 2 - 100), btype="low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, btype="high", fs=SR, output="sos"), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], btype="band", fs=SR, output="sos"), x)
def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
def put(buf, t, x, g=1.0):
    i = int(round(t * SR)); j = min(len(buf), i + len(x))
    if i < 0: x = x[-i:]; i = 0
    if i < len(buf): buf[i:j] += g * x[: j - i]

PROG = [[62, 66, 69, 74], [59, 62, 66, 71], [55, 59, 62, 67], [57, 61, 64, 69]]   # D Bm G A
ROOT = [38, 35, 43, 45]

def epiano(f, d, g=1.0):
    t = tt(d); mod = np.sin(2 * np.pi * f * 2 * t) * 1.2 * np.exp(-t * 3.5)
    x = np.sin(2 * np.pi * f * t + mod) * np.exp(-t * 1.6) + 0.25 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 6)
    a = int(0.004 * SR); x[:a] *= np.linspace(0, 1, a); r = int(0.08 * SR); x[-r:] *= np.linspace(1, 0, r)
    return x * g
def pad(f, d):
    t = tt(d); x = np.zeros_like(t)
    for det in (-0.006, 0, 0.007):
        ph = rng.uniform(0, 2 * np.pi); x += np.sin(2 * np.pi * f * (1 + det) * t + ph) + 0.3 * np.sin(4 * np.pi * f * (1 + det) * t + ph)
    env = np.minimum(1, t / 0.6) * np.minimum(1, (d - t) / 0.6)
    return x * env / 3
def pluck(f, d=0.35):
    t = tt(d); return (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 9)
def bass_note(f, d):
    t = tt(d); x = np.sin(2 * np.pi * f * t) + 0.2 * np.sin(4 * np.pi * f * t)
    env = np.minimum(1, t / 0.01) * np.exp(-t * 0.8); r = int(0.05 * SR); env[-r:] *= np.linspace(1, 0, r)
    return x * env
def kick():
    t = tt(0.4); return np.sin(2 * np.pi * (48 + 70 * np.exp(-t * 28)) * t) * np.exp(-t * 9)
def clap():
    t = tt(0.25); return bp(rng.standard_normal(len(t)), 900, 4000) * np.exp(-t * 22)
def shaker():
    t = tt(0.06); return hp(rng.standard_normal(len(t)), 6000) * np.exp(-t * 70)

keys = np.zeros(N); pads = np.zeros(N); arp = np.zeros(N); bass = np.zeros(N); drums = np.zeros(N); fx = np.zeros(N)
ARP = [0, 2, 1, 3, 2, 1, 3, 2]
for b in range(int(DUR / BAR) + 2):
    t0 = b * BAR; ch = PROG[b % 4]; rt = ROOT[b % 4]
    in_break = B_START - 0.2 <= t0 < B_END - 0.2
    full = t0 >= T0 - BAR * 0.5 and not in_break
    lift = t0 >= LIFT - 0.3
    for m in ch: put(pads, t0, pad(hz(m - 12), BAR + 0.3), 0.55 if not lift else 0.7)
    for off, g in ((0, 1.0), (1.5 * BEAT, 0.6), (3 * BEAT, 0.5)):
        for m in ch[:3]: put(keys, t0 + off, epiano(hz(m), 1.2), g * 0.33)
    if full or lift:
        for k in range(8): put(arp, t0 + k * BEAT / 2, pluck(hz(ch[ARP[k]] + 12)), 0.22 if not lift else 0.3)
        for bt in range(4):
            put(bass, t0 + bt * BEAT, bass_note(hz(rt), BEAT * 0.95), 0.5)
            if bt in (0, 2) or (lift and bt == 3): put(drums, t0 + bt * BEAT, kick(), 0.8)
            if bt in (1, 3): put(drums, t0 + bt * BEAT, clap(), 0.35)
            for s in range(4 if lift else 2): put(drums, t0 + bt * BEAT + s * BEAT / (4 if lift else 2), shaker(), 0.08)
    elif in_break:
        put(bass, t0, bass_note(hz(rt), BAR * 0.9), 0.35)
d = max(0.5, LIFT - (B_END - 2 * BAR)); t = tt(d)
put(fx, LIFT - d, lp(rng.standard_normal(len(t)), 3000) * (t / d) ** 2 * 0.12)
for m in PROG[0]: put(keys, DUR - 1.6, epiano(hz(m), 2.5), 0.3)
music = keys + pads * 0.45 + arp * 0.9 + bass * 0.55 + drums * 0.7 + fx
for dl, g in ((0.11, 0.25), (0.23, 0.15), (0.37, 0.08)):
    k = int(dl * SR); music[k:] += g * music[:-k] * 0.6
music = hp(music, 35); music = np.tanh(music * 1.1) / 1.1
music /= np.max(np.abs(music)) + 1e-9
music = music[: int(SR * DUR)] * 0.9
wf.write(os.path.join(HERE, "bgm.wav"), SR, (music * 32767).astype(np.int16))
print("bgm.wav", round(len(music) / SR, 2), "s")
