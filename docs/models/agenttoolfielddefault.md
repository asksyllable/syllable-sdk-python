# AgentToolFieldDefault

Agent-level value for a static parameter on a tool, overriding the tool-level default if one
exists.


## Fields

| Field                           | Type                            | Required                        | Description                     | Example                         |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `field_name`                    | *str*                           | :heavy_check_mark:              | The name of the field           | temperature_unit                |
| `default_value`                 | *Any*                           | :heavy_check_mark:              | The default value for the field | fahrenheit                      |