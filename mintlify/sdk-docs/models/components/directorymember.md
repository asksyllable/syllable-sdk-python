---
title: 'DirectoryMember'
---

## Example Usage

```typescript
import { DirectoryMember } from "syllable-sdk/models/components";

let value: DirectoryMember = {
  name: "<value>",
  type: "<value>",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `name`                                                                                        | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `type`                                                                                        | *string*                                                                                      | TRUE                                                                            | N/A                                                                                           |
| `extensions`                                                                                  | [components.DirectoryExtension](/sdk-docs/models/components/directoryextension)[]              | FALSE                                                                            | N/A                                                                                           |
| `contactTags`                                                                                 | [components.ContactTags](/sdk-docs/models/components/contacttags)                              | FALSE                                                                            | N/A                                                                                           |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | FALSE                                                                            | N/A                                                                                           |
| `lastUpdatedBy`                                                                               | *string*                                                                                      | FALSE                                                                            | N/A                                                                                           |
| `id`                                                                                          | *number*                                                                                      | FALSE                                                                            | N/A                                                                                           |