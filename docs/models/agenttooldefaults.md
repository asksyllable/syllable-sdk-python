# AgentToolDefaults

An agent-level configuration of default values for tool parameters for its tools.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `tool_name`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | The name of the tool                                                     |
| `default_values`                                                         | List[[models.AgentToolFieldDefault](../models/agenttoolfielddefault.md)] | :heavy_check_mark:                                                       | The default values for fields used in the tool                           |