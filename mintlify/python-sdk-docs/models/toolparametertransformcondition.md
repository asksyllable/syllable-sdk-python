---
title: 'ToolParameterTransformCondition'
---

A condition to be met for a transform to be applied to the value of a tool parameter.


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `key`                                     | *str*                                     | TRUE                        | The name of the parameter to check.       | key                                       |
| `value`                                   | *str*                                     | TRUE                        | The value to check against the parameter. | value                                     |
| `operator`                                | *OptionalNullable[Literal["eq"]]*         | FALSE                        | The operator to use for the comparison.   |                                           |