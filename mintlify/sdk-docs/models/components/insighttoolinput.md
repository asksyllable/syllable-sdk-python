---
title: 'InsightToolInput'
---

## Example Usage

```typescript
import { InsightToolInput } from "syllable-sdk/models/components";

let value: InsightToolInput = {
  name: "<value>",
  description: "whenever whenever pomelo",
  version: 987349,
  toolArguments: {},
  insightToolDefinitionId: 759283,
};
```

## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `name`                                                                                               | *string*                                                                                             | TRUE                                                                                   | Human readable name of Insight Tool                                                                  |
| `description`                                                                                        | *string*                                                                                             | TRUE                                                                                   | Text description of Insight Tool                                                                     |
| `version`                                                                                            | *number*                                                                                             | TRUE                                                                                   | Version number of Insight Tool                                                                       |
| `toolArguments`                                                                                      | [components.InsightToolInputToolArguments](/sdk-docs/models/components/insighttoolinputtoolarguments) | TRUE                                                                                   | Arguments for Insight Tool                                                                           |
| `insightToolDefinitionId`                                                                            | *number*                                                                                             | TRUE                                                                                   | Unique ID for Insight Tool Definition                                                                |