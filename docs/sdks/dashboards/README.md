# Dashboards
(*dashboards*)

## Overview

Operations related to dashboards. Currently the API/SDK           only supports fetching basic information about dashboards.

### Available Operations

* [list](#list) - Post List Dashboards
* [fetch_info](#fetch_info) - Post Fetch Info
* [~~session_events~~](#session_events) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary~~](#post_session_summary) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers~~](#post_session_transfers) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions~~](#post_sessions) - Post Sessions :warning: **Deprecated**

## list

METHOD: POST
URL: /dashboard/list
ARGUMENTS: None
RETURNS: List of dashboards

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `page`                                                                              | *OptionalNullable[int]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `search_fields`                                                                     | List[[models.DashboardProperties](../../models/dashboardproperties.md)]             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `search_field_values`                                                               | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `order_by`                                                                          | [OptionalNullable[models.DashboardProperties]](../../models/dashboardproperties.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `order_by_direction`                                                                | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)       | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `fields`                                                                            | List[[models.DashboardProperties](../../models/dashboardproperties.md)]             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `start_datetime`                                                                    | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `end_datetime`                                                                      | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ListResponseDashboardResponse](../../models/listresponsedashboardresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## fetch_info

METHOD: POST
URL: /dashboard/fetch_info
ARGUMENTS: None
RETURNS: Dashboard info for embedding

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.fetch_info(dashboard_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dashboard_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardTokenResponse](../../models/dashboardtokenresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## ~~session_events~~

METHOD: POST
URL: /dashboard/session_events
ARGUMENTS: None
RETURNS: Dashboard info for embedding
DEPRECATED: This endpoint is deprecated. Please use /dashboard/list instead

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.session_events()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Dashboard](../../models/dashboard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~post_session_summary~~

METHOD: POST
URL: /dashboard/session_summary
ARGUMENTS: None
RETURNS: Dashboard info for embedding
DEPRECATED: This endpoint is deprecated. Please use /dashboard/list instead

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.post_session_summary()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Dashboard](../../models/dashboard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~post_session_transfers~~

METHOD: POST
URL: /dashboard/session_transfers
ARGUMENTS: None
RETURNS: Dashboard info for embedding
DEPRECATED: This endpoint is deprecated. Please use /dashboard/list instead

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.post_session_transfers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Dashboard](../../models/dashboard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~post_sessions~~

METHOD: POST
URL: /dashboard/sessions
ARGUMENTS: None
RETURNS: Dashboard info for embedding
DEPRECATED: This endpoint is deprecated. Please use /dashboard/list instead

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.dashboards.post_sessions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Dashboard](../../models/dashboard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |