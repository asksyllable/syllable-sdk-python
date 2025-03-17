---
title: 'Defaults'
---

The default values for the parameters of the function/tool call.


## Supported Types

### `any`

```typescript
const value: any = "<value>";
```

### `{ [k: string]: components.ToolParameterDefault }`

```typescript
const value: { [k: string]: components.ToolParameterDefault } = {
  "key": {
    transform: {
      when: {
        key: "key",
        value: "value",
      },
    },
  },
};
```

