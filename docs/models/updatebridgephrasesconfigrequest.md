# UpdateBridgePhrasesConfigRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `agent_id`                                                     | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | Agent ID to update config for                                  |
| `tool_name`                                                    | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | Tool name to update config for                                 |
| `bridge_phrases_config`                                        | [models.BridgePhrasesConfig](../models/bridgephrasesconfig.md) | :heavy_check_mark:                                             | N/A                                                            |