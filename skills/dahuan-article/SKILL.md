---
name: dahuan-article
description: 大欢公众号推文创作与发布排版技能。负责公众号推文的选题研究、长文写作/改稿、20字强反差标题提炼、微信内联 HTML 一键排版（Base64 JPG/GIF 与原生 SVG SMIL 动效）、以及 2.35:1/1:1 双裁切封面制作。用户要写公众号文章、修改稿件、做推文排版预览或做公众号推文封面时使用；做 3:4 贴图用 dahuan-image-post，做视频号口播与成片用 dahuan-video。
---

# 大欢公众号推文创作与排版

本技能独立服务于 **公众号长文推文**（与 `dahuan-image-post` 贴图、`dahuan-video` 视频并列为大欢三大平行载体技能，无总入口依赖）。

先读 [共同原则与红线](references/principles-and-red-lines.md)，再查同选题已有项目记录（[项目记录约定](references/project-records.md)）与历史修改；不编造亲历、收入与实测，未经当前明确授权不自动在外部平台发布。

## 先定读者、主线与承诺

1. 默认读者是对 AI 与一人项目（OPC）感兴趣的普通人：先讲人、需求、动作与可见结果，再解释必要技术，照顾初学者并保留准确边界。
2. 新选题或全文重构先读 [从命题到文章](references/topic-to-article.md) 与 [文章写作规范](references/article.md)；AI 商业案例选材结合 [AI商业案例](references/ai-business-cases.md)。
3. 一期只定一种风格，选前只查 [风格索引](styles/index.md) 与 [风格与参照](references/styles.md)，不中途混用多种风格或盲目套用模板。
4. 局部修改保留已认可的开头、观点和结构，只同步受影响段落与交付物；判断边界读 [增量制作与审批边界](references/incremental-production.md)。

## 标题、正文与配图要求

- **20 字强反差标题**：首选 20 字以内、具体动作/数字与回报形成强反差的简洁短标题（如`36元开谷歌AI会员，竟还送顶级AI云服务器`），背景细节放进导语或首段承接。
- **活人感与去 AI 味**：读 [大欢的声音](references/voice.md)，少用路标词（“值得注意的是”“不仅如此”“本质上”）、翻案腔与三连问，用具体人、动作、钱和时间推着读。
- **配图真实性与极简图注**：产品功能、账单与价格优先采用真实一手截图或 HTML/CSS 代码渲染的高清中文对比图，**严禁把含文字或表格的网页截图喂给 AI 生图模型重绘或拼合**。图注 `.caption` 保持极简，仅写画面主体，不加「xx实拍：」冗余前缀。
- **板块序号清晰对齐**：章节序号（如 `01`、`02`）与小标题同排稳重对齐，不用过小独立换行号（参考 `threejs.cc` 的排版克制与留白）。

## 微信内联排版与双裁切封面

- **一键复制 HTML**：完整实现与接口约定见 [发布排版规范](references/publication.md) 及 [公众号正文复制脚本](assets/wechat-copy.js)。
  - 静态图转 JPEG Data URI（`data:image/jpeg;base64,...`），动态演示保留 GIF Data URI（`data:image/gif;base64,...`），并在复制 `<img>` 上写入 `data-w` 与 `data-ratio`。
  - 动效仅用公众号原生支持的循环型 SVG SMIL 动画（`<animate>` / `<animateTransform>` / `<animateMotion>`）；**禁止点击触发态 `begin="click"` + `<set>`**；复制清理 `id` 时**必须排除 `<svg>` 内部节点**。
- **2.35:1 + 1:1 双裁切封面**：读 [双裁切封面规范](references/cover.md) 与 [双裁切案例](references/dual-crop-example.md)。先确保标题和完整核心主体舒适落在中央 1:1 区域内，再平衡横版两翼；交付时检查实际尺寸及缩略图可读性。

## 交付与如实汇报

- 区分「本地 HTML 可预览」「剪贴板 `text/html` 验证通过」「公众号后台草稿保存且图片加载完成」「正式发布」四个状态，仅报告已实际完成与核验到的状态。
- 经验积累与常见纠错见 [推文经验库](references/lessons.md)；具体写作节奏与改稿示范按需读 [写作与改稿判断](references/writing-craft.md)、[认可写法案例](references/accepted-workflow.md) 与 [纠错示例](references/revision-examples.md)。
