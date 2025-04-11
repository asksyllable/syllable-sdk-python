# SummaryEntry

A summary entry is an aggregation of latency entries by category and sub-category.
It contains the total and average latency for each category.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `category`                                             | [models.LatencyCategory](../models/latencycategory.md) | :heavy_check_mark:                                     | N/A                                                    |
| `sub_category`                                         | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `event_count`                                          | *int*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `sum_ms`                                               | *float*                                                | :heavy_check_mark:                                     | N/A                                                    |
| `sum_str`                                              | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `average_ms`                                           | *float*                                                | :heavy_check_mark:                                     | N/A                                                    |
| `average_str`                                          | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |