# 贴图经验库

面向 3:4 公众号贴图与图片卡片的实操经验索引。跨选题复现的问题记入此处或 [贴图制作与检查](production.md)。

| 日期 | 用户要点 / 问题发现 | 做法 | 现在在哪里 |
|---|---|---|---|
| 10-16 | 贴图默认 1080×1440 (3:4)，浏览器仅设 `clip` 未设 `fullPage: true` 曾被视口截断为 1080×907 | 导出时同时设置 `fullPage: true`、`clip` 与 `scale: 'css'`，并读取输出图片实际像素 | [references/production.md](production.md) |
| 10-29 | 「文字不溢出」不等于审美通过；故事页硬套步骤框、全套同构模板显得死板 | 按内容性质区分首图、人物、步骤和结尾构图，统一字体、色彩与页码 | [references/production.md](production.md) |
| 11-15 | 官网中文对比截图交给 AI 生图重构导致文字扭曲失真；图注过长干扰阅读 | 对比表与中文图卡改用 HTML/CSS 代码高精度渲染导出，图注极简居中 | [references/production.md](production.md) |
