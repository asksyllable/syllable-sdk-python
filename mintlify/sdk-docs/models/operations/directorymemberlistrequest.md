---
title: 'DirectoryMemberListRequest'
---

## Example Usage

```typescript
import { DirectoryMemberListRequest } from "syllable-sdk/models/operations";

let value: DirectoryMemberListRequest = {};
```

## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `page`                                                                                         | *number*                                                                                       | FALSE                                                                             | N/A                                                                                            |
| `limit`                                                                                        | *number*                                                                                       | FALSE                                                                             | N/A                                                                                            |
| `searchFields`                                                                                 | [components.DirectoryMemberProperties](/sdk-docs/models/components/directorymemberproperties)[] | FALSE                                                                             | N/A                                                                                            |
| `searchFieldValues`                                                                            | *string*[]                                                                                     | FALSE                                                                             | N/A                                                                                            |
| `orderBy`                                                                                      | [components.DirectoryMemberProperties](/sdk-docs/models/components/directorymemberproperties)   | FALSE                                                                             | N/A                                                                                            |
| `orderByDirection`                                                                             | [components.OrderByDirection](/sdk-docs/models/components/orderbydirection)                     | FALSE                                                                             | N/A                                                                                            |
| `fields`                                                                                       | [components.DirectoryMemberProperties](/sdk-docs/models/components/directorymemberproperties)[] | FALSE                                                                             | N/A                                                                                            |
| `startDatetime`                                                                                | *string*                                                                                       | FALSE                                                                             | N/A                                                                                            |
| `endDatetime`                                                                                  | *string*                                                                                       | FALSE                                                                             | N/A                                                                                            |