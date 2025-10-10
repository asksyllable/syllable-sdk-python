# PronunciationOverride

A single text replacement rule.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `text`                                               | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `replacement`                                        | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `languages`                                          | List[*str*]                                          | :heavy_minus_sign:                                   | N/A                                                  |
| `provider`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `voice`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `match_type`                                         | [Optional[models.MatchType]](../models/matchtype.md) | :heavy_minus_sign:                                   | Matching strategy for override text.                 |
| `match_options`                                      | List[*str*]                                          | :heavy_minus_sign:                                   | N/A                                                  |
| `enabled`                                            | *Optional[bool]*                                     | :heavy_minus_sign:                                   | N/A                                                  |
| `notes`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |