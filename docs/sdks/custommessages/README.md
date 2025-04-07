# CustomMessages
(*custom_messages*)

## Overview

Operations related to custom message configuration.           A custom message is a pre-configured message delivered by an agent as a greeting at the           beginning of a conversation. Multiple agents can use the same custom mesasage. A custom           message has one or more rules defined, which allow for different messages to be           dynamically selected and delivered at runtime based on the current time and either           date or day of the week. For more information, see           [Console docs](https://docs.syllable.ai/Resources/Messages).

### Available Operations

* [list](#list) - Custom Messages List
* [create](#create) - Create Custom Message
* [update](#update) - Update Custom Message
* [get_by_id](#get_by_id) - Get Custom Message By Id
* [delete](#delete) - Delete Custom Message

## list

List the existing custom_messages

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.list(page=0, search_fields=[
        syllable_sdk.CustomMessageProperties.NAME,
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
| `search_fields`                                                                                                                                        | List[[models.CustomMessageProperties](../../models/custommessageproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.CustomMessageProperties]](../../models/custommessageproperties.md)                                                            | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.CustomMessageProperties](../../models/custommessageproperties.md)]                                                                        | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

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

    res = ss_client.custom_messages.create(request={
        "name": "Customer service greeting",
        "text": "Hello and thank you for calling customer service. How can I help you today?",
        "label": "Customer service",
        "rules": [
            {
                "description": "Closed on New Year's Day",
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
                "invert": False,
                "text": "Hello, thank you for calling. Sorry, we're closed today.",
            },
            {
                "description": "Closed on New Year's Day",
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
                "invert": False,
                "text": "Hello, thank you for calling. Sorry, we're closed today.",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CustomMessageCreateRequest](../../models/custommessagecreaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

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

    res = ss_client.custom_messages.update(request={
        "name": "Customer service greeting",
        "text": "Hello and thank you for calling customer service. How can I help you today?",
        "label": "Customer service",
        "rules": [
            {
                "description": "Closed on New Year's Day",
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
                "invert": False,
                "text": "Hello, thank you for calling. Sorry, we're closed today.",
            },
            {
                "description": "Closed on New Year's Day",
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
                "invert": False,
                "text": "Hello, thank you for calling. Sorry, we're closed today.",
            },
        ],
        "id": 1,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CustomMessageUpdateRequest](../../models/custommessageupdaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CustomMessageResponse](../../models/custommessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Get the custom message by its ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.custom_messages.get_by_id(custom_message_id=931598)

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