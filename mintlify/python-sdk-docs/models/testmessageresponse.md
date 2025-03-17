---
title: 'TestMessageResponse'
---

Response from an agent in a test chat.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `test_id`                                                                | *str*                                                                    | TRUE                                                       | Channel-manager-side ID of the session (see Session.channel_manager_sid) |
| `agent_id`                                                               | *str*                                                                    | TRUE                                                       | ID of the agent with which the chat is taking place                      |
| `text`                                                                   | *Optional[str]*                                                          | FALSE                                                       | The text of the message that elicited the response                       |
| `response`                                                               | [Optional[models.Response]](../models/response.md)                       | FALSE                                                       | N/A                                                                      |
| `response_text`                                                          | *Optional[str]*                                                          | FALSE                                                       | The text of the response                                                 |