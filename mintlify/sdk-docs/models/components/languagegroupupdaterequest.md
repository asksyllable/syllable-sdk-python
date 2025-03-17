---
title: 'LanguageGroupUpdateRequest'
---

## Example Usage

```typescript
import { LanguageGroupUpdateRequest } from "syllable-sdk/models/components";

let value: LanguageGroupUpdateRequest = {
  name: "Call Center 1 Languages",
  description: "Languages spoken by operators at Call Center 1",
  languageConfigs: [
    {
      languageCode: "zh-CN",
      voiceProvider: "ElevenLabs",
      voiceDisplayName: "Matilda",
      dtmfCode: 1,
    },
  ],
  skipCurrentLanguageInMessage: false,
  id: 1,
  editComments: "Added Spanish support.",
};
```

## Fields

| Field                                                                                                                             | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                            | *string*                                                                                                                          | TRUE                                                                                                                | The name of the language group.                                                                                                   | Call Center 1 Languages                                                                                                           |
| `description`                                                                                                                     | *string*                                                                                                                          | FALSE                                                                                                                | Description of the language group.                                                                                                | Languages spoken by operators at Call Center 1                                                                                    |
| `languageConfigs`                                                                                                                 | [components.LanguageConfig](/sdk-docs/models/components/languageconfig)[]                                                          | TRUE                                                                                                                | Voice and DTMF configurations for each language in the group.                                                                     |                                                                                                                                   |
| `skipCurrentLanguageInMessage`                                                                                                    | *boolean*                                                                                                                         | TRUE                                                                                                                | Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu. |                                                                                                                                   |
| `id`                                                                                                                              | *number*                                                                                                                          | TRUE                                                                                                                | The ID of the language group to update.                                                                                           | 1                                                                                                                                 |
| `editComments`                                                                                                                    | *string*                                                                                                                          | FALSE                                                                                                                | Comments for the most recent edit to the language group.                                                                          | Added Spanish support.                                                                                                            |