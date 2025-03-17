---
title: 'ListResponseServiceResponse'
---

## Example Usage

```typescript
import { ListResponseServiceResponse } from "syllable-sdk/models/components";

let value: ListResponseServiceResponse = {
  items: [
    {
      name: "<value>",
      description:
        "and ouch supportive honestly uh-huh mmm gently electric mmm zen",
      id: 197259,
      lastUpdated: new Date("2024-08-09T06:13:30.901Z"),
      lastUpdatedBy: "<value>",
      tools: [
        "<value>",
      ],
    },
  ],
  page: 290248,
  pageSize: 304173,
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `items`                                                                    | [components.ServiceResponse](/sdk-docs/models/components/serviceresponse)[] | TRUE                                                         | N/A                                                                        |
| `page`                                                                     | *number*                                                                   | TRUE                                                         | N/A                                                                        |
| `pageSize`                                                                 | *number*                                                                   | TRUE                                                         | N/A                                                                        |
| `totalPages`                                                               | *number*                                                                   | FALSE                                                         | N/A                                                                        |
| `totalCount`                                                               | *number*                                                                   | FALSE                                                         | N/A                                                                        |