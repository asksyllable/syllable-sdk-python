# CustomMessageUpdateRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | The name of the custom message                                   |
| `text`                                                           | *str*                                                            | :heavy_check_mark:                                               | The text of the custom message                                   |
| `id`                                                             | *int*                                                            | :heavy_check_mark:                                               | The ID of the custom message                                     |
| `label`                                                          | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | The label of the custom message                                  |
| `rules`                                                          | List[[models.CustomMessageRule](../models/custommessagerule.md)] | :heavy_minus_sign:                                               | Rules for time-specific message variants                         |
| `type`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |