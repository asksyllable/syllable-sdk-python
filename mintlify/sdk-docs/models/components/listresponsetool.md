---
title: 'ListResponseTool'
---

## Example Usage

```typescript
import { ListResponseTool } from "syllable-sdk/models/components";

let value: ListResponseTool = {
  items: [
    {
      name: "<value>",
      definition: {
        tool: {
          function: {
            name: "<value>",
            description:
              "gee fondly handful electronics mid athletic frequent and everlasting versus",
            parameters: {},
          },
        },
      },
      serviceId: 633998,
      id: 867290,
    },
  ],
  page: 940210,
  pageSize: 750765,
};
```

## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `items`                                              | [components.Tool](/sdk-docs/models/components/tool)[] | TRUE                                   | N/A                                                  |
| `page`                                               | *number*                                             | TRUE                                   | N/A                                                  |
| `pageSize`                                           | *number*                                             | TRUE                                   | N/A                                                  |
| `totalPages`                                         | *number*                                             | FALSE                                   | N/A                                                  |
| `totalCount`                                         | *number*                                             | FALSE                                   | N/A                                                  |