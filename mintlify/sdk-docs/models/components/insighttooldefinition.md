---
title: 'InsightToolDefinition'
---

## Example Usage

```typescript
import { InsightToolDefinition } from "syllable-sdk/models/components";

let value: InsightToolDefinition = {
  id: 618826,
  name: "<value>",
  type: "<value>",
  description: "svelte ah hunt until",
  toolParameters: {},
  toolResultSet: {},
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *number*                                                               | TRUE                                                     | Unique ID for Insight Tool Definition                                  |
| `name`                                                                 | *string*                                                               | TRUE                                                     | Human readable name of Insight Tool Definition                         |
| `type`                                                                 | *string*                                                               | TRUE                                                     | Type of Insight Tool Definition                                        |
| `description`                                                          | *string*                                                               | TRUE                                                     | Text description of Insight Tool Definition                            |
| `toolParameters`                                                       | [components.ToolParameters](/sdk-docs/models/components/toolparameters) | TRUE                                                     | Parameters for Insight Tool Definition                                 |
| `toolResultSet`                                                        | [components.ToolResultSet](/sdk-docs/models/components/toolresultset)   | TRUE                                                     | Result key/types for Insight Tool Definition                           |