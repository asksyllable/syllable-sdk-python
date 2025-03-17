---
title: 'PromptUpdate'
---

## Example Usage

```typescript
import { PromptUpdate } from "syllable-sdk/models/components";

let value: PromptUpdate = {
  name: "<value>",
  type: "<value>",
  llmConfig: {
    model: "gpt-4o",
    version: "2024-05-13",
    apiVersion: "2024-06-01",
  },
  id: 722056,
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
| `id`                                                         | *number*                                                     | TRUE                                           | The Prompt ID                                                |
| `editComments`                                               | *string*                                                     | FALSE                                           | The comments for the last edit                               |