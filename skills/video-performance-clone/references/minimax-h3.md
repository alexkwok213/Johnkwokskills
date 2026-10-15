# MiniMax H3：首帧与全参考两套结构

核对日期：2026-10-15。依据MiniMax官方写作指南整理；此文件自包含，不要求另装依赖技能。有本地 `h3-prompt-writing` 时可读取对应指南核对复杂台词、音频复用或首尾帧情形，但不改变本技能已确认的用户取舍。

- [官方模型与模式](https://www.minimax.io/news/minimax-h3-open-source)
- [官方base指南](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md)
- [官方reference指南](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md)

## 共同规则

给中文使用说明，正式生成正文按指南使用英文，原对白/歌词/可见文字保留原语言。若用户明确要求中文正文则遵从，保留字段与引用标签。以下字段是**提示词内部结构**，不是自行发明的API参数。

只使用确认过、实际上传的素材。仅首帧不增加产品图或视频；全参考才建立额外标签。同一镜头内动作使用 `First, Next, Finally` 等先后词，不为三个阶段创建三个 `[Shot]`。多镜头用 `[Shot 1]`、`[Shot 2]`，只有真实切镜才写 `the camera cuts to`。

**用户默认不要动作秒表**，因此正文不逐段添加时间。首帧格式保留官方0.00绑定首行，它仅声明哪张图是开场。官方多镜示例会给切镜时间；本用户选择顺序版本时按其偏好省略切点数字，保留真实镜头次序，不宣称这是逐帧精确控制；需要精确卡点再协商采用官方时间写法。

动作细节足以执行即可，不为满足示例字数而增加本不存在的微动作、表情或音效。总时长和画幅放生成设置中，不借模板承诺某个第三方入口的能力。

适配三字段或六字段时，保留关键情绪对应的可见神情、视线、身体承重、接触与听者反应，按 [prompt-directing.md](prompt-directing.md) 执行。“自然发挥”不替代关键表演描写，也不要求照搬人类皮肤或面部结构到动物角色。

## 仅首帧：I2VA

第一行使用：

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

空行后按顺序输出三个字段：

1. `integrated_multimodal_description`：从`[Shot 1]`和首帧真实状态起步，继承人物/产品/场景/构图，以First/Next/Finally写后续动作、反应和自然变化。全程一镜时只出现一个Shot。
2. `overall_soundscape`：环境和动作音；明确要求整片静音时为`N/A`，并在视觉正文说明目标完全静音。没听到音轨不等于确认没有声音，来源限制留在报告。
3. `non_diegetic_music`：观众层配乐；无配乐为`N/A`。

完整示例：[food-h3-first.txt](examples/food-h3-first.txt)。首尾帧模式若用户另行提出，再按官方base指南调整绑定，不把两张图误当全参考产品图。

## 全能参考：Ref2VA

按以下顺序输出六个字段，不能把首帧三字段结构直接改名冒充全参考：

1. `subject_definitions`：定义实际要复用的`<Subject N>`，图片/视频/音频用`<Picture N>`、`<Video N>`、`<Audio N>`标明来源及职责。图片作为具体开场锚点时单列Picture；仅提供某个产品外观时可在对应Subject定义中引用Picture。
2. `summary`：以`[reference generation]`或`[keyframe completion + reference generation]`说明任务，使用已定义标签，不把动作参考误写成`video editing`。
3. `retention_analysis`：按已定义职责说明`fully_preserved`、`partially_preserved`、`attribute_transfer`或`weak_reference`；这些是要求保留的角色属性，不是已生成效果的评分。只参考运镜时不能标“保留整段视频所有内容”。
4. `detailed_description`：先用一两句说明风格，再从`[Shot 1]`展开，首次可见时写出对应Subject的关键特征、位置和动作；在开场/产品/镜头真正生效处使用标签。用先后顺序写动作，避免只列引用关系而没有可执行画面。
5. `overall_soundscape`。
6. `non_diegetic_music`。

首帧/开场图在Ref2VA里可定义为画面锚点，不能将其等同于另一个FL2VA接口的严格首帧参数，也不默认用户入口支持两者混传。

完整示例：[food-h3-omni.txt](examples/food-h3-omni.txt)。若视频仅提供运镜和动作，视频里的脸和产品不自动被继承；产品外形优先产品图，目标身份优先首帧/人物图。

## 对白及引用校验

发声主体用稳定`(S1)`、`(S2)`，台词格式为`<d>[Chinese] 原台词。</d>`；静音角色不强加说话者ID。画外音标明实际角色嘴唇保持闭合。不要添加未确认的Audio引用。

检查所有Subject/Picture/Video/Audio标签在各字段含义一致、素材真实存在，开场姿态与实际图片相容。所有关键动作有画面描述，微动作仍允许自然发挥。字段适配和静态检查通过不等于已验证成片。
