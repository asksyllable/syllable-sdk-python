---
title: 'Service'
---

A service is a collection of tools.

## Example Usage

```typescript
import { Service } from "syllable-sdk/models/components";

let value: Service = {
  name: "<value>",
  description: "psst till with",
  id: 904949,
  tools: [
    "<value>",
  ],
};
```

## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `name`                                        | *string*                                      | TRUE                            | The name of the service                       |
| `description`                                 | *string*                                      | TRUE                            | The description of the service                |
| `id`                                          | *number*                                      | TRUE                            | The ID of the service                         |
| `tools`                                       | *string*[]                                    | TRUE                            | Names of the tools that belong to the service |