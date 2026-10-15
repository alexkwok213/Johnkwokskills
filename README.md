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

## 小红书改写

[小红书改写技能](skills/xiaohongshu-rewriter/SKILL.md)


## 视频表演拆解与复刻

[技能源码](skills/video-performance-clone/SKILL.md) · [下载 ZIP 技能包](packages/video-performance-clone.zip)

读取参考视频，拆解人物动作、神情、镜头和对白节奏，默认输出适用于 Seedance 2.5 的中文生成提示词。完整提示词直接出现在回复中，并保存为 `prompt.txt`。

- 保留关键动作、情绪转折和连续性，让细微表情、眨眼与手部姿态自然发挥。
- 区分画面观察、声音测量与推测，不把自然姿态写成刻意动作。
- 配套带时间戳的抽帧、切镜候选、音轨和能量分析工具；样本可保存后再次调用。
- [吃播生成提示词示例](skills/video-performance-clone/references/examples/food-prompt.txt)。仓库与 ZIP 不含个人原视频、抽帧或本机样本库。

### 安装与使用

可以把下面这句话发给支持技能安装的 AI 编程助手：

> 安装 https://github.com/alexkwok213/Johnkwokskills/tree/main/skills/video-performance-clone 这个技能，告诉我怎么用。

或下载 ZIP，将其中的 `video-performance-clone` 文件夹放入助手的技能目录。然后附上视频并说：

> 使用 $video-performance-clone 拆解这个视频，保留关键动作，细微表演自然发挥，给我一条可直接粘贴到 Seedance 2.5 的完整提示词。

本地抽帧需要 Python、Pillow、FFmpeg 和 ffprobe。可在自己的虚拟环境中安装本技能的 `requirements.txt`，然后运行：

```bash
python scripts/extract_evidence.py /path/to/video.mp4 --out /path/to/empty-evidence-directory
```

可用 `--start`、`--end` 和 `--fps` 抽取局部动作。图像、声音理解和转写由所用助手及其可用工具完成；抽帧脚本不会独立判断人物情绪，也不会调用付费视频生成服务。
