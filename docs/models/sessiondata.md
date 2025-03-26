# SessionData


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `session_id`                                               | *int*                                                      | :heavy_check_mark:                                         | Session ID                                                 | 123                                                        |
| `source`                                                   | *str*                                                      | :heavy_check_mark:                                         | Session source                                             | +1234567890                                                |
| `target`                                                   | *str*                                                      | :heavy_check_mark:                                         | Session target                                             | +1239876543                                                |
| `is_test`                                                  | *bool*                                                     | :heavy_check_mark:                                         | Is test session                                            | false                                                      |
| `messages`                                                 | List[[models.SessionMessage](../models/sessionmessage.md)] | :heavy_check_mark:                                         | Session messages                                           |                                                            |