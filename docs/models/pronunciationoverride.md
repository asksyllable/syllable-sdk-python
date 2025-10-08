# PronunciationOverride

A single text replacement rule.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `text`                                                     | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `replacement`                                              | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `language`                                                 | [OptionalNullable[models.Language]](../models/language.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `provider`                                                 | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `voice`                                                    | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `match_type`                                               | [Optional[models.MatchType]](../models/matchtype.md)       | :heavy_minus_sign:                                         | Matching strategy for override text.                       |
| `match_options`                                            | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `enabled`                                                  | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `notes`                                                    | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |