---
title: 'ListResponseSession'
---

## Example Usage

```typescript
import { ListResponseSession } from "syllable-sdk/models/components";

let value: ListResponseSession = {
  items: [
    {
      timestamp: new Date("2024-02-07T18:04:15.155Z"),
      channelManagerService: "console",
      channelManagerType: "voice_twilio_v1",
      source: "user@email.com",
    },
  ],
  page: 866861,
  pageSize: 816151,
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `items`                                                    | [components.Session](/sdk-docs/models/components/session)[] | TRUE                                         | N/A                                                        |
| `page`                                                     | *number*                                                   | TRUE                                         | N/A                                                        |
| `pageSize`                                                 | *number*                                                   | TRUE                                         | N/A                                                        |
| `totalPages`                                               | *number*                                                   | FALSE                                         | N/A                                                        |
| `totalCount`                                               | *number*                                                   | FALSE                                         | N/A                                                        |