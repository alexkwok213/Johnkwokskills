# 双裁切提示词与实际案例

## 2026-10-15 的案例

文章讲 AI 快速重做游戏与软件，面向 AI 入门及 OPC 读者。封面使用「游戏还没发售 / AI 已经复刻了」，中央两幅呼应的方块游戏窗口表达重做关系，左右分别补充图片编辑和视频剪辑场景。背景浅色，黑色大字，AI 与游戏方块使用少量珊瑚红。

这些是本篇的创意选择，不是所有文章的固定元素。画面是 AI 生成的封面插画，不是具体产品的真实截图。

### 实际尺寸带来的经验

提示词要求 2350×1000，实际生成 1920×819，宽高比约 2.344:1。按宽 1920 计算，2.35:1 的高度约 817.02，相差约 2 像素；不能将原图描述为精确 2350×1000。

实际原图的中央方形连续坐标约为 `x=550.5` 至 `1369.5`，高 819。图中的两行标题与两幅游戏窗口都需要完整落在这一范围内。此前交付记录说明了中央范围，但没有腾讯后台双裁切截图验收；后续执行技能时仍需查看实际裁切预览。

重要经验：先设计中央方形的完整故事，再利用横版两翼；不要先做左右分栏的大海报，最后才发现方形只能截出半个标题。

## 可替换的提示词结构

按实际文章替换花括号内容，坐标按目标画布重新计算，不照搬案例。不要把占位符送入生成工具。

```text
Asset: Chinese WeChat editorial cover, landscape 2.35:1, opaque background.
Target canvas: {WIDTH} x {HEIGHT} pixels.
Article idea: {ONE SENTENCE ABOUT THE ARTICLE'S ACTUAL CHANGE OR RESULT}.
Visual style: {STYLE MATCHING THE ARTICLE AND USER'S REFERENCE}.

The SAME image will be centrally cropped to a 1:1 square.
The square runs from x={LEFT} to x={RIGHT}, y=0 to y={HEIGHT}.
Keep all essential words and the COMPLETE primary subject inside this square,
with comfortable margins. The square alone must tell a complete story.
The outer wings contain only expendable supporting scenery.
Do not draw crop guides or safe-area lines into the final image.

Exact text, line 1: {TITLE_LINE_1}
Exact text, line 2 if needed: {TITLE_LINE_2}
Use legible simplified Chinese; preserve spelling; AI must be uppercase.
The text must remain readable at small thumbnail size.
Primary subject: {SUBJECT AND THE VISIBLE RELATIONSHIP THAT EXPLAINS THE TOPIC}.
Side wings: {SECONDARY CONTEXT, OPTIONAL}.
Avoid: {ONLY RELEVANT DISTRACTIONS OR UNWANTED ELEMENTS}.
```

## 本次实际生成提示词

下面保留本次成功生成的输入，供理解层级与安全区表达。它不是尺寸输出保证；坐标仅适用于这次要求的画布。

```text
Use case: ads-marketing.
Generate a polished Chinese WeChat public-account article cover, a NEW image. Requested exact output canvas: 2350 pixels wide by 1000 pixels high, landscape aspect ratio 2.35:1. Opaque background.
Article topic: AI can rapidly recreate a game after seeing its prototype, and rebuild useful parts of professional software, allowing an individual to turn an idea into a working product. Cover conveys this idea visually; it is an editorial illustration, not a real screenshot.
Visual direction: refined editorial graphic design, light warm white / pale gray background, bold black Chinese typography, restrained coral-red accent matching colorful falling-block gameplay, realistic desktop application-window styling, subtle soft shadows. Professional, clear, clean and attractive at thumbnail size. No cartoon robots, no sci-fi brains, no neon, no dramatic dollar bills, no coins, no busy infographic.
MANDATORY dual-crop-safe layout: The same image will also be centrally cropped to a 1:1 square. Keep ALL important words and the COMPLETE central game-window composition inside the central 850 x 850 area, centered at (1175,500). Central 1:1 crop is x=675 to1675, y=0 to1000. Leave generous space inside that square. No visible safe-area lines or crop guides. Left and right outer wings only contain secondary imagery/background.
Inside the central square: two bold, elegant centered lines of perfectly legible simplified Chinese, above the main game illustration.
Text verbatim, line 1: “游戏还没发售”
Text verbatim, line 2: “AI 已经复刻了”
No additional headings or caption. Do not include quote marks. All letters AI must be uppercase. Text should occupy roughly y=130–360 and fit well inside x=775–1575, with strong typographic hierarchy and optical balance.
Below the text, centered within x=770–1580 and y=430–860: a striking pair of overlapping floating desktop game windows showing two versions of the SAME elegant rotating falling-block puzzle game, with a grid and bright coral, blue and gold tetromino pieces. One window sits slightly behind, the recreated window in front; a short subtle red connector between them implies rapid recreation. Both complete window frames must be fully inside the central square. Game windows have small neutral macOS-style controls, and NO tiny words or brand logos.
Outer left wing: secondary cropped image-editing window with photo, layer thumbnails and color sliders. Outer right wing: secondary cropped video-editing window with preview and multitrack timeline. These look sophisticated but remain visually subordinate and can disappear in the square crop. No tiny gibberish text; represent interface controls with shapes, no copied brand assets or logos.
The full wide composition must feel intentional, with balanced side wings, while the central square alone is a complete, beautiful cover. Leave margins at top and bottom, crisp contours, high-quality typesetting, no watermark, no borders.
```
