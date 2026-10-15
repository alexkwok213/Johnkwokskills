# Johnkwokskills

个人 AI 技能集合。

## 大欢公众号写作

[技能源码](skills/dahuan-writer/SKILL.md) · [下载 ZIP 技能包](packages/dahuan-writer.zip)

面向 AI 入门及关注 OPC 的读者，从真实事件、具体需求和可见成果展开，用通俗解释连接实际使用与生意机会。

- 用吸睛事件切入，让案例沿同一条主线推进，工具在读者需要时出现。
- 实操展示实际给 AI 的话、过程、用时与成果；资料核验保存在后台。
- 重点选择性加粗，关键总结和结尾共鸣句加粗标红。
- 配套公众号富文本复制代码，以及 2.35:1 横版、中央 1:1 裁切的封面设计指导。

### 安装与使用

可以把下面这句话发给支持技能安装的 AI 编程助手：

> 安装 https://github.com/alexkwok213/Johnkwokskills/tree/main/skills/dahuan-writer 这个技能，告诉我怎么用。

也可以下载 ZIP，解压后将 `dahuan-writer` 文件夹放到所用助手的技能目录。Codex 的个人技能目录为 `~/.codex/skills/`。

安装后可这样提出需求：

> 请使用 $dahuan-writer，把这些材料写成面向 AI 入门和 OPC 读者的公众号文章。先确定主线，再直接讲事件，用真实实操支撑判断，并检查重点排版和发布准备。

本技能允许按相关写稿上下文自动调用；明确指定的新读者、文体和交付要求优先。

### 配套文件

- [认可的写作方式](skills/dahuan-writer/references/accepted-workflow.md)
- [发布排版与双裁切封面](skills/dahuan-writer/references/publication.md)
- [与卡兹克原文的比较](skills/dahuan-writer/references/khazix-comparison.md)
- [改稿纠错示例](skills/dahuan-writer/references/revision-examples.md)
- [公众号复制代码](skills/dahuan-writer/assets/wechat-copy.js)

## 大欢公众号封面

[技能源码](skills/dahuan-cover/SKILL.md) · [下载 ZIP 技能包](packages/dahuan-cover.zip)

根据文章提炼短文案和核心画面，用 AI 生成同图适配 2.35:1 横版与中央 1:1 裁切的公众号封面。

- 先设计中央方形，再向两侧扩展；标题和完整核心主体都留在安全区内。
- 配套本次真实使用的生成提示词，以及“目标尺寸不等于实际输出尺寸”的检查经验。
- 检查中文、缩略图可读性、真实像素尺寸与两种裁切，保存原图及最终提示词。
- 可独立使用，也能接在大欢公众号写作定稿之后。

把下面这句话发给支持技能安装的 AI 编程助手：

> 安装 https://github.com/alexkwok213/Johnkwokskills/tree/main/skills/dahuan-cover 这个技能，告诉我怎么用。

安装后附上文章并说：

> 请使用 $dahuan-cover，根据这篇文章生成封面，让 2.35:1 横版和中央 1:1 裁切都保留完整标题与核心画面。

技能需要所用助手具备图像生成能力，优先使用内置 image_gen；仅安装技能不会自行提供图像生成服务。

## 小红书改写

[小红书改写技能](skills/xiaohongshu-rewriter/SKILL.md)


## 视频表演拆解与复刻

[技能源码](skills/video-performance-clone/SKILL.md) · [下载 ZIP 技能包](packages/video-performance-clone.zip)

读取参考视频，拆解人物动作、神情、镜头和对白节奏。复刻前先确认 Seedance 2.5、Seedance 2.0 或 MiniMax H3，以及仅首帧图或全能参考；完整提示词直接出现在回复中，并保存为 `prompt.txt`。

- 保留关键动作、情绪转折和连续性，让细微表情、眨眼与手部姿态自然发挥。
- 区分画面观察、声音测量与推测，不把自然姿态写成刻意动作。
- 配套带时间戳的抽帧、切镜候选、音轨和能量分析工具；样本可保存后再次调用。
- 生成正文默认使用第一阶段、第二阶段或真实镜头序号，核验用的秒数留在拆解报告里。
- [三模型 × 两输入方式：六份完整示例](skills/video-performance-clone/references/examples.md)。仓库与 ZIP 不含个人原视频、抽帧或本机样本库。

### 安装与使用

可以把下面这句话发给支持技能安装的 AI 编程助手：

> 安装 https://github.com/alexkwok213/Johnkwokskills/tree/main/skills/video-performance-clone 这个技能，告诉我怎么用。

或下载 ZIP，将其中的 `video-performance-clone` 文件夹放入助手的技能目录。然后附上视频并说：

> 使用 $video-performance-clone 拆解这个视频。复刻前先问我要用哪个模型，以及仅首帧还是全能参考；保留关键动作，细微表演自然发挥，按先后顺序给我可直接使用的提示词。

| 模型 | 仅首帧 | 全能参考 |
|---|---|---|
| Seedance 2.5 | 中文阶段顺序，继承首帧 | 中文素材职责与阶段顺序 |
| Seedance 2.0 | 中文镜头/动作顺序 | 中文素材绑定与顺序，不依赖精确秒点 |
| MiniMax H3 | I2VA首帧绑定＋三字段 | Ref2VA素材定义＋六字段 |

单镜头中的第一、第二阶段不会被写成切镜。H3格式保留必要的开场绑定，动作正文按先后顺序展开；首帧与全参考的实际模式限制见[输入方式说明](skills/video-performance-clone/references/input-modes.md)。

本地抽帧需要 Python、Pillow、FFmpeg 和 ffprobe。可在自己的虚拟环境中安装本技能的 `requirements.txt`，然后运行：

```bash
python scripts/extract_evidence.py /path/to/video.mp4 --out /path/to/empty-evidence-directory
```

可用 `--start`、`--end` 和 `--fps` 抽取局部动作。图像、声音理解和转写由所用助手及其可用工具完成；抽帧脚本不会独立判断人物情绪，也不会调用付费视频生成服务。
