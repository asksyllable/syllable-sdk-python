---
title: 'PromptCreate'
---

## Example Usage

```typescript
import { PromptCreate } from "syllable-sdk/models/components";

let value: PromptCreate = {
  name: "<value>",
  type: "<value>",
  llmConfig: {
    model: "gpt-4o",
    version: "2024-05-13",
    apiVersion: "2024-06-01",
  },
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `name`                                                       | *string*                                                     | TRUE                                           | The Prompt name                                              |
| `description`                                                | *string*                                                     | FALSE                                           | The description of the prompt                                |
| `type`                                                       | *string*                                                     | TRUE                                           | The type of the prompt                                       |
| `context`                                                    | *string*                                                     | FALSE                                           | The prompt text                                              |
| `tools`                                                      | *string*[]                                                   | FALSE                                           | The tools for the prompt                                     |
| `llmConfig`                                                  | [components.LlmConfig](/sdk-docs/models/components/llmconfig) | TRUE                                           | N/A                                                          |