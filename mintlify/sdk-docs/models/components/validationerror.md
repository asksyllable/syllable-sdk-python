---
title: 'ValidationError'
---

## Example Usage

```typescript
import { ValidationError } from "syllable-sdk/models/components";

let value: ValidationError = {
  loc: [
    "<value>",
  ],
  msg: "<value>",
  type: "<value>",
};
```

## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `loc`              | *components.Loc*[] | TRUE | N/A                |
| `msg`              | *string*           | TRUE | N/A                |
| `type`             | *string*           | TRUE | N/A                |