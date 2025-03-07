# ToolFunction

A function available to an agent.

See:
- https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | The name of the function/tool call.                      | weather_fetcher                                          |
| `description`                                            | *str*                                                    | :heavy_check_mark:                                       | The description of the tool.                             | Fetches weather data                                     |
| `parameters`                                             | *Any*                                                    | :heavy_check_mark:                                       | The JSON Schema of parameters of the function/tool call. | {}                                                       |