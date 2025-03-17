---
title: 'CustomMessageCreateRequest'
---


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *str*                                                            | TRUE                                               | The name of the custom message                                   |
| `text`                                                           | *str*                                                            | TRUE                                               | The text of the custom message                                   |
| `label`                                                          | *OptionalNullable[str]*                                          | FALSE                                               | The label of the custom message                                  |
| `rules`                                                          | List[[models.CustomMessageRule](../models/custommessagerule.md)] | FALSE                                               | Rules for time-specific message variants                         |
| `type`                                                           | *Optional[str]*                                                  | FALSE                                               | N/A                                                              |