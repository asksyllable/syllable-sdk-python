# CustomMessageHistoryRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `custom_message_id`                                                           | *int*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `page`                                                                        | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `order_by_direction`                                                          | [Optional[models.OrderByDirection]](../models/orderbydirection.md)            | :heavy_minus_sign:                                                            | The direction in which to order list results, either ascending or descending. |