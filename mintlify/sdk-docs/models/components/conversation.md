---
title: 'Conversation'
---

A conversation is a record of messages between a user and an agent, and is composed of one or
more sessions.

## Example Usage

```typescript
import { Conversation } from "syllable-sdk/models/components";

let value: Conversation = {
  timestamp: new Date("2025-11-06T10:52:56.298Z"),
  conversationId: "<id>",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `timestamp`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | TRUE                                                                            | Timestamp of the conversation                                                                 |
| `conversationId`                                                                              | *string*                                                                                      | TRUE                                                                            | ID of the conversation                                                                        |
| `agentId`                                                                                     | *string*                                                                                      | FALSE                                                                            | ID of the agent with which the conversation occurred                                          |
| `agentName`                                                                                   | *string*                                                                                      | FALSE                                                                            | Name of the agent with which the conversation occurred                                        |
| `agentType`                                                                                   | *string*                                                                                      | FALSE                                                                            | Value of the "type" field of the agent with which the conversation occurred                   |
| `promptId`                                                                                    | *string*                                                                                      | FALSE                                                                            | ID of the prompt used in the conversation                                                     |
| `promptName`                                                                                  | *string*                                                                                      | FALSE                                                                            | Name of the prompt used in the conversation                                                   |
| `promptVersion`                                                                               | *string*                                                                                      | FALSE                                                                            | Version of the prompt used in the conversation                                                |
| `llmProvider`                                                                                 | *string*                                                                                      | FALSE                                                                            | Provider for the LLM used in the conversation (see PromptResponse.llm_config.provider)        |
| `llmModel`                                                                                    | *string*                                                                                      | FALSE                                                                            | Model for the LLM used in the conversation (see PromptResponse.llm_config.model)              |
| `llmVersion`                                                                                  | *string*                                                                                      | FALSE                                                                            | Version for the LLM used in the conversation (see PromptResponse.llm_config.version)          |
| `isLegacy`                                                                                    | *boolean*                                                                                     | FALSE                                                                            | Whether the conversation occurred on the legacy Syllable system                               |