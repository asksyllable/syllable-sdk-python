# InsightConditionRule


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `rule_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `source`                                                   | [models.Source](../models/source.md)                       | :heavy_check_mark:                                         | N/A                                                        |
| `field`                                                    | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `operator`                                                 | [OptionalNullable[models.Operator]](../models/operator.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `value`                                                    | *Optional[Any]*                                            | :heavy_minus_sign:                                         | N/A                                                        |