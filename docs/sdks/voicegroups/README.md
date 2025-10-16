# VoiceGroups
(*voice_groups*)

## Overview

### Available Operations

* [list](#list) - List Voice Groups
* [create](#create) - Create Voice Group
* [update](#update) - Update Voice Group
* [get_by_id](#get_by_id) - Get Voice Group
* [delete](#delete) - Delete Voice Group
* [voice_groups_create_voice_sample](#voice_groups_create_voice_sample) - Create Voice Sample

## list

Fetch voice groups.

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_list" method="get" path="/api/v1/voice_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.list(page=0, limit=25, search_fields=[
        models.VoiceGroupProperties.NAME,
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
| `search_fields`                                                                                                                                        | List[[models.VoiceGroupProperties](../../models/voicegroupproperties.md)]                                                                              | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.VoiceGroupProperties]](../../models/voicegroupproperties.md)                                                                  | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.VoiceGroupProperties](../../models/voicegroupproperties.md)]                                                                              | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseVoiceGroupResponse](../../models/listresponsevoicegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new voice group.

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_create" method="post" path="/api/v1/voice_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.create(request={
        "name": "Call Center 1 Languages",
        "description": "Languages spoken by operators at Call Center 1",
        "language_configs": [
            {
                "language_code": models.LanguageCode.EN_US,
                "voice_provider": models.TtsProvider.OPEN_AI,
                "voice_display_name": models.AgentVoiceDisplayName.ALLOY,
                "dtmf_code": 1,
            },
            {
                "language_code": models.LanguageCode.ES_US,
                "voice_provider": models.TtsProvider.GOOGLE,
                "voice_display_name": models.AgentVoiceDisplayName.ES_US_NEURAL2_B,
                "dtmf_code": 2,
            },
        ],
        "skip_current_language_in_message": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.VoiceGroupCreateRequest](../../models/voicegroupcreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.VoiceGroupResponse](../../models/voicegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing voice group

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_update" method="put" path="/api/v1/voice_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.update(request={
        "name": "Call Center 1 Languages",
        "description": "Languages spoken by operators at Call Center 1",
        "language_configs": [
            {
                "language_code": models.LanguageCode.EN_US,
                "voice_provider": models.TtsProvider.OPEN_AI,
                "voice_display_name": models.AgentVoiceDisplayName.ALLOY,
                "dtmf_code": 1,
            },
            {
                "language_code": models.LanguageCode.ES_US,
                "voice_provider": models.TtsProvider.GOOGLE,
                "voice_display_name": models.AgentVoiceDisplayName.ES_US_NEURAL2_B,
                "dtmf_code": 2,
            },
        ],
        "skip_current_language_in_message": True,
        "id": 1,
        "edit_comments": "Added Spanish support.",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.VoiceGroupUpdateRequest](../../models/voicegroupupdaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.VoiceGroupResponse](../../models/voicegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Fetch a given voice group.

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_get_by_id" method="get" path="/api/v1/voice_groups/{voice_group_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.get_by_id(voice_group_id=431245)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `voice_group_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VoiceGroupResponse](../../models/voicegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a voice group.

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_delete" method="delete" path="/api/v1/voice_groups/{voice_group_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.delete(voice_group_id=225046, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `voice_group_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## voice_groups_create_voice_sample

Generate voice sample.

### Example Usage

<!-- UsageSnippet language="python" operationID="voice_groups_create_voice_sample" method="post" path="/api/v1/voice_groups/voices/sample" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.voice_groups.voice_groups_create_voice_sample(request={
        "language_code": models.LanguageCode.FA_IR,
        "voice_provider": models.TtsProvider.GOOGLE,
        "voice_display_name": models.AgentVoiceDisplayName.VINDEMIATRIX_ENGLISH_,
        "voice_speed": 1,
        "voice_pitch": 0,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.VoiceSampleCreateRequest](../../models/voicesamplecreaterequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |