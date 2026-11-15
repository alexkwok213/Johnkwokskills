# 推文经验库

用户纠正过、且能迁移到后续公众号推文的判断。开工前只查与当前环节相关的条目；跨选题复现两次或用户明确要求“以后都这样”时，升格写进对应参考文件并在这里留一行索引。

## 规矩

- 单次修正先记在当期项目 `修改与复盘.md`。
- 「用户要点」只记用户原话与明确反馈；技术推断注明推断来源。

## 已沉淀进参考文件的经验

| 日期 | 用户要点 | 现在在哪里 |
|---|---|---|
| 10-16 | 标题和开头是黄金三秒，字词要值得读者的注意力 | [references/article.md](article.md) |
| 10-21 | 删掉无关职业、设备标签，第一句单独要有吸引力 | [references/ai-business-cases.md](ai-business-cases.md) |
| 10-22、10-25 | 收入口号、价格接下载、收费相关表达影响审核和推流 | [references/principles-and-red-lines.md](principles-and-red-lines.md) |
| 10-24 | 改稿时风格被悄悄换掉，写乱了 | [references/styles.md](styles.md) |
| 10-26 | 三连问、提示性冒号、对仗口号像 AI；规则过多抑制发挥 | [references/voice.md](voice.md) |
| 11-15 | 标题要够简洁又有反差（如`36元开谷歌AI会员，竟还送顶级AI云服务器`） | [references/article.md](article.md) |
| 11-15 | 章节序号太小且独立换行显得生硬，参考优秀前端对齐（threejs.cc）；图片下方图注精简，去掉「实拍：」冗余前缀；官网对比图自己用中文重做，不拿原图给 AI 拼接 | [references/article.md](article.md)、[references/publication.md](publication.md) |
| 11-15 | 复制进公众号时外部图片/大图易丢失，应转 Base64 JPG/GIF 并写 `data-w`/`data-ratio`；原生循环 SVG SMIL 动效可正常复制且需保留 `<svg>` 内部 `id`，但点击交互态 `begin="click"` + `<set>` 效果不需要且会乱码 | [references/publication.md](publication.md)、[../assets/wechat-copy.js](../assets/wechat-copy.js) |
