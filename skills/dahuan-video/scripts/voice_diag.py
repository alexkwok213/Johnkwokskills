import sys, subprocess, numpy as np
from scipy.signal import butter, sosfilt
SR=16000
def load(p):
    raw=subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar",str(SR),"-f","s16le","-"],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(float)/32768
def f0_track(x):
    hop=160; win=640; f0=[]; hnr=[]
    for i in range(0,len(x)-win,hop):
        s=x[i:i+win]*np.hanning(win)
        if np.sqrt(np.mean(s**2))<0.01: continue
        ac=np.correlate(s,s,'full')[win-1:]; ac/=ac[0]+1e-9
        lo,hi=int(SR/400),int(SR/70); k=lo+np.argmax(ac[lo:hi]); r=ac[k]
        if r>0.45: f0.append(SR/k); hnr.append(10*np.log10(r/(1-r+1e-9)))
    return np.array(f0),np.array(hnr)
def bands(x):
    F=np.abs(np.fft.rfft(x))**2; f=np.fft.rfftfreq(len(x),1/SR); tot=F.sum()
    g=lambda a,b: 10*np.log10(F[(f>=a)&(f<b)].sum()/tot+1e-12)
    cen=(F*f).sum()/tot
    return g(80,300),g(300,1000),g(1000,2500),g(2500,5000),g(5000,8000),cen
if len(sys.argv)<2 or sys.argv[1] in ("-h","--help"):
    print("usage: voice_diag.py AUDIO [AUDIO ...]\n输出基频、谐噪比与频带能量，仅作诊断线索，不判断好不好听。")
    sys.exit(0 if len(sys.argv)>1 else 2)
for p in sys.argv[1:]:
    x=load(p); f0,h=f0_track(x); b=bands(x)
    print(f"{p.split('/')[-2][-12:]+'/'+p.split('/')[-1]:34s} F0 med {np.median(f0):5.0f}Hz  F0 spread {np.std(f0):4.0f}  HNR {np.median(h):4.1f}dB | 80-300 {b[0]:5.1f} 300-1k {b[1]:5.1f} 1-2.5k {b[2]:5.1f} 2.5-5k {b[3]:5.1f} 5-8k {b[4]:5.1f} | centroid {b[5]:4.0f}Hz")
