---
title: 'Target'
---

## Example Usage

```typescript
import { Target } from "syllable-sdk/models/components";

let value: Target = {
  agentId: 87129,
  target: "<value>",
  targetMode: "voice",
  channelId: 832620,
  id: 778157,
};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `agentId`                                                        | *number*                                                         | TRUE                                               | The Agent ID                                                     |
| `target`                                                         | *string*                                                         | TRUE                                               | The Target                                                       |
| `targetMode`                                                     | [components.TargetModes](/sdk-docs/models/components/targetmodes) | TRUE                                               | N/A                                                              |
| `channelId`                                                      | *number*                                                         | TRUE                                               | The Channel ID                                                   |
| `fallbackTarget`                                                 | *string*                                                         | FALSE                                               | The Fallback Target                                              |
| `isTest`                                                         | *boolean*                                                        | FALSE                                               | Whether the Target is for testing                                |
| `id`                                                             | *number*                                                         | TRUE                                               | The Target ID                                                    |
| `channelName`                                                    | *string*                                                         | FALSE                                               | The Channel Name                                                 |