---
title: 'LanguageGroupCreateRequest'
---

## Example Usage

```typescript
import { LanguageGroupCreateRequest } from "syllable-sdk/models/components";

let value: LanguageGroupCreateRequest = {
  name: "Call Center 1 Languages",
  description: "Languages spoken by operators at Call Center 1",
  languageConfigs: [
    {
      languageCode: "th-TH",
      voiceProvider: "OpenAI",
      voiceDisplayName: "River",
      dtmfCode: 1,
    },
  ],
  skipCurrentLanguageInMessage: false,
};
```

## Fields

| Field                                                                                                                             | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                            | *string*                                                                                                                          | TRUE                                                                                                                | The name of the language group.                                                                                                   | Call Center 1 Languages                                                                                                           |
| `description`                                                                                                                     | *string*                                                                                                                          | FALSE                                                                                                                | Description of the language group.                                                                                                | Languages spoken by operators at Call Center 1                                                                                    |
| `languageConfigs`                                                                                                                 | [components.LanguageConfig](/sdk-docs/models/components/languageconfig)[]                                                          | TRUE                                                                                                                | Voice and DTMF configurations for each language in the group.                                                                     |                                                                                                                                   |
| `skipCurrentLanguageInMessage`                                                                                                    | *boolean*                                                                                                                         | TRUE                                                                                                                | Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu. |                                                                                                                                   |