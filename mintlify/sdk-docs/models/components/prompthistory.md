---
title: 'PromptHistory'
---

Record of a change to a prompt. Values reflect post-change state.

## Example Usage

```typescript
import { PromptHistory } from "syllable-sdk/models/components";

let value: PromptHistory = {
  timestamp: new Date("2023-03-07T02:00:55.358Z"),
  promptId: "<id>",
  promptText: "<value>",
  promptName: "<value>",
  userEmail: "<value>",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `timestamp`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | TRUE                                                                            | Timestamp of the change                                                                       |
| `promptId`                                                                                    | *string*                                                                                      | TRUE                                                                            | ID of the prompt                                                                              |
| `promptText`                                                                                  | *string*                                                                                      | TRUE                                                                            | Text of the prompt                                                                            |
| `promptDescription`                                                                           | *string*                                                                                      | FALSE                                                                            | Description of the prompt                                                                     |
| `promptName`                                                                                  | *string*                                                                                      | TRUE                                                                            | Name of the prompt                                                                            |
| `llmConfig`                                                                                   | *string*                                                                                      | FALSE                                                                            | String representation of LLM config for the prompt                                            |
| `comments`                                                                                    | *string*                                                                                      | FALSE                                                                            | Comments describing the change                                                                |
| `userEmail`                                                                                   | *string*                                                                                      | TRUE                                                                            | Email address of the user who made the change                                                 |