# AgentToolDefaults

Agent-level static parameter values for a tool, overriding any tool-level defaults.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `tool_name`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | The name of the tool                                                     | get_weather                                                              |
| `default_values`                                                         | List[[models.AgentToolFieldDefault](../models/agenttoolfielddefault.md)] | :heavy_check_mark:                                                       | The default values for fields used in the tool                           | [<br/>{<br/>"default_value": "fahrenheit",<br/>"field_name": "temperature_unit"<br/>}<br/>] |