---
title: 'ChannelTarget'
---

Class for all Channel Target responses

## Example Usage

```typescript
import { ChannelTarget } from "syllable-sdk/models/components";

let value: ChannelTarget = {
  id: 468651,
  channelId: 976762,
  channelName: "<value>",
  agentId: 604846,
  agent: {
    name: "<value>",
    type: "<value>",
    promptId: 739264,
    timezone: "Africa/Dakar",
    id: 282807,
    updatedAt: new Date("2022-05-12T17:39:01.246Z"),
    lastUpdatedBy: "<value>",
  },
  target: "<value>",
  targetMode: "<value>",
  updatedAt: new Date("2022-11-21T13:40:18.320Z"),
  lastUpdatedBy: "<value>",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *number*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `channelId`                                                                                   | *number*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `channelName`                                                                                 | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `agentId`                                                                                     | *number*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `agent`                                                                                       | [components.DaoChannelTargetAgent](/sdk-docs/models/components/daochanneltargetagent)          | TRUE                                                                            | N/A                                                                                           |
| `target`                                                                                      | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `targetMode`                                                                                  | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `fallbackTarget`                                                                              | *string*                                                                                      | FALSE                                                                            | N/A                                                                                           |
| `isTest`                                                                                      | *boolean*                                                                                     | FALSE                                                                            | N/A                                                                                           |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | TRUE                                                                            | N/A                                                                                           |
| `lastUpdatedBy`                                                                               | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |