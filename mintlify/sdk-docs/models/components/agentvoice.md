---
title: 'AgentVoice'
---

Voice option for an agent.

## Example Usage

```typescript
import { AgentVoice } from "syllable-sdk/models/components";

let value: AgentVoice = {
  provider: "OpenAI",
  displayName: "Lily",
  varName: "wavenet:female/cmn-TW-Wavenet-A",
  gender: "female",
  supportedLanguages: [
    {
      name: "English",
      code: "zh-CN",
    },
  ],
  deprecated: false,
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `provider`                                                                           | [components.TtsProvider](/sdk-docs/models/components/ttsprovider)                     | TRUE                                                                   | TTS provider for an agent voice.                                                     |
| `displayName`                                                                        | [components.AgentVoiceDisplayName](/sdk-docs/models/components/agentvoicedisplayname) | TRUE                                                                   | Display names of voices that Syllable supports.                                      |
| `varName`                                                                            | [components.AgentVoiceVarName](/sdk-docs/models/components/agentvoicevarname)         | TRUE                                                                   | The variable name of an agent voice (used when procesing messages).                  |
| `gender`                                                                             | [components.AgentVoiceGender](/sdk-docs/models/components/agentvoicegender)           | TRUE                                                                   | Gender for an agent voice.                                                           |
| `model`                                                                              | [components.AgentVoiceModel](/sdk-docs/models/components/agentvoicemodel)             | FALSE                                                                   | Model for an agent voice.                                                            |
| `supportedLanguages`                                                                 | [components.AgentLanguage](/sdk-docs/models/components/agentlanguage)[]               | TRUE                                                                   | Languages supported by the voice                                                     |
| `deprecated`                                                                         | *boolean*                                                                            | TRUE                                                                   | Whether the voice is deprecated and should not be used                               |