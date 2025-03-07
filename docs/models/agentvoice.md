# AgentVoice

Voice option for an agent.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider`                                                          | [models.TtsProvider](../models/ttsprovider.md)                      | :heavy_check_mark:                                                  | TTS provider for an agent voice.                                    |
| `display_name`                                                      | [models.AgentVoiceDisplayName](../models/agentvoicedisplayname.md)  | :heavy_check_mark:                                                  | Display names of voices that Syllable supports.                     |
| `var_name`                                                          | [models.AgentVoiceVarName](../models/agentvoicevarname.md)          | :heavy_check_mark:                                                  | The variable name of an agent voice (used when procesing messages). |
| `gender`                                                            | [models.AgentVoiceGender](../models/agentvoicegender.md)            | :heavy_check_mark:                                                  | Gender for an agent voice.                                          |
| `supported_languages`                                               | List[[models.AgentLanguage](../models/agentlanguage.md)]            | :heavy_check_mark:                                                  | Languages supported by the voice                                    |
| `deprecated`                                                        | *bool*                                                              | :heavy_check_mark:                                                  | Whether the voice is deprecated and should not be used              |
| `model`                                                             | [Optional[models.AgentVoiceModel]](../models/agentvoicemodel.md)    | :heavy_minus_sign:                                                  | Model for an agent voice.                                           |