---
title: 'AgentLanguage'
---

Language option for an agent.

## Example Usage

```typescript
import { AgentLanguage } from "syllable-sdk/models/components";

let value: AgentLanguage = {
  name: "English",
  code: "yue-HK",
};
```

## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `name`                                                             | *string*                                                           | TRUE                                                 | Name of the language                                               | English                                                            |
| `code`                                                             | [components.LanguageCode](/sdk-docs/models/components/languagecode) | TRUE                                                 | BCP 47 codes of languages that Syllable supports.                  |                                                                    |