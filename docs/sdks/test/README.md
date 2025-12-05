# Agents.Test

## Overview

Operations for testing agents with live text.           These endpoints allow sending messages to an agent and receiving its responses.

### Available Operations

* [send_test_message](#send_test_message) - Send New Message

## send_test_message

Send a new message

### Example Usage

<!-- UsageSnippet language="python" operationID="send_test_message" method="post" path="/api/v1/agents/test/messages" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.test.send_test_message(request={
        "service_name": "<value>",
        "source": "user@email.com",
        "text": "Hello",
        "test_id": "<id>",
        "agent_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TestMessage](../../models/testmessage.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestMessageResponse](../../models/testmessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |