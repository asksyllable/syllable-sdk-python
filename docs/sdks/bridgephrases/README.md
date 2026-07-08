# BridgePhrases

## Overview

### Available Operations

* [list](#list) - List Bridge Phrases
* [create](#create) - Create Bridge Phrases
* [update](#update) - Update Bridge Phrases
* [get_by_id](#get_by_id) - Get Bridge Phrases
* [delete](#delete) - Delete Bridge Phrases

## list

Fetch bridge phrases configs.

### Example Usage

<!-- UsageSnippet language="python" operationID="bridge_phrases_list" method="get" path="/api/v1/bridge_phrases/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.bridge_phrases.list(page=0, limit=25, search_fields=[
        models.BridgePhrasesProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            | Example                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The page number from which to start (0-based)                                                                                                          | 0                                                                                                                                                      |
| `limit`                                                                                                                                                | *Optional[int]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | The maximum number of items to return                                                                                                                  | 25                                                                                                                                                     |
| `search_fields`                                                                                                                                        | List[[models.BridgePhrasesProperties](../../models/bridgephrasesproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.BridgePhrasesProperties]](../../models/bridgephrasesproperties.md)                                                            | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.BridgePhrasesProperties](../../models/bridgephrasesproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseBridgePhrasesResponse](../../models/listresponsebridgephrasesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new bridge phrases config.

### Example Usage

<!-- UsageSnippet language="python" operationID="bridge_phrases_create" method="post" path="/api/v1/bridge_phrases/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.bridge_phrases.create(request={
        "name": "Default Bridge Phrases",
        "description": "Standard hold phrases for inbound line.",
        "config": {
            "phrases": {
                "messages": [
                    "One moment, please.",
                    "Let me check on that for you.",
                ],
                "localized": {
                    "es-US": {
                        "messages": [
                            "Un momento, por favor.",
                        ],
                    },
                    "fr-FR": {
                        "messages": [
                            "Un instant, je vous en prie.",
                        ],
                    },
                },
            },
            "tools": [
                {
                    "tool_name": "<value>",
                    "phrases": {
                        "messages": [
                            "One moment, please.",
                            "Let me check on that for you.",
                        ],
                        "localized": {
                            "es-US": {
                                "messages": [
                                    "Un momento, por favor.",
                                ],
                            },
                            "fr-FR": {
                                "messages": [
                                    "Un instant, je vous en prie.",
                                ],
                            },
                        },
                    },
                },
            ],
            "randomize_bridge_phrases": True,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.BridgePhrasesCreateRequest](../../models/bridgephrasescreaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.BridgePhrasesResponse](../../models/bridgephrasesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing bridge phrases config.

### Example Usage

<!-- UsageSnippet language="python" operationID="bridge_phrases_update" method="put" path="/api/v1/bridge_phrases/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.bridge_phrases.update(request={
        "name": "Default Bridge Phrases",
        "description": "Standard hold phrases for inbound line.",
        "config": {
            "phrases": {
                "messages": [
                    "One moment, please.",
                    "Let me check on that for you.",
                ],
                "localized": {
                    "es-US": {
                        "messages": [
                            "Un momento, por favor.",
                        ],
                    },
                    "fr-FR": {
                        "messages": [
                            "Un instant, je vous en prie.",
                        ],
                    },
                },
            },
            "tools": [
                {
                    "tool_name": "<value>",
                    "phrases": {
                        "messages": [
                            "One moment, please.",
                            "Let me check on that for you.",
                        ],
                        "localized": {
                            "es-US": {
                                "messages": [
                                    "Un momento, por favor.",
                                ],
                            },
                            "fr-FR": {
                                "messages": [
                                    "Un instant, je vous en prie.",
                                ],
                            },
                        },
                    },
                },
            ],
            "randomize_bridge_phrases": True,
        },
        "id": 1,
        "edit_comments": "Added Spanish overrides for the transfer tool.",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.BridgePhrasesUpdateRequest](../../models/bridgephrasesupdaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.BridgePhrasesResponse](../../models/bridgephrasesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Fetch a given bridge phrases config.

### Example Usage

<!-- UsageSnippet language="python" operationID="bridge_phrases_get_by_id" method="get" path="/api/v1/bridge_phrases/{bridge_phrases_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.bridge_phrases.get_by_id(bridge_phrases_id=627472)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bridge_phrases_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BridgePhrasesResponse](../../models/bridgephrasesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a bridge phrases config.

### Example Usage

<!-- UsageSnippet language="python" operationID="bridge_phrases_delete" method="delete" path="/api/v1/bridge_phrases/{bridge_phrases_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.bridge_phrases.delete(bridge_phrases_id=722051, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bridge_phrases_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |