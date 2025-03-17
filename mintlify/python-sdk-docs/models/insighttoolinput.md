---
title: 'InsightToolInput'
---


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `name`                                                                             | *str*                                                                              | TRUE                                                                 | Human readable name of Insight Tool                                                |
| `description`                                                                      | *str*                                                                              | TRUE                                                                 | Text description of Insight Tool                                                   |
| `version`                                                                          | *int*                                                                              | TRUE                                                                 | Version number of Insight Tool                                                     |
| `tool_arguments`                                                                   | [models.InsightToolInputToolArguments](../models/insighttoolinputtoolarguments.md) | TRUE                                                                 | Arguments for Insight Tool                                                         |
| `insight_tool_definition_id`                                                       | *int*                                                                              | TRUE                                                                 | Unique ID for Insight Tool Definition                                              |