---
title: 'SessionLabelCreate'
---

## Example Usage

```typescript
import { SessionLabelCreate } from "syllable-sdk/models/components";

let value: SessionLabelCreate = {
  sessionId: 588152,
  type: "human-rating",
  code: "BAD",
  userEmail: "<value>",
  issueCategories: [
    "Silent treatment",
  ],
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `sessionId`                                                    | *number*                                                       | TRUE                                             | The internal ID of the session (see Session.session_id)        |                                                                |
| `type`                                                         | *string*                                                       | TRUE                                             | The type of the label                                          | auto-rating                                                    |
| `code`                                                         | *string*                                                       | TRUE                                             | A code describing the quality of the labeled session           | GOOD                                                           |
| `userEmail`                                                    | *string*                                                       | TRUE                                             | The email of the user who created the label                    |                                                                |
| `comments`                                                     | *string*                                                       | FALSE                                             | Comment string describing additional details about the session |                                                                |
| `issueCategories`                                              | *string*[]                                                     | FALSE                                             | Descriptions of issues occurring in the labeled call           | [<br/>"Silent treatment"<br/>]                                 |