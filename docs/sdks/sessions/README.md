# Sessions
(*sessions*)

## Overview

Operations related to sessions. A session is a building block of a           conversation.

### Available Operations

* [list](#list) - Sessions List
* [get_full_summary](#get_full_summary) - Get Full Session Summary By Id
* [get_by_id](#get_by_id) - Get A Single Session By Id
* [stream_recording](#stream_recording) - Stream Recording

## list

Sessions List

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.sessions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `page`                                                                          | *OptionalNullable[int]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_fields`                                                                 | List[[models.SessionProperties](../../models/sessionproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_field_values`                                                           | List[*str*]                                                                     | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by`                                                                      | [OptionalNullable[models.SessionProperties]](../../models/sessionproperties.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by_direction`                                                            | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)   | :heavy_minus_sign:                                                              | N/A                                                                             |
| `fields`                                                                        | List[[models.SessionProperties](../../models/sessionproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `start_datetime`                                                                | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `end_datetime`                                                                  | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ListResponseSession](../../models/listresponsesession.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_full_summary

Get Full Session Summary By Id

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.sessions.get_full_summary(session_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SessionSummaryResponse](../../models/sessionsummaryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Get A Single Session By Id

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.sessions.get_by_id(session_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## stream_recording

Stream Recording

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.sessions.stream_recording(token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |