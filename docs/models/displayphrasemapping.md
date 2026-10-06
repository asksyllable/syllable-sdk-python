# DisplayPhraseMapping

A producer-owned localized phrase with per-item dynamic values.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `template`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `params`                                                                | Dict[str, [models.Params](../models/params.md)]                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `prose`                                                                 | Dict[str, [models.Prose](../models/prose.md)]                           | :heavy_minus_sign:                                                      | N/A                                                                     |
| `dates`                                                                 | Dict[str, [models.DisplayDateMapping](../models/displaydatemapping.md)] | :heavy_minus_sign:                                                      | N/A                                                                     |