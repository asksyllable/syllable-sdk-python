# Sessions.Transcript

## Overview

### Available Operations

* [get_by_id](#get_by_id) - Get Session Transcript By Id

## get_by_id

Return a session's transcript, and whether it is complete.

Transcript records reach the logs database through an asynchronous pipeline, so a read taken
immediately after a session ends can return a short record. `transcript_complete` is true only
when everything the session reported writing is present, across both the spoken transcript and
the tool activity in `actions`. A caller that needs the whole record should re-request with
exponential backoff until it is true, or until its own time limit passes, keeping the last
response either way.

A time limit is required rather than optional. `transcript_complete` never turns true for a
session still in progress, for a session on a channel that reports no expected count (only
voice reports one today), or for a session that ended before the field was introduced - so a
caller polling without a limit would never stop.

### Example Usage

<!-- UsageSnippet language="python" operationID="session_transcript_get_by_id" method="get" path="/api/v1/sessions/transcript/{session_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.sessions.transcript.get_by_id(session_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SessionTranscriptionResponse](../../models/sessiontranscriptionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |