# SessionTranscriptionResponse

Text transcript of a given session. For more information, see
[Console docs](https://docs.syllable.ai/workspaces/Sessions).


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `session_id`                                             | *str*                                                    | :heavy_check_mark:                                       | Internal ID of the session                               |
| `transcription`                                          | List[[models.SessionText](../models/sessiontext.md)]     | :heavy_check_mark:                                       | Transcriptions of all messages in the session            |
| `actions`                                                | List[[models.SessionAction](../models/sessionaction.md)] | :heavy_check_mark:                                       | Tool invocations that occurred during the session        |