---
title: 'SessionData'
---


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `session_id`                                               | *int*                                                      | TRUE                                         | N/A                                                        |
| `source`                                                   | *str*                                                      | TRUE                                         | N/A                                                        |
| `target`                                                   | *str*                                                      | TRUE                                         | N/A                                                        |
| `is_test`                                                  | *bool*                                                     | TRUE                                         | N/A                                                        |
| `messages`                                                 | List[[models.SessionMessage](../models/sessionmessage.md)] | TRUE                                         | N/A                                                        |