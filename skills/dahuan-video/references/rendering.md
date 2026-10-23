# 可移植逐帧渲染

这是无声画面渲染器。不会自动制作旁白、混音或判断内容质量。`assets/starter/index.html` 是 2 秒技术样片，不是成功案例，也不能代表真实选题已验收。

## 环境

- Python 3.10+；用独立虚拟环境安装 `pip install -r requirements.txt`（渲染用 Playwright/Pillow，配乐与声音诊断脚本另需 numpy/scipy）。
- 系统安装 ffmpeg（须带 libx264）；ffprobe 用于核查输出。
- 默认先执行 `python -m playwright install chromium`。已有 Chrome/Chromium 时，可用 `--browser /path/to/browser`，无需再下载浏览器。
- 从技能目录运行下列命令，或把路径替换为绝对路径。输出放自己的项目内。

```bash
python scripts/render_frames.py preview 0 1 1.9 --html assets/starter/index.html --output-dir /path/to/project/render-check --width 360 --height 640
python scripts/render_frames.py full --html assets/starter/index.html --output-dir /path/to/project/render-check --width 360 --height 640 --fps 10
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_read_frames:format=duration -of json /path/to/project/render-check/video_noaudio.mp4
```

输出 `preview.jpg` 或 `video_noaudio.mp4`。默认 1080×1920、30 fps；尺寸须为偶数。完整渲染帧数为 `ceil(TL.dur * fps)`，时长最多向上补不足一帧。仅编码成功后替换目标视频；失败返回非零退出码，不报告成功，也不覆盖旧的有效输出。重复运行会替换同名成功输出；同一输出目录不要并发渲染。

## HTML 合约

必须定义 `window.TL = {dur: 秒数}` 和 `window.render(t)`。每帧只由秒数 `t` 决定；不要依赖实时播放、随机数、CSS 自运行动画或上一个帧的状态。`render` 可返回 Promise，渲染器会等待。

先等待页面网络空闲，每帧等待字体、`img` 解码、HTML 音视频资源加载及 seek 完成、两次浏览器绘制。视频需暂停并由 `render(t)` 设置 `currentTime`，显示有效片段内的时刻；未加载或损坏媒体会失败。CSS 背景、WebGL/Canvas 自定义纹理或其他异步资源应由项目自行 preload，并通过 `render` 的 Promise 表示就绪。不要直接渲染不可信网页。

把技术样片复制到项目中再改。真实素材使用相对于 HTML 的路径，例如 `assets/shot.mp4`；不带个人电脑路径、账号或音色文件。自行录制/已获授权的媒体放项目目录。合成旁白与配乐后，仍需实际听辨和完整回看。

## 检查

```bash
python -m unittest discover -s tests -v
```

集成检查需显式设置 `DAHUAN_BROWSER` 为已有 Chrome/Chromium 可执行文件路径；未设置时会跳过真实渲染。检查覆盖 2 秒、20 帧输出与预览、真实视频 seek 后画面变色、缺失 HTML、损坏图片、ffmpeg 失败和旧输出保护。通过这些只说明渲染链路工作，不等于创作质量合格。
