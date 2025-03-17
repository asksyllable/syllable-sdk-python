---
title: 'ChannelTargetUpdateRequest'
---

## Example Usage

```typescript
import { ChannelTargetUpdateRequest } from "syllable-sdk/models/components";

let value: ChannelTargetUpdateRequest = {
  agentId: 63955,
  channelId: 485628,
  target: "<value>",
  targetMode: "email",
  id: 876506,
};
```

## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `agentId`                                                                                                                      | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the agent associated with the channel target                                                                         |
| `channelId`                                                                                                                    | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the channel associated with the channel target                                                                       |
| `target`                                                                                                                       | *string*                                                                                                                       | TRUE                                                                                                             | The name of the channel target (must correspond to an organization-level target)                                               |
| `targetMode`                                                                                                                   | [components.TargetModes](/sdk-docs/models/components/targetmodes)                                                               | TRUE                                                                                                             | Available modes (communication methods) for channel targets.                                                                   |
| `fallbackTarget`                                                                                                               | *string*                                                                                                                       | FALSE                                                                                                             | The fallback for the channel target (currently only supported for "voice" mode)                                                |
| `isTest`                                                                                                                       | *boolean*                                                                                                                      | FALSE                                                                                                             | Whether the channel target is intended for testing. If true, any sessions created through this target will be labeled as test. |
| `id`                                                                                                                           | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the channel target                                                                                                   |