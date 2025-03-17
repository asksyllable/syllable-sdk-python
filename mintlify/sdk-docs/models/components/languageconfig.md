---
title: 'LanguageConfig'
---

Voice and DTMF configurations for a language in a language group. List of available voices
and their supported languages can be fetched from `GET /agents/voices/available/`.

## Example Usage

```typescript
import { LanguageConfig } from "syllable-sdk/models/components";

let value: LanguageConfig = {
  languageCode: "en-US",
  voiceProvider: "OpenAI",
  voiceDisplayName: "Mark",
  dtmfCode: 1,
};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `languageCode`                                                                               | [components.LanguageCode](/sdk-docs/models/components/languagecode)                           | TRUE                                                                           | BCP 47 codes of languages that Syllable supports.                                            |                                                                                              |
| `voiceProvider`                                                                              | [components.TtsProvider](/sdk-docs/models/components/ttsprovider)                             | TRUE                                                                           | TTS provider for an agent voice.                                                             |                                                                                              |
| `voiceDisplayName`                                                                           | [components.AgentVoiceDisplayName](/sdk-docs/models/components/agentvoicedisplayname)         | TRUE                                                                           | Display names of voices that Syllable supports.                                              |                                                                                              |
| `dtmfCode`                                                                                   | *number*                                                                                     | TRUE                                                                           | DTMF code that should be used for the language in the menu generated from the language group | 1                                                                                            |