---
title: 'Tool'
---

## Example Usage

```typescript
import { Tool } from "syllable-sdk/models/components";

let value: Tool = {
  name: "<value>",
  definition: {
    tool: {
      function: {
        name: "<value>",
        description:
          "knavishly egg keenly grave incidentally righteously gastropod ponder",
        parameters: {},
      },
    },
  },
  serviceId: 279068,
  id: 209750,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | *string*                                                                     | TRUE                                                           | The name of the tool                                                         |
| `definition`                                                                 | [components.SDKToolDefinition](/sdk-docs/models/components/sdktooldefinition) | TRUE                                                           | N/A                                                                          |
| `serviceId`                                                                  | *number*                                                                     | TRUE                                                           | The service this tool belongs to                                             |
| `id`                                                                         | *number*                                                                     | TRUE                                                           | The ID of the tool                                                           |
| `serviceName`                                                                | *string*                                                                     | FALSE                                                           | The name of the service this tool belongs to                                 |