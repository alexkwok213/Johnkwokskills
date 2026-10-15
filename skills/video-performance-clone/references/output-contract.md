# 输出与存档

工作输出 `report.md`、`prompt.txt`、`prompt.md`、`sample.json`、`evidence/`。`prompt.txt` 只含可直接粘贴进目标模型的生成正文，与对话里的完整代码块一致；`prompt.md` 可另含使用方法，不能要求用户拼接多个部分才得到一条可用提示词。证据目录含 manifest、元信息、总览/局部图、音轨及有条件时的 ASR 原结果。

报告包含：元信息与实际用到的能力；角色/空间锚点；镜头表；逐台词表演表；声音已核验与未核验项；写实效果；用户意图与成片偏差；可迁移规则；提示词；未确认项。

报告与证据使用源时间戳，生成正文默认使用阶段/镜头顺序。`prompt.md` 在代码块外写清本次模型、首帧或全能参考方式、真实素材的职责及生成时长设置。仅首帧不虚构其他参考；全能参考不承诺文字指定的开场图等同于严格首帧参数锁定。用户要求模型对比时，各套输出独立完整，不要求拼接。

表演表：时间范围、镜头、角色、原台词/触发词、动作、神情/视线、声音、对方反应、证据及置信度。没有证据填未核验，不填正常。

`sample.json` 至少含：

```json
{
  "id": "源SHA256前12位",
  "title": "参考片短名",
  "tags": ["写实", "对话", "争吵"],
  "source": {"original_path": "/绝对路径.mp4", "sha256": "完整哈希"},
  "analysis_basis": {"visual": "连续帧", "audio": "ASR候选，未听辨"},
  "generation_target": {
    "model": "Seedance 2.5",
    "input_mode": "first_frame",
    "sequence_style": "ordered_phases",
    "confirmed_by": "本次用户明确选择",
    "references": [{"file": "本次真实首帧文件", "label": "图片1", "roles": ["opening", "identity", "scene"]}]
  },
  "characters": [],
  "shots": [{"id": "S1", "start": 0, "end": 2.1, "description": "观察"}],
  "events": [{
    "start": 0, "end": 1.5, "shot": "S1", "character": "女方",
    "dialogue": {"text": "候选原话", "source": "ASR", "verified": false},
    "action": "可见动作", "face_gaze": "可见神情和视线",
    "voice": {"description": "未听辨", "verified": false},
    "evidence": ["evidence/frame-000001.jpg"],
    "confidence": "中，前景遮挡"
  }],
  "transfer_rules": [{"rule": "可迁移规律", "evidence_events": [0]}],
  "user_intent": {"text": "用户原文", "differences": []},
  "unknowns": ["精确音色待听辨"],
  "files": {"report": "report.md", "prompt": "prompt.md", "manifest": "evidence/manifest.json"}
}
```

持久样本索引 `assets/library/index.json` 是数组，每项 `id/title/tags/summary/path`；path 相对 library。同源哈希避免重复存档。调用样本时读实际报告和相关证据，不能仅凭索引摘要写精确模仿。

保存前检查 JSON 可解析、源哈希一致、所有证据存在、事件有序且在时长内；结构检查不能代替内容核对。
