# TestMessageResponse

Response from an agent in a test chat.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `test_id`                                                                | *str*                                                                    | :heavy_check_mark:                                                       | Channel-manager-side ID of the session (see Session.channel_manager_sid) |
| `agent_id`                                                               | *str*                                                                    | :heavy_check_mark:                                                       | ID of the agent with which the chat is taking place                      |
| `text`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The text of the message that elicited the response                       |
| `response`                                                               | [Optional[models.Response]](../models/response.md)                       | :heavy_minus_sign:                                                       | The response from the agent                                              |
| `response_text`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The text of the response                                                 |