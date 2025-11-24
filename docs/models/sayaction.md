# SayAction


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `if_`                                                                  | [OptionalNullable[models.SayActionIf2]](../models/sayactionif2.md)     | :heavy_minus_sign:                                                     | An expression that must evaluate to true for the action to be applied. |
| `text`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Text to apply if the condition is true.                                |
| `action`                                                               | *Optional[Literal["say"]]*                                             | :heavy_minus_sign:                                                     | N/A                                                                    |
| `role`                                                                 | [Optional[models.Role]](../models/role.md)                             | :heavy_minus_sign:                                                     | The role of the message.                                               |