---
title: 'ListResponseInsightToolOutput'
---

## Example Usage

```typescript
import { ListResponseInsightToolOutput } from "syllable-sdk/models/components";

let value: ListResponseInsightToolOutput = {
  items: [
    {
      name: "<value>",
      description: "impish loyalty cake although misfire",
      version: 842777,
      toolArguments: {},
      insightToolDefinitionId: 373216,
      id: 222864,
      lastUpdatedBy: "<value>",
    },
  ],
  page: 80532,
  pageSize: 85311,
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `items`                                                                        | [components.InsightToolOutput](/sdk-docs/models/components/insighttooloutput)[] | TRUE                                                             | N/A                                                                            |
| `page`                                                                         | *number*                                                                       | TRUE                                                             | N/A                                                                            |
| `pageSize`                                                                     | *number*                                                                       | TRUE                                                             | N/A                                                                            |
| `totalPages`                                                                   | *number*                                                                       | FALSE                                                             | N/A                                                                            |
| `totalCount`                                                                   | *number*                                                                       | FALSE                                                             | N/A                                                                            |