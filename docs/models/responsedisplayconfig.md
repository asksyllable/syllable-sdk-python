# ResponseDisplayConfig

Declarative presentation metadata stored with a tool definition.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `version`                                                           | *Optional[Literal[1]]*                                              | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *Literal["card-list"]*                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `items_path`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `mapping`                                                           | [models.DisplayCardMapping](../models/displaycardmapping.md)        | :heavy_check_mark:                                                  | Supported mappings from one result item to the existing card shape. |