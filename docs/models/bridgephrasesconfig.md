# BridgePhrasesConfig

Configuration for conversational bridge phrases.

Top-level fields are the default (English) phrases.
The `localized` dict provides per-language overrides keyed by BCP-47 language tag.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `first_slow_messages`                                                       | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Messages to say when the agent is first delayed.                            |
| `very_slow_messages`                                                        | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Messages to say when the agent is significantly delayed.                    |
| `tool_responses`                                                            | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Messages to say when a tool call is in progress.                            |
| `localized`                                                                 | Dict[str, [models.BridgePhraseMessages](../models/bridgephrasemessages.md)] | :heavy_minus_sign:                                                          | Per-language overrides keyed by BCP-47 tag (e.g. "es-US").                  |