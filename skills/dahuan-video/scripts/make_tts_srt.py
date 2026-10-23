#!/usr/bin/env python3
"""Turn a narration list (one line per paragraph, UTF-8 txt) into an SRT whose cues start at 0, SLOT, 2*SLOT ...
Import it in 剪映「文本 → 导入本地字幕」, select all, 朗读, export audio only, then run split_jianying.py.
usage: make_tts_srt.py lines.txt out.srt --slot 15"""
import sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument("lines"); ap.add_argument("out"); ap.add_argument("--slot", type=int, default=15)
A = ap.parse_args()
L = [l.strip() for l in open(A.lines, encoding="utf-8") if l.strip()]
ts = lambda s: f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d},000"
open(A.out, "w", encoding="utf-8").write("\n".join(f"{i+1}\n{ts(i*A.slot)} --> {ts(i*A.slot+A.slot-3)}\n{t}\n" for i, t in enumerate(L)))
print(f"{len(L)} cues, slot {A.slot}s -> {A.out}")
