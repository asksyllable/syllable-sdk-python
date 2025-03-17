---
title: 'InsightsWorkflowUpdateRequest'
---

## Example Usage

```typescript
import { InsightsWorkflowUpdateRequest } from "syllable-sdk/models/operations";

let value: InsightsWorkflowUpdateRequest = {
  workflowId: 795457,
  insightWorkflowInput: {
    name: "<value>",
    description:
      "availability sorrowful towards yet dredger deadly siege regulate",
    insightToolIds: [
      767210,
    ],
    conditions: {},
    status: "<value>",
  },
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `workflowId`                                                                       | *number*                                                                           | TRUE                                                                 | N/A                                                                                |
| `insightWorkflowInput`                                                             | [components.InsightWorkflowInput](/sdk-docs/models/components/insightworkflowinput) | TRUE                                                                 | N/A                                                                                |