---
title: 'InsightsToolUpdateRequest'
---

## Example Usage

```typescript
import { InsightsToolUpdateRequest } from "syllable-sdk/models/operations";

let value: InsightsToolUpdateRequest = {
  toolId: 548256,
  insightToolInput: {
    name: "<value>",
    description: "sorrowful furthermore lest besides sniveling close whoa",
    version: 259600,
    toolArguments: {},
    insightToolDefinitionId: 60078,
  },
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `toolId`                                                                   | *number*                                                                   | TRUE                                                         | N/A                                                                        |
| `insightToolInput`                                                         | [components.InsightToolInput](/sdk-docs/models/components/insighttoolinput) | TRUE                                                         | N/A                                                                        |