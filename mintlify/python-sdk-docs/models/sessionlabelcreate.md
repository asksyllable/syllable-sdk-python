---
title: 'SessionLabelCreate'
---


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `session_id`                                                   | *int*                                                          | TRUE                                             | The internal ID of the session (see Session.session_id)        |                                                                |
| `type`                                                         | *str*                                                          | TRUE                                             | The type of the label                                          | auto-rating                                                    |
| `code`                                                         | *str*                                                          | TRUE                                             | A code describing the quality of the labeled session           | GOOD                                                           |
| `user_email`                                                   | *str*                                                          | TRUE                                             | The email of the user who created the label                    |                                                                |
| `comments`                                                     | *OptionalNullable[str]*                                        | FALSE                                             | Comment string describing additional details about the session |                                                                |
| `issue_categories`                                             | List[*str*]                                                    | FALSE                                             | Descriptions of issues occurring in the labeled call           | [<br/>"Silent treatment"<br/>]                                 |