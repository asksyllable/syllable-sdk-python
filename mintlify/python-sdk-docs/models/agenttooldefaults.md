---
title: 'AgentToolDefaults'
---

An agent-level configuration of default values for tool parameters for its tools.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `tool_name`                                                              | *str*                                                                    | TRUE                                                       | The name of the tool                                                     |
| `default_values`                                                         | List[[models.AgentToolFieldDefault](../models/agenttoolfielddefault.md)] | TRUE                                                       | The default values for fields used in the tool                           |