# 大欢公众号推文（dahuan-article）

面向公众号长文推文的一站式独立技能：把一手素材或选题整理成读者愿意点开并读完的长文，生成可直接粘贴进公众号编辑器的微信内联 HTML 预览（支持 Base64 JPG/GIF 图片与原生 SVG SMIL 循环动效），并制作同时兼容 `2.35:1` 横版与中央 `1:1` 方形的封面图。

[下载 ZIP](../packages/dahuan-article.zip) · [技能源码](../skills/dahuan-article/SKILL.md) · [套件整包](../packages/dahuan-suite.zip) · [返回套件说明](dahuan.md)

![WorkBuddy 公众号双裁切封面成品](assets/dahuan-cover-example.png)

## 适用场景

> 使用 $dahuan-article，研究这组资料并完成公众号长文：给我 20 字内强反差标题、去 AI 味正文，以及可一键复制进公众号的内联 HTML 预览。

> 使用 $dahuan-article，根据这篇定稿生成 2.35:1 推文封面，确保所有标题文字和核心主体都完整落在中央 1:1 裁切安全区内。

> 使用 $dahuan-article，检查本地排版 HTML 中的图片与 SVG 动效是否符合微信粘贴规范，不要破坏 SVG 内部 id 或塞入点击状态切换动画。

## 包含内容

| 模块 / 参考 | 用途 | 文件 |
|---|---|---|
| 共同原则、红线与项目记录 | 事实归属、版权/平台/时效边界、可接续项目档案与增量修改准则 | [principles-and-red-lines.md](../skills/dahuan-article/references/principles-and-red-lines.md)、[incremental-production.md](../skills/dahuan-article/references/incremental-production.md) |
| 从命题到长文与标题打磨 | 选题视角选择、20 字强反差标题法则、配图真实性（禁用 AI 重绘拼合 UI）与极简图注 | [topic-to-article.md](../skills/dahuan-article/references/topic-to-article.md)、[article.md](../skills/dahuan-article/references/article.md) |
| 大欢口吻与风格参照 | 活人感与去 AI 味清单；商业观察 / 观点拆解 / 案例速递三种风格索引 | [voice.md](../skills/dahuan-article/references/voice.md)、[styles/index.md](../skills/dahuan-article/styles/index.md) |
| 微信内联 HTML 一键排版 | JPG/GIF Base64 + `data-w`/`data-ratio` 写入、保留 `<svg>` 内部 `id`、原生循环 SMIL 边界 | [publication.md](../skills/dahuan-article/references/publication.md)、[wechat-copy.js](../skills/dahuan-article/assets/wechat-copy.js) |
| 2.35:1 + 1:1 双裁切封面 | 中央方形优先构图、实测案例与双裁切提示词模板 | [cover.md](../skills/dahuan-article/references/cover.md)、[dual-crop-example.md](../skills/dahuan-article/references/dual-crop-example.md) |

## 使用条件

- 独立文件夹 `dahuan-article` 解压后放入技能目录即可运行，无需再安装旧版 `dahuan`、`dahuan-writer` 或 `dahuan-cover`。
- 生成双裁切封面需助手接入图像生成工具；粘贴进公众号草稿箱需在当前已登录微信公众平台后台内操作或由用户手动粘贴。未真实在后台保存回读草稿前，仅报告本地预览与剪贴板检查状态。
