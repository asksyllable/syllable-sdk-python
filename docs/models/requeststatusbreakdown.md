# RequestStatusBreakdown

Per-request_status breakdown with total count and optional channel_manager_status counts.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `total_count`                                                                | *int*                                                                        | :heavy_check_mark:                                                           | Total number of requests with this request_status                            |                                                                              |
| `counts`                                                                     | Dict[str, *int*]                                                             | :heavy_minus_sign:                                                           | Counts by channel_manager_status within this request_status; omitted if none | {<br/>"DELIVERED": 2,<br/>"PENDING": 3,<br/>"SENT": 5<br/>}                  |