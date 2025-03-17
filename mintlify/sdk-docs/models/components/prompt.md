---
title: 'Prompt'
---

## Example Usage

```typescript
import { Prompt } from "syllable-sdk/models/components";

let value: Prompt = {
  name: "<value>",
  type: "<value>",
  llmConfig: {
    model: "gpt-4o",
    version: "2024-05-13",
    apiVersion: "2024-06-01",
  },
  id: 925597,
  lastUpdated: "<value>",
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
| `lastUpdated`                                                | *string*                                                     | TRUE                                           | The last updated date of the prompt                          |
| `lastUpdatedBy`                                              | *string*                                                     | FALSE                                           | The last updated user who last updated of the prompt         |
| `agentCount`                                                 | *number*                                                     | FALSE                                           | The number of agents using the prompt                        |