---
title: 'SessionLabel'
---

A session label is associated with a given session and contains an evaluation of quality and
descriptions of issues the user encountered in that session or other details.

## Example Usage

```typescript
import { SessionLabel } from "syllable-sdk/models/components";

let value: SessionLabel = {
  sessionId: 798690,
  type: "human-rating",
  code: "OK",
  userEmail: "<value>",
  issueCategories: [
    "Silent treatment",
  ],
  id: 486272,
  timestamp: "<value>",
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
| `id`                                                           | *number*                                                       | TRUE                                             | The internal ID of the label                                   |                                                                |
| `timestamp`                                                    | *string*                                                       | TRUE                                             | The timestamp of the label creation                            |                                                                |