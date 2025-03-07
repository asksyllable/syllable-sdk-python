# InsightToolDefinition


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *int*                                                | :heavy_check_mark:                                   | Unique ID for Insight Tool Definition                |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | Human readable name of Insight Tool Definition       |
| `type`                                               | *str*                                                | :heavy_check_mark:                                   | Type of Insight Tool Definition                      |
| `description`                                        | *str*                                                | :heavy_check_mark:                                   | Text description of Insight Tool Definition          |
| `tool_parameters`                                    | [models.ToolParameters](../models/toolparameters.md) | :heavy_check_mark:                                   | Parameters for Insight Tool Definition               |
| `tool_result_set`                                    | [models.ToolResultSet](../models/toolresultset.md)   | :heavy_check_mark:                                   | Result key/types for Insight Tool Definition         |