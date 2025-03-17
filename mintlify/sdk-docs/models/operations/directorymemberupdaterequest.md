---
title: 'DirectoryMemberUpdateRequest'
---

## Example Usage

```typescript
import { DirectoryMemberUpdateRequest } from "syllable-sdk/models/operations";

let value: DirectoryMemberUpdateRequest = {
  memberId: 770873,
  directoryMember: {
    name: "<value>",
    type: "<value>",
  },
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `memberId`                                                               | *number*                                                                 | TRUE                                                       | N/A                                                                      |
| `directoryMember`                                                        | [components.DirectoryMember](/sdk-docs/models/components/directorymember) | TRUE                                                       | N/A                                                                      |