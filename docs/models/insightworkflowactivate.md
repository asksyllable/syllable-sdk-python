# InsightWorkflowActivate

Request model to activate an insight workflow.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `is_acknowledged`                                                      | *bool*                                                                 | :heavy_check_mark:                                                     | Flag to indicate if the user has acknowledged the estimate             | true                                                                   |
| `estimate`                                                             | [models.InsightWorkflowEstimate](../models/insightworkflowestimate.md) | :heavy_check_mark:                                                     | Response model for an insight workflow.                                |                                                                        |