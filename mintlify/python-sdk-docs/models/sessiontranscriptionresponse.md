---
title: 'SessionTranscriptionResponse'
---

Text transcript of a given session. For more information, see
[Console docs](https://docs.syllable.ai/workspaces/Sessions).


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `session_id`                                             | *str*                                                    | TRUE                                       | Internal ID of the session                               |
| `transcription`                                          | List[[models.SessionText](../models/sessiontext.md)]     | TRUE                                       | Transcriptions of all messages in the session            |
| `actions`                                                | List[[models.SessionAction](../models/sessionaction.md)] | TRUE                                       | Tool invocations that occurred during the session        |