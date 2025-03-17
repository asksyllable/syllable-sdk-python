---
title: 'LanguageGroupResponse'
---

A language group is a collection of language, voice, and DTMF configuration that can be 
linked to an agent to define the languages and voices it supports. For more information, see 
[Console docs](https://docs.syllable.ai/Resources/LanguageGroups).

## Example Usage

```typescript
import { LanguageGroupResponse } from "syllable-sdk/models/components";

let value: LanguageGroupResponse = {
  name: "Call Center 1 Languages",
  description: "Languages spoken by operators at Call Center 1",
  languageConfigs: [
    {
      languageCode: "zh-CN",
      voiceProvider: "ElevenLabs",
      voiceDisplayName: "Will",
      dtmfCode: 1,
    },
  ],
  skipCurrentLanguageInMessage: false,
  id: 1,
  editComments: "Added Spanish support.",
  agentsInfo: [
    {
      id: 1,
      name: "Test Agent",
    },
  ],
  updatedAt: new Date("2023-04-22T20:11:12.127Z"),
  lastUpdatedBy: "user@mail.com",
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
| `agentsInfo`                                                                                                                      | [components.LanguageGroupAgentInfo](/sdk-docs/models/components/languagegroupagentinfo)[]                                          | FALSE                                                                                                                | IDs and names of the agents linked to the language group                                                                          |                                                                                                                                   |
| `updatedAt`                                                                                                                       | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                     | TRUE                                                                                                                | Timestamp of the last update to the language group.                                                                               |                                                                                                                                   |
| `lastUpdatedBy`                                                                                                                   | *string*                                                                                                                          | TRUE                                                                                                                | Email of the user who last updated the language group.                                                                            | user@mail.com                                                                                                                     |