# LatencyEntry

Data model for latency entries.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `measurement_start`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `category`                                                           | [models.LatencyCategory](../models/latencycategory.md)               | :heavy_check_mark:                                                   | N/A                                                                  |
| `label`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `metadata`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `unit_type`                                                          | [models.LatencyUnitType](../models/latencyunittype.md)               | :heavy_check_mark:                                                   | N/A                                                                  |
| `value`                                                              | *float*                                                              | :heavy_check_mark:                                                   | N/A                                                                  |
| `value_str`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `time_delta`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |