# CustomMessages
(*custom_messages*)

## Overview

### Available Operations

* [list](#list) - Custom Messages List
* [create](#create) - Create Custom Message
* [update](#update) - Update Custom Message
* [get](#get) - Get Custom Message By Id
* [delete](#delete) - Delete Custom Message

## list

List the existing custom_messages

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `page`                                                                                      | *OptionalNullable[int]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_fields`                                                                             | List[[models.CustomMessageProperties](../../models/custommessageproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_field_values`                                                                       | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by`                                                                                  | [OptionalNullable[models.CustomMessageProperties]](../../models/custommessageproperties.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by_direction`                                                                        | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)               | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `fields`                                                                                    | List[[models.CustomMessageProperties](../../models/custommessageproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `start_datetime`                                                                            | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `end_datetime`                                                                              | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListResponseCustomMessageResponse](../../models/listresponsecustommessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new custom message

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.create(name="<value>", text="<value>", rules=[
        {
            "description": "delightfully fumigate convection though zowie up bulky electronics",
            "invert": False,
            "text": "Sorry, we're closed today",
            "time_range_start": "09:00",
            "time_range_end": "17:00",
            "date_": "2025-01-01",
            "days_of_week": [
                syllable_sdk.DayOfWeek.MO,
                syllable_sdk.DayOfWeek.TU,
                syllable_sdk.DayOfWeek.WE,
                syllable_sdk.DayOfWeek.TH,
                syllable_sdk.DayOfWeek.FR,
            ],
        },
        {
            "description": "yuck forager beneath please shadowy foodstuffs welcome",
            "invert": True,
            "text": "Sorry, we're closed today",
            "time_range_start": "09:00",
            "time_range_end": "17:00",
            "date_": "2025-01-01",
            "days_of_week": [
                syllable_sdk.DayOfWeek.MO,
                syllable_sdk.DayOfWeek.TU,
                syllable_sdk.DayOfWeek.WE,
                syllable_sdk.DayOfWeek.TH,
                syllable_sdk.DayOfWeek.FR,
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the custom message                                      |
| `text`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The text of the custom message                                      |
| `label`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The label of the custom message                                     |
| `rules`                                                             | List[[models.CustomMessageRule](../../models/custommessagerule.md)] | :heavy_minus_sign:                                                  | Rules for time-specific message variants                            |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomMessageResponse](../../models/custommessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a custom message

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.update(name="<value>", text="<value>", id=975440, rules=[
        {
            "description": "technician eulogise whereas till mild than during",
            "invert": True,
            "text": "Sorry, we're closed today",
            "time_range_start": "09:00",
            "time_range_end": "17:00",
            "date_": "2025-01-01",
            "days_of_week": [
                syllable_sdk.DayOfWeek.MO,
                syllable_sdk.DayOfWeek.TU,
                syllable_sdk.DayOfWeek.WE,
                syllable_sdk.DayOfWeek.TH,
                syllable_sdk.DayOfWeek.FR,
            ],
        },
        {
            "description": "qualified cycle woot abseil perfumed fisherman with duh",
            "invert": True,
            "text": "Sorry, we're closed today",
            "time_range_start": "09:00",
            "time_range_end": "17:00",
            "date_": "2025-01-01",
            "days_of_week": [
                syllable_sdk.DayOfWeek.MO,
                syllable_sdk.DayOfWeek.TU,
                syllable_sdk.DayOfWeek.WE,
                syllable_sdk.DayOfWeek.TH,
                syllable_sdk.DayOfWeek.FR,
            ],
        },
        {
            "description": "ultimately in likely opera please antelope",
            "invert": True,
            "text": "Sorry, we're closed today",
            "time_range_start": "09:00",
            "time_range_end": "17:00",
            "date_": "2025-01-01",
            "days_of_week": [
                syllable_sdk.DayOfWeek.MO,
                syllable_sdk.DayOfWeek.TU,
                syllable_sdk.DayOfWeek.WE,
                syllable_sdk.DayOfWeek.TH,
                syllable_sdk.DayOfWeek.FR,
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the custom message                                      |
| `text`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The text of the custom message                                      |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the custom message                                        |
| `label`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The label of the custom message                                     |
| `rules`                                                             | List[[models.CustomMessageRule](../../models/custommessagerule.md)] | :heavy_minus_sign:                                                  | Rules for time-specific message variants                            |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomMessageResponse](../../models/custommessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get the custom message by its ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.get(custom_message_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_message_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomMessageResponse](../../models/custommessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete custom message by ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.delete(custom_message_id=545907, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_message_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |