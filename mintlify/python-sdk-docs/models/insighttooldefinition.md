---
title: 'InsightToolDefinition'
---


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *int*                                                | TRUE                                   | Unique ID for Insight Tool Definition                |
| `name`                                               | *str*                                                | TRUE                                   | Human readable name of Insight Tool Definition       |
| `type`                                               | *str*                                                | TRUE                                   | Type of Insight Tool Definition                      |
| `description`                                        | *str*                                                | TRUE                                   | Text description of Insight Tool Definition          |
| `tool_parameters`                                    | [models.ToolParameters](../models/toolparameters.md) | TRUE                                   | Parameters for Insight Tool Definition               |
| `tool_result_set`                                    | [models.ToolResultSet](../models/toolresultset.md)   | TRUE                                   | Result key/types for Insight Tool Definition         |