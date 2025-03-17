---
title: 'ListResponseEvent'
---

## Example Usage

```typescript
import { ListResponseEvent } from "syllable-sdk/models/components";

let value: ListResponseEvent = {
  items: [
    {
      timestamp: new Date("2023-01-15T12:10:56.303Z"),
      source: "tool-call",
      category: "automation",
      type: "phone-transfer",
      userId: "+18042221111",
      description: "Transfer to phone number +18042221111",
    },
  ],
  page: 347233,
  pageSize: 148141,
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `items`                                                | [components.Event](/sdk-docs/models/components/event)[] | TRUE                                     | N/A                                                    |
| `page`                                                 | *number*                                               | TRUE                                     | N/A                                                    |
| `pageSize`                                             | *number*                                               | TRUE                                     | N/A                                                    |
| `totalPages`                                           | *number*                                               | FALSE                                     | N/A                                                    |
| `totalCount`                                           | *number*                                               | FALSE                                     | N/A                                                    |