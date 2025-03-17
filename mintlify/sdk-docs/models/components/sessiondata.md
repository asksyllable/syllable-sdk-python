---
title: 'SessionData'
---

## Example Usage

```typescript
import { SessionData } from "syllable-sdk/models/components";

let value: SessionData = {
  sessionId: 653000,
  source: "<value>",
  target: "<value>",
  isTest: false,
  messages: [
    {
      role: "agent",
      dialog: {
        text: "<value>",
      },
      toolCalls: [
        {
          tollCallId: "<id>",
          toolName: "<value>",
          toolArguments: {},
          timestamp: new Date("2024-08-24T12:55:52.067Z"),
        },
      ],
      timestamp: new Date("2025-06-12T11:40:46.096Z"),
    },
  ],
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `sessionId`                                                              | *number*                                                                 | TRUE                                                       | N/A                                                                      |
| `source`                                                                 | *string*                                                                 | TRUE                                                       | N/A                                                                      |
| `target`                                                                 | *string*                                                                 | TRUE                                                       | N/A                                                                      |
| `isTest`                                                                 | *boolean*                                                                | TRUE                                                       | N/A                                                                      |
| `messages`                                                               | [components.SessionMessage](/sdk-docs/models/components/sessionmessage)[] | TRUE                                                       | N/A                                                                      |