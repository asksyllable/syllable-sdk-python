---
title: 'ToolUpdate'
---

## Example Usage

```typescript
import { ToolUpdate } from "syllable-sdk/models/components";

let value: ToolUpdate = {
  name: "<value>",
  definition: {
    tool: {
      function: {
        name: "<value>",
        description:
          "however ultimately boo ham gift harmful down cross-contamination before enrage",
        parameters: {},
      },
    },
  },
  serviceId: 715053,
  id: 418109,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | *string*                                                                     | TRUE                                                           | The name of the tool                                                         |
| `definition`                                                                 | [components.SDKToolDefinition](/sdk-docs/models/components/sdktooldefinition) | TRUE                                                           | N/A                                                                          |
| `serviceId`                                                                  | *number*                                                                     | TRUE                                                           | The service this tool belongs to                                             |
| `id`                                                                         | *number*                                                                     | TRUE                                                           | The ID of the tool                                                           |