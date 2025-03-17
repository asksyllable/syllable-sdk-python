---
title: 'TestMessageResponse'
---

Response from an agent in a test chat.

## Example Usage

```typescript
import { TestMessageResponse } from "syllable-sdk/models/components";

let value: TestMessageResponse = {
  testId: "<id>",
  agentId: "<id>",
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `testId`                                                                 | *string*                                                                 | TRUE                                                       | Channel-manager-side ID of the session (see Session.channel_manager_sid) |
| `agentId`                                                                | *string*                                                                 | TRUE                                                       | ID of the agent with which the chat is taking place                      |
| `text`                                                                   | *string*                                                                 | FALSE                                                       | The text of the message that elicited the response                       |
| `response`                                                               | [components.Response](/sdk-docs/models/components/response)               | FALSE                                                       | N/A                                                                      |
| `responseText`                                                           | *string*                                                                 | FALSE                                                       | The text of the response                                                 |