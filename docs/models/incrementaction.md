# IncrementAction


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `if_`                                                                          | [OptionalNullable[models.IncrementActionIf2]](../models/incrementactionif2.md) | :heavy_minus_sign:                                                             | An expression that must evaluate to true for the action to be applied.         |
| `action`                                                                       | *Optional[Literal["inc"]]*                                                     | :heavy_minus_sign:                                                             | N/A                                                                            |
| `name`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | Numeric destination path to increment.                                         |
| `by`                                                                           | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | Increment amount (defaults to 1).                                              |