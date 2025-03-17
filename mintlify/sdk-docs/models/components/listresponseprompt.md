---
title: 'ListResponsePrompt'
---

## Example Usage

```typescript
import { ListResponsePrompt } from "syllable-sdk/models/components";

let value: ListResponsePrompt = {
  items: [
    {
      name: "<value>",
      type: "<value>",
      llmConfig: {
        model: "gpt-4o",
        version: "2024-05-13",
        apiVersion: "2024-06-01",
      },
      id: 407183,
      lastUpdated: "<value>",
    },
  ],
  page: 69167,
  pageSize: 697429,
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `items`                                                  | [components.Prompt](/sdk-docs/models/components/prompt)[] | TRUE                                       | N/A                                                      |
| `page`                                                   | *number*                                                 | TRUE                                       | N/A                                                      |
| `pageSize`                                               | *number*                                                 | TRUE                                       | N/A                                                      |
| `totalPages`                                             | *number*                                                 | FALSE                                       | N/A                                                      |
| `totalCount`                                             | *number*                                                 | FALSE                                       | N/A                                                      |