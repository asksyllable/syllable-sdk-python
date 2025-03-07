# LanguageGroups
(*language_groups*)

## Overview

### Available Operations

* [list](#list) - List Language Groups
* [create](#create) - Create Language Group
* [update](#update) - Update Language Group
* [get_by_id](#get_by_id) - Get Language Group
* [delete](#delete) - Delete Language Group

## list

Fetch language groups.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `page`                                                                                      | *OptionalNullable[int]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_fields`                                                                             | List[[models.LanguageGroupProperties](../../models/languagegroupproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_field_values`                                                                       | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by`                                                                                  | [OptionalNullable[models.LanguageGroupProperties]](../../models/languagegroupproperties.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by_direction`                                                                        | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)               | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `fields`                                                                                    | List[[models.LanguageGroupProperties](../../models/languagegroupproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `start_datetime`                                                                            | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `end_datetime`                                                                              | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListResponseLanguageGroupResponse](../../models/listresponselanguagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new language group.

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.create(name="Call Center 1 Languages", language_configs=[
        {
            "language_code": syllable_sdk.LanguageCode.ES_US,
            "voice_provider": syllable_sdk.TtsProvider.ELEVEN_LABS,
            "voice_display_name": syllable_sdk.AgentVoiceDisplayName.BRIAN,
            "dtmf_code": 1,
        },
    ], skip_current_language_in_message=True, description="Languages spoken by operators at Call Center 1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                            | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | The name of the language group.                                                                                                   | Call Center 1 Languages                                                                                                           |
| `language_configs`                                                                                                                | List[[models.LanguageConfig](../../models/languageconfig.md)]                                                                     | :heavy_check_mark:                                                                                                                | Voice and DTMF configurations for each language in the group.                                                                     |                                                                                                                                   |
| `skip_current_language_in_message`                                                                                                | *bool*                                                                                                                            | :heavy_check_mark:                                                                                                                | Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu. |                                                                                                                                   |
| `description`                                                                                                                     | *OptionalNullable[str]*                                                                                                           | :heavy_minus_sign:                                                                                                                | Description of the language group.                                                                                                | Languages spoken by operators at Call Center 1                                                                                    |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |

### Response

**[models.LanguageGroupResponse](../../models/languagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing language group

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.update(name="Call Center 1 Languages", language_configs=[
        {
            "language_code": syllable_sdk.LanguageCode.ES_US,
            "voice_provider": syllable_sdk.TtsProvider.ELEVEN_LABS,
            "voice_display_name": syllable_sdk.AgentVoiceDisplayName.WILL,
            "dtmf_code": 1,
        },
        {
            "language_code": syllable_sdk.LanguageCode.ES_US,
            "voice_provider": syllable_sdk.TtsProvider.ELEVEN_LABS,
            "voice_display_name": syllable_sdk.AgentVoiceDisplayName.WILL,
            "dtmf_code": 1,
        },
        {
            "language_code": syllable_sdk.LanguageCode.YUE_HK,
            "voice_provider": syllable_sdk.TtsProvider.GOOGLE,
            "voice_display_name": syllable_sdk.AgentVoiceDisplayName.GEORGE,
            "dtmf_code": 1,
        },
    ], skip_current_language_in_message=True, id=1, description="Languages spoken by operators at Call Center 1", edit_comments="Added Spanish support.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                            | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | The name of the language group.                                                                                                   | Call Center 1 Languages                                                                                                           |
| `language_configs`                                                                                                                | List[[models.LanguageConfig](../../models/languageconfig.md)]                                                                     | :heavy_check_mark:                                                                                                                | Voice and DTMF configurations for each language in the group.                                                                     |                                                                                                                                   |
| `skip_current_language_in_message`                                                                                                | *bool*                                                                                                                            | :heavy_check_mark:                                                                                                                | Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu. |                                                                                                                                   |
| `id`                                                                                                                              | *int*                                                                                                                             | :heavy_check_mark:                                                                                                                | The ID of the language group to update.                                                                                           | 1                                                                                                                                 |
| `description`                                                                                                                     | *OptionalNullable[str]*                                                                                                           | :heavy_minus_sign:                                                                                                                | Description of the language group.                                                                                                | Languages spoken by operators at Call Center 1                                                                                    |
| `edit_comments`                                                                                                                   | *OptionalNullable[str]*                                                                                                           | :heavy_minus_sign:                                                                                                                | Comments for the most recent edit to the language group.                                                                          | Added Spanish support.                                                                                                            |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |

### Response

**[models.LanguageGroupResponse](../../models/languagegroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Fetch a given language group.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.get_by_id(language_group_id=931598)

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
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a language group.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.language_groups.delete(language_group_id=545907, reason="<value>")

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
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |