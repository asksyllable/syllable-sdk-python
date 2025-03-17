---
title: 'SessionMessage'
---

## Example Usage

```typescript
import { SessionMessage } from "syllable-sdk/models/components";

let value: SessionMessage = {
  role: "agent",
  dialog: {
    text: "<value>",
  },
  toolCalls: [
    {
      tollCallId: "<id>",
      toolName: "<value>",
      toolArguments: {},
      timestamp: new Date("2025-05-27T23:28:25.141Z"),
    },
  ],
  timestamp: new Date("2023-02-15T03:11:35.631Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `role`                                                                                        | [components.DialogRole](/sdk-docs/models/components/dialogrole)                                | TRUE                                                                            | N/A                                                                                           |
| `dialog`                                                                                      | [components.DialogMessage](/sdk-docs/models/components/dialogmessage)                          | TRUE                                                                            | N/A                                                                                           |
| `toolCalls`                                                                                   | [components.DialogToolCall](/sdk-docs/models/components/dialogtoolcall)[]                      | TRUE                                                                            | N/A                                                                                           |
| `timestamp`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | TRUE                                                                            | N/A                                                                                           |