---
title: 'InsightWorkflowInput'
---

## Example Usage

```typescript
import { InsightWorkflowInput } from "syllable-sdk/models/components";

let value: InsightWorkflowInput = {
  name: "<value>",
  description:
    "instead gah vision um sneaky never hmph though unfortunately hmph",
  insightToolIds: [
    117315,
  ],
  conditions: {},
  status: "<value>",
};
```

## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                 | *string*                                                                                               | TRUE                                                                                     | Human readable name of Insight Workflow                                                                |
| `description`                                                                                          | *string*                                                                                               | TRUE                                                                                     | Text description of Insight Workflow                                                                   |
| `insightToolIds`                                                                                       | *number*[]                                                                                             | TRUE                                                                                     | List of Insight Tool IDs                                                                               |
| `conditions`                                                                                           | [components.InsightWorkflowInputConditions](/sdk-docs/models/components/insightworkflowinputconditions) | TRUE                                                                                     | Conditions for Insight Workflow                                                                        |
| `status`                                                                                               | *string*                                                                                               | TRUE                                                                                     | Status of the Insight Workflow                                                                         |