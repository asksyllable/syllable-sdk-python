# JMESPathExpression

JMESPath expression object.

Use this object form to explicitly mark JMESPath syntax:
{"type": "jp", "expression": "inputs.can_sign_consent == `true`"}
See https://jmespath.org/specification.html#grammar


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `expression`                                                                                             | *str*                                                                                                    | :heavy_check_mark:                                                                                       | JMESPath expression string.                                                                              | inputs.can_sign_consent == `true`                                                                        |
| `type`                                                                                                   | [Optional[models.JMESPathExpressionType]](../models/jmespathexpressiontype.md)                           | :heavy_minus_sign:                                                                                       | JMESPath expression language selector. Use with object form {"type":"jp"\|"jmespath","expression":"..."}. |                                                                                                          |