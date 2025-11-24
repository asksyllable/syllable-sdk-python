# ConditionalText


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `if_`                                                                          | [OptionalNullable[models.ConditionalTextIf2]](../models/conditionaltextif2.md) | :heavy_minus_sign:                                                             | An expression that must evaluate to true for the action to be applied.         |
| `text`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | Text to apply if the condition is true.                                        |