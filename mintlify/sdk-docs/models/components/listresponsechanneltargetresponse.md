---
title: 'ListResponseChannelTargetResponse'
---

## Example Usage

```typescript
import { ListResponseChannelTargetResponse } from "syllable-sdk/models/components";

let value: ListResponseChannelTargetResponse = {
  items: [],
  page: 16429,
  pageSize: 929530,
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `items`                                                                                | [components.ChannelTargetResponse](/sdk-docs/models/components/channeltargetresponse)[] | TRUE                                                                     | N/A                                                                                    |
| `page`                                                                                 | *number*                                                                               | TRUE                                                                     | N/A                                                                                    |
| `pageSize`                                                                             | *number*                                                                               | TRUE                                                                     | N/A                                                                                    |
| `totalPages`                                                                           | *number*                                                                               | FALSE                                                                     | N/A                                                                                    |
| `totalCount`                                                                           | *number*                                                                               | FALSE                                                                     | N/A                                                                                    |