---
title: 'ToolParameterDefault'
---

The default value for a parameter of a tool call.

## Example Usage

```typescript
import { ToolParameterDefault } from "syllable-sdk/models/components";

let value: ToolParameterDefault = {
  transform: {
    when: {
      key: "key",
      value: "value",
    },
  },
};
```

## Fields

| Field                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transform`                                                                                                                                                                                                                                  | [components.ToolParameterTransform](/sdk-docs/models/components/toolparametertransform)                                                                                                                                                       | TRUE                                                                                                                                                                                                                           | A transform to be applied to the value of a tool parameter.<br/><br/>Either `value` or `format` must be set:<br/>- `value` is any arbitrary value: string, list or dictionary.<br/>- `format` is a string composed of other parameters or context variables. |