# Johnkwokskills

大欢（大欢AI工坊）内容创作开放技能集：围绕真实商业案例与工具科普工作流，按发布载体**拆分为三个完全独立、自包含的平行技能**——公众号推文（`dahuan-article`）、3:4 公众号贴图（`dahuan-image-post`）、视频号创作与成片（`dahuan-video`）。

[下载整套套件 ZIP](packages/dahuan-suite.zip) · [安装与使用](#安装与使用)

![WorkBuddy 贴图版实际成品预览](docs/assets/dahuan-image-post-preview.png)

## 三个平行技能

| 技能 | 定位与交付内容 | 文档与源码 | 单包下载 |
|---|---|---|---|
| `dahuan-article` | 公众号推文：选题、20 字强反差标题、去 AI 味长文、微信内联 HTML 一键排版（Base64 JPG/GIF 与原生循环 SVG 动效）、2.35:1/1:1 双裁切封面 | [介绍](docs/dahuan-article.md) · [源码](skills/dahuan-article/SKILL.md) | [ZIP](packages/dahuan-article.zip) |
| `dahuan-image-post` | 公众号贴图：将同一选题重组为 `1080×1440` 3:4 滑动图解卡片，HTML/CSS 渲染导出、手机可读性检查与短正文 | [介绍](docs/dahuan-image-post.md) · [源码](skills/dahuan-image-post/SKILL.md) | [ZIP](packages/dahuan-image-post.zip) |
| `dahuan-video` | 视频号全流程：思路四要素对齐、泥潭战友口吻口播撰写/改稿，以及 `1080×1920` 竖屏成片制作（原片、MG、配音、配乐、大字黄金三段字幕、120ms 气口与封面） | [介绍](docs/dahuan-video.md) · [源码](skills/dahuan-video/SKILL.md) | [ZIP](packages/dahuan-video.zip) |

一次被认可的黑金商业案例成片做法保存在 [原片＋MG 制作方案](skills/dahuan-video/references/recipes/original-footage-mg.md)，2026-11 实战进一步收敛为「黄金三段式纯净视觉与大字层级」，供按题材选用。

## 安装与使用

1. 下载 [dahuan-suite.zip](packages/dahuan-suite.zip) 解压获得 `dahuan-article`、`dahuan-image-post`、`dahuan-video` 三个完整独立目录，复制到助手技能目录（如 `~/.agents/skills/` 或 `~/.codex/skills/`）。
2. 如仅需其中一项载体能力，单独下载对应单包 ZIP 解压即可运行，**不依赖额外总入口文件夹**。

![WorkBuddy 公众号封面实际成品](docs/assets/dahuan-cover-example.png)

> 使用 $dahuan-article，围绕这篇材料写出 20 字内强反差标题与公众号长文，生成带 Base64 图片和循环 SVG 动效的一键复制 HTML 预览，并制作双裁切封面。

> 使用 $dahuan-image-post，把这篇定稿改成一组 3:4（1080×1440）公众号贴图卡片，检查手机宽度清晰度，交付图片包与短正文。

> 使用 $dahuan-video，先对齐核心角度和前 3 秒钩子写出视频号口播稿，我确认后按黄金三段字幕与真实原片完成 1080×1920 竖屏成片。

## 运行条件

- 写作与图文整理无外部付费依赖；公众号双裁切封面需助手支持图像生成，贴图导出需要可用的浏览器截图环境；
- 成片逐帧渲染需要 Python 3.10+、Playwright/Chromium 和带 `libx264` 的 `ffmpeg`，详见 [渲染入口](skills/dahuan-video/references/rendering.md)。技能不含作者私人素材、音色与平台账号。
- 更多方法与实战复盘见 [从命题到文章](skills/dahuan-article/references/topic-to-article.md)、[发布排版规范](skills/dahuan-article/references/publication.md) 与 [口播叙事法则](skills/dahuan-video/references/spoken.md)。

## 许可证

本仓库目前未提供统一许可证。
