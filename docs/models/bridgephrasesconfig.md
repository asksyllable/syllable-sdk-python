# BridgePhrasesConfig

Configuration for conversational bridge phrases.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `first_slow_messages`                                    | List[*str*]                                              | :heavy_minus_sign:                                       | Messages to say when the agent is first delayed.         |
| `very_slow_messages`                                     | List[*str*]                                              | :heavy_minus_sign:                                       | Messages to say when the agent is significantly delayed. |
| `tool_responses`                                         | List[*str*]                                              | :heavy_minus_sign:                                       | Messages to say when a tool call is in progress.         |