# InsightWorkflowExecutionSummary

How many of a workflow's executions are in each status, optionally within a
created_at date range. Counts cover all matching rows, not just one page.


## Fields

| Field                          | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `pending`                      | *Optional[int]*                | :heavy_minus_sign:             | Rows in PENDING status         | 5                              |
| `processing`                   | *Optional[int]*                | :heavy_minus_sign:             | Rows in PROCESSING status      | 2                              |
| `completed`                    | *Optional[int]*                | :heavy_minus_sign:             | Rows in COMPLETED status       | 100                            |
| `failed`                       | *Optional[int]*                | :heavy_minus_sign:             | Rows in FAILED status          | 3                              |
| `total`                        | *Optional[int]*                | :heavy_minus_sign:             | Total rows across all statuses | 110                            |