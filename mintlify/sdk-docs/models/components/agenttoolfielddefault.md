---
title: 'AgentToolFieldDefault'
---

An agent-level configuration of default values for tool parameters for a given tool.

## Example Usage

```typescript
import { AgentToolFieldDefault } from "syllable-sdk/models/components";

let value: AgentToolFieldDefault = {
  fieldName: "<value>",
  defaultValue: "<value>",
};
```

## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `fieldName`                     | *string*                        | TRUE              | The name of the field           |
| `defaultValue`                  | *any*                           | TRUE              | The default value for the field |