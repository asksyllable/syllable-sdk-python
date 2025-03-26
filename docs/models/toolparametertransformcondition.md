# ToolParameterTransformCondition

A condition to be met for a transform to be applied to the value of a tool parameter.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `key`                                                                | *str*                                                                | :heavy_check_mark:                                                   | The name of the parameter to check.                                  | key                                                                  |
| `value`                                                              | *str*                                                                | :heavy_check_mark:                                                   | The value to check against the parameter.                            | value                                                                |
| `operator`                                                           | *OptionalNullable[Literal["eq"]]*                                    | :heavy_minus_sign:                                                   | The operator to use for the comparison. Currently only supports "eq" | eq                                                                   |