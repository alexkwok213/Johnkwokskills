# 找风格和模板

先从视频用途、核心动作和制作工具组合出搜索词，例如 `MG 科普解说 插画 路径动画`、`kinetic typography editorial motion design explainer`、`Remotion animated timeline template`。中英文互补。打开候选的原始页面，能看示片就看最能说明风格的一段。候选数量以能形成实质比较为准，通常三条以内就够。

| 要找什么 | 首选来源 | 查验重点 |
| --- | --- | --- |
| 中文应用案例或创作入口 | [Fotor Agent](https://www.fotor.com.cn/agent/) 从灵感中心进入「MG动画解说 → 更多」，按需查「MG动效」或「产品发布视频」。 | 打开详情，交叉看起始简报和成片。 |
| 动画案例与平台模板 | [OiiOii](https://www.oiioii.tv/zh/) 从首页切到「Motion 动画 → 灵感」，查纯动效；找角色动画、场景或叙事节奏时，再查 [Oii TV](https://www.oiioii.tv/oii-tv?tab=creator)。 | 打开样片，确认画幅和动作；需要复用工程时，再核验「做同款」的具体内容、编辑和导出方式。 |
| 有示片和书面规则的风格 | [Lemo-Opuscar 中文画廊](https://lemomo-ai.github.io/lemo-opuscar/zh/) 和[源码仓库](https://github.com/lemomo-ai/lemo-opuscar)。 | 挑选具体风格页，对照可见示片和 `STYLE.md` 提炼规律。原仓库以代码制片为主，按当前任务核验运行方式和兼容性。 |
| 可编辑的 React 工程或组件 | [Remotion Starter Templates](https://www.remotion.dev/templates) 和 [Remotion Elements](https://www.remotion.dev/elements)。 | 查框架版本、替换文案和尺寸的难度、运行依赖、许可和预览结果。 |
| 制作技能模板 | [Remotion 官方 Agent Skills](https://www.remotion.dev/docs/ai/skills) 和 [Lemo-Opuscar 的技能目录](https://github.com/lemomo-ai/lemo-opuscar/tree/main/plugin/skills/lemo-opuscar)。 | 查实际入口和适用的 agent，确认脚本、下载、凭据和运行要求。把第三方技能当作参考资料，实际安装或执行前核对来源和内容，并遵守本次授权。 |

为每条候选提供原始链接，标记它是成片案例、风格说明、可编辑工程还是 Agent Skill。用具体细节说明哪个镜头可借用哪条规律，例如何时揭示标题、怎么用遮罩接下一镜、什么元素维持视觉连续。动态内容看不到时，只描述实际读到的文本或静帧。先试最匹配的一个方向，再决定是否需要继续找。

## 从案例提炼制作方案

按本次的表达问题筛选，例如怎样说明因果、怎样让观众看懂一组数字、怎样交代系统的步骤。优先找一个叙事结构接近的案例，再找一个视觉机制不同的案例。若要做选择，说明两种方案分别适合讲什么，以及各自要准备哪些素材。

| 参考入口 | 能借鉴的做法 |
| --- | --- |
| Fotor · [随机播放真的随机吗？](https://www.fotor.com.cn/agent/?template=2dd51f30-5b2a-44ba-b74a-91174a3ec07e) | 预览里用曲目网格和大计数器建立具体情境，起始简报再把概率条和对比安排到后段。适合从一个看得见的例子带出抽象概念。 |
| Fotor · [叫车之后，你不知道的那些事](https://www.fotor.com.cn/agent/?template=3ce4b77d-e706-4f30-8817-acbdc5a6f1bc) | 起始简报让同一张订单贯穿下单、匹配、接驾、行程、抵达，用卡片、地图路径和分步回顾拆解后台流程。可套用到物流、审批或支付等不同流程。 |
| Fotor · [MG动画解说分类](https://www.fotor.com.cn/agent/) | 数据比较先找「Q1到Q4公司业绩」，历史题材可找「互联网发展简史」「桑葚简史」，短内容可找「心理学三大误区」「凑单是真的省钱吗？」。打开详情后再确认候选的叙事方式。 |
| OiiOii · [Motion 动画 → 灵感](https://www.oiioii.tv/zh/) → 沃克斯风格纸贴解说 | 预览用纸面剪贴和高对比箭头显示太阳、树冠与路面之间的关系，把原因和结果放在同一画面。适合环境科普、机制对照或带实物图像的解释。 |
| OiiOii · [Motion 动画 → 灵感](https://www.oiioii.tv/zh/) | 看「蓝图编年史」「像素闯关讲解」「等轴微缩世界」等候选，按主题挑剖面讲解、步骤推进或空间关系的表现方法。只有栏目地址时附上案例名称和点入路径。 |

看得到起始简报时，对照成片记录「简报怎么写 → 成片怎么处理 → 这一镜怎么迁移」。有可见时间码时附上相关片段。只看到封面时，把画面判断限定在该静帧。对选中的案例，写成一条可执行的分镜动作，例如「订单卡固定在画面中央，匹配成功时连线才延伸到司机卡」。依照本片内容重新写文案、构图和素材清单。

## 风格规格

用够制作的细节记录选定方向，按需填写以下项目。

- 色板与色彩分工、中文字体与字号层级、布局、图形形状和质感。
- 可重复的 2–3 个动作规则，例如「卡片上移 32 px 并在 12 帧内减速停住」「过场由同一个圆形遮罩展开」。
- 信息密度、节拍、阅读停留、常用转场，以及字幕和声音的处理。
- 参考来源、拟用的素材或代码、需要标注的出处。视觉参考可转译成原创构图、文字和图形。实际复用时查看原项目许可证和素材条款。Lemo-Opuscar 对代码、文档、示片和第三方素材的规则不同，以仓库的 [LICENSE](https://github.com/lemomo-ai/lemo-opuscar/blob/main/LICENSE) 与该示片的 `CREDITS` 为准。
