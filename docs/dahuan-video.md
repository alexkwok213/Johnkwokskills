# 大欢视频号创作与成片（dahuan-video）

独立承接视频号全流程：从「思路主题对齐 → 口播脚本撰写与改稿」到「`1080×1920` 竖屏成片制作、音效混音、质感检查与 `1080×1440` 封面归档」。真实原片提供证据，解释动画讲清事实，配音、配乐和大字字幕按实际语音时间轴严格对齐。

[下载 ZIP](../packages/dahuan-video.zip) · [技能源码](../skills/dahuan-video/SKILL.md) · [套件整包](../packages/dahuan-suite.zip) · [返回套件说明](dahuan.md)

## 适合什么任务

- 新案例从头做起：先与用户对齐「内核、角度、基调、前 3 秒钩子」，写出干净人话口播脚本，待文字认可后转入配音与竖屏成片制作。
- 已有定稿口播做成片：把确认的口播与一组真实原片做成 `1080×1920` 竖屏成片与配套 `1080×1440`（兼容 4:3）封面。
- 局部修订视频：只调整字幕、配乐、某段画面或气口停顿，沿用既定版式与文字认可结果。

写公众号长文用 `dahuan-article`；做 3:4 贴图用 `dahuan-image-post`；只分析参考视频表演与写生视频提示词，用独立的 `video-performance-clone`。

## 内置资料与工程工具

| 模块 | 用途 | 文件 |
|---|---|---|
| 口播写作与叙事法则 | 动笔前四要素对齐、泥潭战友站位、两大案例叙事、按题材区分角标边界与防 AI 腔 | [spoken.md](../skills/dahuan-video/references/spoken.md)、[voice.md](../skills/dahuan-video/references/voice.md)、[ai-business-cases.md](../skills/dahuan-video/references/ai-business-cases.md) |
| 原片＋MG 方案（含黄金三段式） | 黑金商业案例起步参数、顶部双行大字＋纯净主视觉＋上提大字字幕、120ms 气口标准 | [recipes/original-footage-mg.md](../skills/dahuan-video/references/recipes/original-footage-mg.md) |
| 采访原声与数字人 | 整句边界切分、音频淡出呼吸、数字人小窗避让主角 | [interview-and-avatar.md](../skills/dahuan-video/references/interview-and-avatar.md) |
| 声音、质检与渲染 | 试听顺序、混音起点、HTML 逐帧渲染器（2 秒技术样片与测试）及剪映配音历史参考 | [sound-and-checks.md](../skills/dahuan-video/references/sound-and-checks.md)、[rendering.md](../skills/dahuan-video/references/rendering.md)、[jianying-tts.md](../skills/dahuan-video/references/jianying-tts.md) |
| 工程辅助脚本 | 逐帧渲染、配乐起点生成、响度与静音检查、声音诊断、剪映音频切分、字幕生成 | `skills/dahuan-video/scripts/` |

## 怎样判断做好了

- **口播文字先经确认**：新增或改写台词需向用户展示并获认可后，才进入配音和渲染。
- **音画与视听复核**：完整回看成片首帧、转场和结尾，手机外放实际试听人声清晰度与配乐让位；抽帧核对字幕折行、遮挡与画面空窗；切勿拿单张静态截图 `zoompan` 凑长度，也不要用自动化脚本参数替代实际视听检查。

## 运行环境要求

逐帧渲染需要 Python 3.10+、`skills/dahuan-video/requirements.txt` 依赖、Chromium 与带 `libx264` 的 `ffmpeg`。配音依赖本地剪映或你自己的 TTS 工具；仓库不附带作者原始媒体、私人音色或平台账号。
