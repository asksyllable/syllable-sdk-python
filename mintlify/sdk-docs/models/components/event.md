---
title: 'Event'
---

An event represents a specific occurrence during a session.

## Example Usage

```typescript
import { Event } from "syllable-sdk/models/components";

let value: Event = {
  timestamp: new Date("2025-12-12T02:02:24.972Z"),
  source: "tool-call",
  category: "automation",
  type: "phone-transfer",
  userId: "+18042221111",
  description: "Transfer to phone number +18042221111",
};
```

## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `timestamp`                                                                                         | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)       | TRUE                                                                                  | Timestamp at which the event occurred                                                               |                                                                                                     |
| `sessionId`                                                                                         | *string*                                                                                            | FALSE                                                                                  | ID of the session in which the event occurred                                                       |                                                                                                     |
| `conversationId`                                                                                    | *string*                                                                                            | FALSE                                                                                  | ID of the conversation associated with the session in which the event occurred                      |                                                                                                     |
| `source`                                                                                            | *string*                                                                                            | FALSE                                                                                  | Source of the event (either a tool call or an LLM prompt)                                           | tool-call                                                                                           |
| `sourceId`                                                                                          | *string*                                                                                            | FALSE                                                                                  | ID of the source of the event (either a tool ID or a prompt ID)                                     |                                                                                                     |
| `category`                                                                                          | *string*                                                                                            | FALSE                                                                                  | Broad categorization of the event                                                                   | automation                                                                                          |
| `type`                                                                                              | *string*                                                                                            | FALSE                                                                                  | More specific class of the event                                                                    | phone-transfer                                                                                      |
| `userId`                                                                                            | *string*                                                                                            | FALSE                                                                                  | ID of the user interacting with the system when the event occurred (e.g., their       phone number) | +18042221111                                                                                        |
| `description`                                                                                       | *string*                                                                                            | FALSE                                                                                  | Human-readable description of the event                                                             | Transfer to phone number +18042221111                                                               |
| `attributes`                                                                                        | [components.Attributes](/sdk-docs/models/components/attributes)                                      | FALSE                                                                                  | Arbitrary additional metadata for the event                                                         |                                                                                                     |