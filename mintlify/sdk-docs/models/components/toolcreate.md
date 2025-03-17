---
title: 'ToolCreate'
---

## Example Usage

```typescript
import { ToolCreate } from "syllable-sdk/models/components";

let value: ToolCreate = {
  name: "<value>",
  definition: {
    tool: {
      function: {
        name: "<value>",
        description: "huge whoa because er factorise yearly",
        parameters: {},
      },
    },
  },
  serviceId: 376741,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | *string*                                                                     | TRUE                                                           | The name of the tool                                                         |
| `definition`                                                                 | [components.SDKToolDefinition](/sdk-docs/models/components/sdktooldefinition) | TRUE                                                           | N/A                                                                          |
| `serviceId`                                                                  | *number*                                                                     | TRUE                                                           | The service this tool belongs to                                             |