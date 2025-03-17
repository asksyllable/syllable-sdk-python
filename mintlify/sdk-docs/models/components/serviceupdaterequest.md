---
title: 'ServiceUpdateRequest'
---

## Example Usage

```typescript
import { ServiceUpdateRequest } from "syllable-sdk/models/components";

let value: ServiceUpdateRequest = {
  name: "<value>",
  description: "as about quietly for graceful grouper at bah poorly",
  id: 435531,
};
```

## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `name`                         | *string*                       | TRUE             | The name of the service        |
| `description`                  | *string*                       | TRUE             | The description of the service |
| `id`                           | *number*                       | TRUE             | The ID of the service          |
| `lastUpdatedComments`          | *string*                       | FALSE             | Update comments                |