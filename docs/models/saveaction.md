# SaveAction


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `if_`                                                                  | [OptionalNullable[models.SaveActionIf2]](../models/saveactionif2.md)   | :heavy_minus_sign:                                                     | An expression that must evaluate to true for the action to be applied. |
| `action`                                                               | *Optional[Literal["save"]]*                                            | :heavy_minus_sign:                                                     | N/A                                                                    |
| `name`                                                                 | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | Target name to save (defaults to global variable).                     |
| `inputs`                                                               | List[*str*]                                                            | :heavy_minus_sign:                                                     | Input field names to persist; None saves all collected inputs.         |