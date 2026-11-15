# Johnkwokskills

自用的内容创作与多模态视频技能集合：按目标载体拆分、每项技能自带完整规则与参考示例，解压即可单独或成套安装使用。

## 大欢内容创作套件（dahuan-suite）

围绕大欢及「大欢AI工坊」的真实商业案例与工具科普工作流，按发布载体**彻底拆分为三大平行自包含技能**：推文长文（`dahuan-article`）、3:4 贴图（`dahuan-image-post`）、视频号创作与成片（`dahuan-video`）。

[下载套件整包](packages/dahuan-suite.zip) · [套件说明](docs/dahuan.md) · [安装与使用](#安装与使用)

![WorkBuddy 贴图版实际成品预览](docs/assets/dahuan-image-post-preview.png)

### 三个平行技能

| 技能 | 定位与交付内容 | 文档与源码 | 单包下载 |
|---|---|---|---|
| `dahuan-article` | 公众号推文：选题、20 字强反差标题、去 AI 味长文、微信内联 HTML 一键排版（Base64 JPG/GIF 与原生循环 SVG 动效）、2.35:1/1:1 双裁切封面 | [介绍](docs/dahuan-article.md) · [源码](skills/dahuan-article/SKILL.md) | [ZIP](packages/dahuan-article.zip) |
| `dahuan-image-post` | 公众号贴图：将同一选题重组为 `1080×1440` 3:4 滑动图解卡片，HTML/CSS 渲染导出、手机可读性检查与短正文 | [介绍](docs/dahuan-image-post.md) · [源码](skills/dahuan-image-post/SKILL.md) | [ZIP](packages/dahuan-image-post.zip) |
| `dahuan-video` | 视频号全流程：思路四要素对齐、泥潭战友口吻口播撰写/改稿，以及 `1080×1920` 竖屏成片制作（原片、MG、配音、配乐、大字黄金三段字幕、120ms 气口与封面） | [介绍](docs/dahuan-video.md) · [源码](skills/dahuan-video/SKILL.md) | [ZIP](packages/dahuan-video.zip) |

一次被认可的黑金商业案例成片做法保存在 [原片＋MG 制作方案](skills/dahuan-video/references/recipes/original-footage-mg.md)，2026-11 实战进一步收敛为「黄金三段式纯净视觉与大字层级」，供按题材选用。

### 安装与使用

1. 下载 [dahuan-suite.zip](packages/dahuan-suite.zip) 解压获得 `dahuan-article`、`dahuan-image-post`、`dahuan-video` 三个完整独立目录，复制到助手技能目录（如 `~/.agents/skills/` 或 `~/.codex/skills/`）。
2. 如仅需其中一项载体能力，单独下载对应单包 ZIP 解压即可运行，**不依赖额外总入口文件夹**。原来的 [兼容性套件链接](packages/dahuan-publishing-suite.zip) 内容与 `dahuan-suite.zip` 完全一致。

![WorkBuddy 公众号封面实际成品](docs/assets/dahuan-cover-example.png)

> 使用 $dahuan-article，围绕这篇材料写出 20 字内强反差标题与公众号长文，生成带 Base64 图片和循环 SVG 动效的一键复制 HTML 预览，并制作双裁切封面。

> 使用 $dahuan-image-post，把这篇定稿改成一组 3:4（1080×1440）公众号贴图卡片，检查手机宽度清晰度，交付图片包与短正文。

> 使用 $dahuan-video，先对齐核心角度和前 3 秒钩子写出视频号口播稿，我确认后按黄金三段字幕与真实原片完成 1080×1920 竖屏成片。

### 运行条件

- 写作与图文整理无外部付费依赖；公众号双裁切封面需助手支持图像生成，贴图导出需要可用的浏览器截图环境；
- 成片逐帧渲染需要 Python 3.10+、Playwright/Chromium 和带 `libx264` 的 `ffmpeg`，详见 [渲染入口](skills/dahuan-video/references/rendering.md)。技能不含作者私人素材、音色与平台账号。
- 更多方法与实战复盘见 [从命题到文章](skills/dahuan-article/references/topic-to-article.md)、[发布排版规范](skills/dahuan-article/references/publication.md) 与 [口播叙事法则](skills/dahuan-video/references/spoken.md)。

## 小红书改写

[技能源码](skills/xiaohongshu-rewriter/SKILL.md) · [下载 ZIP](packages/xiaohongshu-rewriter.zip)

把原笔记或核实材料改写成小红书标题、正文与标签。角度和数量按材料能支撑的范围确定：材料不够时说明还缺什么，不用换词或虚构经历凑数。可独立安装，不依赖大欢套件。


## 视频表演拆解与复刻

[技能源码](skills/video-performance-clone/SKILL.md) · [下载 ZIP 技能包](packages/video-performance-clone.zip)

读取参考视频，拆解人物动作、神情、镜头和对白节奏。复刻前先确认 Seedance 2.5、Seedance 2.0、MiniMax H3 或可灵4.0，以及仅首帧图或全能参考；完整提示词直接出现在回复中，并保存为 `prompt.txt`。

- 将关键情绪转折写成可见的神情、视线、听者反应与重心变化，保留动作接触和连续性；非关键眨眼、小姿态与停顿自然发挥。
- 区分画面观察、声音测量与推测，不把自然姿态写成刻意动作。
- 配套带时间戳的抽帧、切镜候选、音轨和能量分析工具；样本可保存后再次调用。
- 生成正文默认使用第一阶段、第二阶段或真实镜头序号，核验用的秒数留在拆解报告里。
- [四模型 × 两输入方式：八份完整示例](skills/video-performance-clone/references/examples.md)。仓库与 ZIP 不含个人原视频、抽帧或本机样本库。
- [可灵4.0适配](skills/video-performance-clone/references/kling40.md)区分关键帧、全能参考与视频编辑，保留表演细节，注明正式版/Flash、素材额度和声音引用的差异。

### 安装与使用

可以把下面这句话发给支持技能安装的 AI 编程助手：

> 安装 https://github.com/alexkwok213/Johnkwokskills/tree/main/skills/video-performance-clone 这个技能，告诉我怎么用。

或下载 ZIP，将其中的 `video-performance-clone` 文件夹放入助手的技能目录。然后附上视频并说：

> 使用 $video-performance-clone 拆解这个视频。复刻前先问我要用哪个模型，以及仅首帧还是全能参考；把关键情绪写成具体表演，保留动作因果，非关键微动作自然发挥，按先后顺序给我可直接使用的提示词。

| 模型 | 仅首帧 | 全能参考 |
|---|---|---|
| Seedance 2.5 | 中文阶段顺序，继承首帧 | 中文素材职责与阶段顺序 |
| Seedance 2.0 | 中文镜头/动作顺序 | 中文素材绑定与顺序，不依赖精确秒点 |
| MiniMax H3 | I2VA首帧绑定＋三字段 | Ref2VA素材定义＋六字段 |
| 可灵4.0 | 关键帧入口，中文后续动作与表演 | 中文素材职责、连续事件与引号内台词 |

单镜头中的第一、第二阶段不会被写成切镜。H3格式保留必要的开场绑定，动作正文按先后顺序展开；首帧与全参考的实际模式限制见[输入方式说明](skills/video-performance-clone/references/input-modes.md)。

本地抽帧需要 Python、Pillow、FFmpeg 和 ffprobe。可在自己的虚拟环境中安装本技能的 `requirements.txt`，然后运行：

```bash
python scripts/extract_evidence.py /path/to/video.mp4 --out /path/to/empty-evidence-directory
```

可用 `--start`、`--end` 和 `--fps` 抽取局部动作。图像、声音理解和转写由所用助手及其可用工具完成；抽帧脚本不会独立判断人物情绪，也不会调用付费视频生成服务。

## 许可证

本仓库目前未提供统一许可证。
