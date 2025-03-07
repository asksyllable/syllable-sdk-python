# SessionLabels
(*session_labels*)

## Overview

### Available Operations

* [get](#get) - Get Label By Id
* [create](#create) - Create Label
* [list](#list) - Session Labels List

## get

Get Label By Id

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.session_labels.get(session_label_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_label_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SessionLabel](../../models/sessionlabel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new label

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.session_labels.create(session_id=486589, type_="auto-rating", code="BAD", user_email="<value>", issue_categories=[
        "Silent treatment",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The internal ID of the session (see Session.session_id)             |                                                                     |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The type of the label                                               | auto-rating                                                         |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | A code describing the quality of the labeled session                | GOOD                                                                |
| `user_email`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The email of the user who created the label                         |                                                                     |
| `comments`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Comment string describing additional details about the session      |                                                                     |
| `issue_categories`                                                  | List[*str*]                                                         | :heavy_minus_sign:                                                  | Descriptions of issues occurring in the labeled call                | [<br/>"Silent treatment"<br/>]                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SessionLabel](../../models/sessionlabel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

Session Labels List

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.session_labels.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `page`                                                                                    | *OptionalNullable[int]*                                                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `search_fields`                                                                           | List[[models.SessionLabelProperties](../../models/sessionlabelproperties.md)]             | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `search_field_values`                                                                     | List[*str*]                                                                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `order_by`                                                                                | [OptionalNullable[models.SessionLabelProperties]](../../models/sessionlabelproperties.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `order_by_direction`                                                                      | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)             | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `fields`                                                                                  | List[[models.SessionLabelProperties](../../models/sessionlabelproperties.md)]             | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `start_datetime`                                                                          | *OptionalNullable[str]*                                                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `end_datetime`                                                                            | *OptionalNullable[str]*                                                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.ListResponseSessionLabel](../../models/listresponsesessionlabel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |