# Test
(*agents.test*)

## Overview

Operations for testing agents with live text.           These endpoints allow sending messages to an agent and receiving its responses.

### Available Operations

* [send_message](#send_message) - Send New Message

## send_message

Send a new message

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.test.send_message(service_name="<value>", source="<value>", test_id="<id>", agent_id="<id>", org_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `service_name`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | Name of the service producing the message                                              |
| `source`                                                                               | *str*                                                                                  | :heavy_check_mark:                                                                     | Name of the source of the message, should identify the user, like an email or username |
| `test_id`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | Channel-manager-side ID of the session (see Session.channel_manager_sid)               |
| `agent_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | ID of the agent with which the chat is taking place                                    |
| `org_name`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Name of the organization associated with the agent                                     |
| `text`                                                                                 | *OptionalNullable[str]*                                                                | :heavy_minus_sign:                                                                     | The text of the message                                                                |
| `override_timestamp`                                                                   | *OptionalNullable[str]*                                                                | :heavy_minus_sign:                                                                     | Override for the timestamp of the message                                              |
| `session_start`                                                                        | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Whether this message is the start of a new session                                     |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[models.TestMessageResponse](../../models/testmessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |