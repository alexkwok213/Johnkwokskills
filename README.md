# Johnkwokskills

把 AI 内容创作中反复要交代的方法，整理成可以安装的技能。这里包含公众号与视频号创作、成片、封面、贴图、小红书改写，以及视频表演拆解与提示词等做法。

## 大欢创作套件：文章、口播、成片、封面、贴图

提供选题、链接、视频或已有素材，让 AI 帮你选角度、组织素材，写成公众号文章或视频号口播；需要时再做成竖屏成片、公众号封面和 3:4 贴图。面向 AI 入门及关注 OPC 的读者，重点是讲清楚有什么用、怎样开始。

[下载套件整包](packages/dahuan-suite.zip) · [套件介绍](docs/dahuan.md) · [安装与使用](#安装与使用)

下面是一次 WorkBuddy 科普稿制作出的 **10 张贴图示例**。张数按内容决定，不固定凑十张。

![WorkBuddy 贴图版实际成品预览](docs/assets/dahuan-image-post-preview.png)

### 五个技能怎样配合

| 技能 | 帮你完成什么 | 介绍与源码 | 单独下载 |
|---|---|---|---|
| `dahuan` | 统一入口：判断这次要什么产物，读取项目已有进度，交给对应技能；存放共同原则与项目记录方法 | [介绍](docs/dahuan.md) · [源码](skills/dahuan/SKILL.md) | 已含在各单包中 |
| `dahuan-writer` | 研究命题、选角度和案例，写公众号文章或视频号口播 | [介绍](docs/dahuan-writer.md) · [源码](skills/dahuan-writer/SKILL.md) | [ZIP](packages/dahuan-writer.zip) |
| `dahuan-video` | 已确认口播做成竖屏成片：原片、解释动画、配音、配乐、字幕与检查 | [介绍](docs/dahuan-video.md) · [源码](skills/dahuan-video/SKILL.md) | [ZIP](packages/dahuan-video.zip) |
| `dahuan-cover` | 提炼封面短句与画面，用 AI 生成横版封面并检查中央方形裁切 | [介绍](docs/dahuan-cover.md) · [源码](skills/dahuan-cover/SKILL.md) | [ZIP](packages/dahuan-cover.zip) |
| `dahuan-image-post` | 把同一选题改成以图片为主的逐页图解，导出上传图片与短正文 | [介绍](docs/dahuan-image-post.md) · [源码](skills/dahuan-image-post/SKILL.md) | [ZIP](packages/dahuan-image-post.zip) |

每个专用技能都可以直接调用；没指定时由 `dahuan` 选择。只要文案就停在文案，只改字幕就只改字幕；明确授权从材料做到成片时，按顺序做完。项目里记录给谁看、哪些事实已核实、哪版被认可、做到哪一步，换聊天或换模型也能接着做。

一次被认可的黑金商业案例成片做法，保存为 [原片＋MG 制作方案](skills/dahuan-video/references/recipes/original-footage-mg.md)：保留具体参数，但不强加给所有题材。

### 安装与使用

推荐安装整套。

1. 下载上面的 ZIP，解压得到 `dahuan`、`dahuan-writer`、`dahuan-video`、`dahuan-cover`、`dahuan-image-post` 五个文件夹。
2. 放入你使用的 AI 助手的技能目录。Codex 的个人技能目录通常是 `~/.codex/skills/`；以实际配置为准。
3. 在新的对话轮次中提供素材，并提出需求，例如：

> 使用 $dahuan，把这个 AI 商业案例写成视频号口播，先给我看文案；我确认后再做成片。

> 使用 $dahuan-writer，把这些材料做成一篇 AI 新功能科普，交付公众号长文和 3:4 贴图两版。

也可以把下面这句话发给支持从 GitHub 安装技能的助手：

> 请从 https://github.com/alexkwok213/Johnkwokskills 安装 skills/dahuan、skills/dahuan-writer、skills/dahuan-video、skills/dahuan-cover 和 skills/dahuan-image-post，告诉我怎么开始使用。

单独下载的 `dahuan-*` 包里已附带 `dahuan` 文件夹（共同原则在里面），两者放在同一个技能目录即可。原来的 [三技能整包](packages/dahuan-publishing-suite.zip) 链接仍可用，现在内容与套件整包相同。

### 能拿到什么

- **文章**：正文、配图、可复制的公众号富文本预览；需要时加横版封面和贴图版。
- **口播**：标题与完整口播，素材/分镜建议另列，不混进配音正文。
- **成片**：1080×1920 竖屏成片、可编辑工程和制作记录，注明哪些已回看、哪些已试听。
- **贴图**：默认 1080×1440、3:4 的编号图片、整套预览、图片压缩包，以及标题与短正文。
- **封面**：默认按 2.35:1 横版和同图中央 1:1 裁切设计，交付实际生成图、提示词及尺寸说明。

下面这张封面的实际尺寸为 **1922×818，约 2.35:1**，已在本地查看横版与中央方形裁切。

![WorkBuddy 公众号封面实际成品](docs/assets/dahuan-cover-example.png)

### 使用前需要什么

技能是给 AI 助手读取的工作方法，需要在支持技能的助手中使用。研究、网页查看、图像生成、配音、视频渲染和图片导出，分别依赖助手实际具备的工具。

- 新命题需要可靠资料；有真实实操时用实操，没有合适实操时可用核实过的功能或案例，不编造亲历。
- AI 封面需要图像生成能力；配音需要你自己的剪映或已配置的 TTS。仅安装技能不会额外提供这些服务。
- 成片渲染需要 Python、Playwright/Chromium 和 ffmpeg，见 [渲染入口](skills/dahuan-video/references/rendering.md)。技能不含作者的原始视频、音色或账号。
- 公众号后台粘贴、上传及手机显示仍要实际检查。本地预览通过不等于平台已验收；技术检测通过也不等于成片被认可。
- 发布、发送或改动外部账号，按当前用户的明确指示执行。

更多写作方法见[从命题到文章](skills/dahuan-writer/references/topic-to-article.md)、[发布排版](skills/dahuan-writer/references/publication.md)和[与卡兹克原文的比较](skills/dahuan-writer/references/khazix-comparison.md)。

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
