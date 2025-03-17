---
title: 'InsightWorkflowInput'
---


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `name`                                                                               | *str*                                                                                | TRUE                                                                   | Human readable name of Insight Workflow                                              |
| `description`                                                                        | *str*                                                                                | TRUE                                                                   | Text description of Insight Workflow                                                 |
| `insight_tool_ids`                                                                   | List[*int*]                                                                          | TRUE                                                                   | List of Insight Tool IDs                                                             |
| `conditions`                                                                         | [models.InsightWorkflowInputConditions](../models/insightworkflowinputconditions.md) | TRUE                                                                   | Conditions for Insight Workflow                                                      |
| `status`                                                                             | *str*                                                                                | TRUE                                                                   | Status of the Insight Workflow                                                       |