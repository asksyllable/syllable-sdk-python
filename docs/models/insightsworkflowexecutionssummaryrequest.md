# InsightsWorkflowExecutionsSummaryRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `workflow_id`                                                | *int*                                                        | :heavy_check_mark:                                           | N/A                                                          |                                                              |
| `start_datetime`                                             | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | ISO 8601 start datetime (inclusive) for created_at filtering | 2026-08-27T13:57:00.123456+00:00                             |
| `end_datetime`                                               | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | ISO 8601 end datetime (exclusive) for created_at filtering   | 2026-08-28T00:00:00Z                                         |