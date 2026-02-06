# ~~LanguageGroups~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

Operations related to language groups. A language group is a           collection of language, voice, and DTMF configuration that can be linked to an agent to           define the languages and voices it supports. For more information, see           [Console docs](https://docs.syllable.ai/Resources/LanguageGroups).

### Available Operations

* [~~list~~](#list) - List Language Groups :warning: **Deprecated**
* [~~create~~](#create) - Create Language Group :warning: **Deprecated**
* [~~update~~](#update) - Update Language Group :warning: **Deprecated**
* [~~get_by_id~~](#get_by_id) - Get Language Group :warning: **Deprecated**
* [~~delete~~](#delete) - Delete Language Group :warning: **Deprecated**
* [~~language_groups_create_voice_sample~~](#language_groups_create_voice_sample) - Create Voice Sample :warning: **Deprecated**

## ~~list~~

Deprecated alias for `GET /api/v1/voice_groups/`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_list" method="get" path="/api/v1/language_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.list(page=0, limit=25, search_fields=[
        models.LanguageGroupProperties.NAME,
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
| `search_fields`                                                                                                                                        | List[[models.LanguageGroupProperties](../../models/languagegroupproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.LanguageGroupProperties]](../../models/languagegroupproperties.md)                                                            | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.LanguageGroupProperties](../../models/languagegroupproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseLanguageGroupResponse](../../models/listresponselanguagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~create~~

Deprecated alias for `POST /api/v1/voice_groups/`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_create" method="post" path="/api/v1/language_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.create(request={
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

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.LanguageGroupCreateRequest](../../models/languagegroupcreaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.LanguageGroupResponse](../../models/languagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~update~~

Deprecated alias for `PUT /api/v1/voice_groups/`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_update" method="put" path="/api/v1/language_groups/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.update(request={
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

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.LanguageGroupUpdateRequest](../../models/languagegroupupdaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.LanguageGroupResponse](../../models/languagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~get_by_id~~

Deprecated alias for `GET /api/v1/voice_groups/{voice_group_id}`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_get_by_id" method="get" path="/api/v1/language_groups/{language_group_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.get_by_id(language_group_id=453313)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `language_group_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LanguageGroupResponse](../../models/languagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~delete~~

Deprecated alias for `DELETE /api/v1/voice_groups/{voice_group_id}`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_delete" method="delete" path="/api/v1/language_groups/{language_group_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.delete(language_group_id=572805, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `language_group_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~language_groups_create_voice_sample~~

Deprecated alias for `POST /api/v1/voice_groups/voices/sample`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="language_groups_create_voice_sample" method="post" path="/api/v1/language_groups/voices/sample" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.language_groups_create_voice_sample(request={
        "language_code": models.LanguageCode.ZH_CN,
        "voice_provider": models.TtsProvider.GOOGLE,
        "voice_display_name": models.AgentVoiceDisplayName.EN_US_NEURAL2_F,
        "voice_speed": 1,
        "voice_pitch": 0,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.LanguageSampleCreateRequest](../../models/languagesamplecreaterequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[httpx.Response](../../models/bytes.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |