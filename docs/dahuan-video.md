# 大欢视频号成片

把已经确认的口播做成视频号竖屏成片：真实原片提供证据，解释动画讲清事实，配音、配乐和字幕按实际音频时长排布。

[下载套件整包](../packages/dahuan-suite.zip) · [单独下载](../packages/dahuan-video.zip) · [技能源码](../skills/dahuan-video/SKILL.md) · [返回目录](../README.md)

## 适合什么任务

- 把定稿口播和一组原片做成 1080×1920 竖屏成片。
- 修改已有成片的字幕、配乐、某一段画面或节奏，只动需要改的部分。
- 沿用项目里已经认可的版式和声音，做同类型的下一期。

只写文案用 `dahuan-writer`；只分析参考视频里的表演并写生成提示词，用独立的 `video-performance-clone`。

## 带了什么

| 内容 | 用途 |
|---|---|
| [原片＋MG 制作方案](../skills/dahuan-video/references/recipes/original-footage-mg.md) | 一次被认可的黑金商业案例做法：版式、字幕、音色、配乐和节奏的起点参数 |
| [声音与质检](../skills/dahuan-video/references/sound-and-checks.md) | 试听顺序、混音起点、技术检测的作用和限制 |
| [渲染入口](../skills/dahuan-video/references/rendering.md) | HTML 时间轴逐帧渲染成视频，含 2 秒技术样片和测试 |
| [剪映配音记录](../skills/dahuan-video/references/jianying-tts.md) | 用剪映朗读生成旁白和字幕的历史操作参考 |
| `scripts/` | 逐帧渲染、配乐起点生成、响度与静音检查、声音诊断、剪映音频切分、字幕生成 |

## 怎样判断做好了

完整回看成片，实际听开头、原声衔接、配乐有没有盖住人声和结尾；抽帧检查字幕断行、遮挡和空窗。响度、静音检测和单元测试只用来定位问题，不能代替听感，也不等于用户认可。

## 使用条件

渲染需要 Python 3.10+、`requirements.txt` 中的依赖、Chromium 和带 libx264 的 ffmpeg。配音依赖你自己的剪映或已配置的 TTS；技能不调用付费服务，也不附带作者的原始素材、音色或账号。
