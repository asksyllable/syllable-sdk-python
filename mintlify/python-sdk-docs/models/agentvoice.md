---
title: 'AgentVoice'
---

Voice option for an agent.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider`                                                          | [models.TtsProvider](../models/ttsprovider.md)                      | TRUE                                                  | TTS provider for an agent voice.                                    |
| `display_name`                                                      | [models.AgentVoiceDisplayName](../models/agentvoicedisplayname.md)  | TRUE                                                  | Display names of voices that Syllable supports.                     |
| `var_name`                                                          | [models.AgentVoiceVarName](../models/agentvoicevarname.md)          | TRUE                                                  | The variable name of an agent voice (used when procesing messages). |
| `gender`                                                            | [models.AgentVoiceGender](../models/agentvoicegender.md)            | TRUE                                                  | Gender for an agent voice.                                          |
| `supported_languages`                                               | List[[models.AgentLanguage](../models/agentlanguage.md)]            | TRUE                                                  | Languages supported by the voice                                    |
| `deprecated`                                                        | *bool*                                                              | TRUE                                                  | Whether the voice is deprecated and should not be used              |
| `model`                                                             | [Optional[models.AgentVoiceModel]](../models/agentvoicemodel.md)    | FALSE                                                  | Model for an agent voice.                                           |