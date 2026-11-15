# 大欢内容创作套件（三大平行技能）

一套为 AI 助手设计的自媒体内容创作技能：面向对 AI 与一人项目（OPC）感兴趣的普通人，按发布载体**彻底拆分为三个相互独立、自包含的平行技能**，互不嵌套、各自完整可用。

[下载套件整包](../packages/dahuan-suite.zip) · [返回仓库目录](../README.md)

## 三大平行技能

| 技能 | 定位与职责 | 单包下载 | 介绍与源码 |
|---|---|---|---|
| `dahuan-article` | 公众号推文全流程：选题研究、长文写作/改稿、20字强反差标题、微信内联 HTML 一键排版（Base64 JPG/GIF 与原生 SVG SMIL 动效）、2.35:1/1:1 双裁切封面 | [dahuan-article.zip](../packages/dahuan-article.zip) | [介绍](dahuan-article.md) · [源码](../skills/dahuan-article/SKILL.md) |
| `dahuan-image-post` | 公众号 3:4 贴图：把定稿或核实资料重组成 `1080×1440` 多图卡片、竖版首图、HTML/CSS 导出与手机端可读性检查、预览与短正文 | [dahuan-image-post.zip](../packages/dahuan-image-post.zip) | [介绍](dahuan-image-post.md) · [源码](../skills/dahuan-image-post/SKILL.md) |
| `dahuan-video` | 视频号全流程：思路对齐、口播脚本撰写/改稿，以及 `1080×1920` 竖屏成片制作（原片剪辑、配音、配乐、大字黄金三段字幕、MG、质检与 `1080×1440` 封面归档） | [dahuan-video.zip](../packages/dahuan-video.zip) | [介绍](dahuan-video.md) · [源码](../skills/dahuan-video/SKILL.md) |

> **架构说明（2026-11 拆分升级）**：旧版 `dahuan`、`dahuan-writer`、`dahuan-cover`、`dahuan-image-post`、`dahuan-video` 五技能混合架构容易产生跨目录依赖与上下文污染。新版已将共同原则、红线与项目记录机制内置于每个独立技能内部，按当期目标载体直接调用对应技能即可，单包解压即可独立工作。

## 共同设计特点

- **按载体独立闭环，共用事实口径**：不编造亲历、收入与实测；真实截图、原片与示意画面分清。
- **不混用风格与跨载体硬套**：长文追求阅读推进与扫读抓重点，贴图追求 3:4 卡片与手机宽度一秒看懂，视频追求前 3 秒高光、120ms 紧凑气口与黄金三段式纯净画面。
- **如实区分交付状态**：明确区分「本地文件/预览完成」「剪贴板检查通过」「公众号后台草稿保存」「正式发布」，不拿本地截图替代平台验收。

## 怎样安装

1. 下载 [dahuan-suite.zip](../packages/dahuan-suite.zip) 解压得到 `dahuan-article`、`dahuan-image-post`、`dahuan-video` 三个独立目录；也可仅下载需要的单包 ZIP。
2. 将目标技能目录放入助手的技能目录（如 `~/.agents/skills/`、`~/.codex/skills/` 等）即可直接用 `$dahuan-article`、`$dahuan-image-post` 或 `$dahuan-video` 触发。

示例：

> 使用 $dahuan-article，围绕这篇一手材料完成公众号推文：提炼 20 字内强反差标题、生成内联 HTML 一键复制预览与双裁切封面。

> 使用 $dahuan-image-post，把这篇推文或核实资料改写成一组 3:4 公众号贴图卡片，导出 1080×1440 图片并检查手机阅读效果。

> 使用 $dahuan-video，先对齐思路和钩子写出视频号口播稿，我确认文字后再制作 1080×1920 竖屏成片。

## 运行依赖说明

图像生成、网页浏览与 TTS 配音分别依赖助手当前接入的工具；视频逐帧渲染需要 Python 3.10+、Playwright/Chromium 与带 `libx264` 的 `ffmpeg`（详见 [渲染入口](../skills/dahuan-video/references/rendering.md)）。本开源套件不包含作者私人账号、原始素材与内部归档系统。
