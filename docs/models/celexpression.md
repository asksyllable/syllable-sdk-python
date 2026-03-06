# CelExpression

Google CEL expression object.

Use this object form when you want CEL syntax:
{"type": "cel", "expression": "inputs.count + 1"}
See https://github.com/google/cel-spec/blob/master/doc/langdef.md


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `expression`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | CEL expression string.                                                                    | inputs.can_sign_consent == true                                                           |
| `type`                                                                                    | *Optional[Literal["cel"]]*                                                                | :heavy_minus_sign:                                                                        | CEL expression language selector. Use with object form {"type":"cel","expression":"..."}. |                                                                                           |