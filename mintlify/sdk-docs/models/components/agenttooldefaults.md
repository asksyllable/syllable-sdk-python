---
title: 'AgentToolDefaults'
---

An agent-level configuration of default values for tool parameters for its tools.

## Example Usage

```typescript
import { AgentToolDefaults } from "syllable-sdk/models/components";

let value: AgentToolDefaults = {
  toolName: "<value>",
  defaultValues: [
    {
      fieldName: "<value>",
      defaultValue: "<value>",
    },
  ],
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `toolName`                                                                             | *string*                                                                               | TRUE                                                                     | The name of the tool                                                                   |
| `defaultValues`                                                                        | [components.AgentToolFieldDefault](/sdk-docs/models/components/agenttoolfielddefault)[] | TRUE                                                                     | The default values for fields used in the tool                                         |