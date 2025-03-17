---
title: 'ListResponseInsightWorkflowOutput'
---

## Example Usage

```typescript
import { ListResponseInsightWorkflowOutput } from "syllable-sdk/models/components";

let value: ListResponseInsightWorkflowOutput = {
  items: [
    {
      name: "<value>",
      description: "astride fidget abaft knottily ethyl covenant",
      insightToolIds: [
        788546,
      ],
      conditions: {},
      status: "<value>",
      id: 56848,
      insightTools: [
        {
          name: "<value>",
          description: "indeed beside motivate zowie tag even well lest",
          version: 62713,
          toolArguments: {},
          insightToolDefinitionId: 424032,
          id: 258684,
          lastUpdatedBy: "<value>",
        },
      ],
      lastUpdatedBy: "<value>",
    },
  ],
  page: 849039,
  pageSize: 33304,
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `items`                                                                                | [components.InsightWorkflowOutput](/sdk-docs/models/components/insightworkflowoutput)[] | TRUE                                                                     | N/A                                                                                    |
| `page`                                                                                 | *number*                                                                               | TRUE                                                                     | N/A                                                                                    |
| `pageSize`                                                                             | *number*                                                                               | TRUE                                                                     | N/A                                                                                    |
| `totalPages`                                                                           | *number*                                                                               | FALSE                                                                     | N/A                                                                                    |
| `totalCount`                                                                           | *number*                                                                               | FALSE                                                                     | N/A                                                                                    |