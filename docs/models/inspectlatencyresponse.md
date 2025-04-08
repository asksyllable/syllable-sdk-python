# InspectLatencyResponse

This is a report of the time spent in each operation during this session. It contains a timeline,
which lists the operations in the order they were executed, and a summary, which aggregates the
operations by category and sub-category.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `session_id`                                           | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `timeline`                                             | List[[models.LatencyEntry](../models/latencyentry.md)] | :heavy_check_mark:                                     | N/A                                                    |
| `summary`                                              | List[[models.SummaryEntry](../models/summaryentry.md)] | :heavy_minus_sign:                                     | N/A                                                    |