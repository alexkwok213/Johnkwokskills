# Remotion 制作与交付

先阅读已有入口、包管理器锁文件、可用 Composition 和项目脚本。新工程用适合任务的官方 starter 或简单的 React/TypeScript 工程。优先核对项目已装版本的 [官方文档](https://www.remotion.dev/docs/) 和 [Agent Skills](https://www.remotion.dev/docs/ai/skills)，按用户的交付需求选择依赖。采用前核验 [Remotion 许可](https://www.remotion.dev/docs/license) 和第三方资源条款。

- 将分镜时间轴落到 Composition 的宽高、fps、总帧数和镜头段。通过 `Sequence` 或 `Series` 组织场景，显式算出转场重叠。把配音长度和目标片长分别记录。固定片长时，按真实配音的停顿排镜，可用结尾定格补足时长。用 `useCurrentFrame()` 驱动连续动画，用 `interpolate()` 或 `spring()` 控制动作，通过 `useVideoConfig()` 对应实际帧率。组件位于 `Sequence` 内时，`useCurrentFrame()` 以镜头起点为零。需要全局节拍时，显式传入全局帧或偏移。
- 根据需要定义可替换的文案、数据与品牌 props。使用可随工程交付的素材，采用项目的字体加载方式和 `staticFile()` 等本地素材入口。以当前帧确定渲染状态，给随机变化固定种子，避免依赖 CSS 实时时钟、浏览器定时器或加载先后。
- 用项目脚本或 [Remotion Studio](https://www.remotion.dev/docs/cli/studio) 看画面和时序，用 [still](https://www.remotion.dev/docs/cli/still) 导出首帧、信息最密帧和转场两侧，先做短样确认中文、版式和节奏，再 [render](https://www.remotion.dev/docs/cli/render) 全片。源码交付时包含可运行的工程、必要素材和明确的 Composition ID。直接交付视频时按约定输出，例如普通 MP4 或需要透明通道的合适编码。
- 示例命令以实际入口、ID 与输出路径替换。先确认项目本地有相应 CLI，沿用项目锁定的依赖。
  ```sh
  npx remotion studio src/index.ts
  npx remotion render src/index.ts Main out/preview.mp4 --frames=0-119
  npx remotion render src/index.ts Main out/final.mp4
  ```
- 导出后检查实际文件的分辨率、帧率、时长和音轨，必要时用 ffprobe。播放检查旁白、停顿、转场、音量及最后一帧。反馈里给出可以打开的产物路径，并说明完成到哪一步。
