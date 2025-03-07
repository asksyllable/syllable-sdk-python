# Services
(*services*)

## Overview

Operations related to service configuration. A service is a collection of           tools.

### Available Operations

* [list](#list) - Service List
* [create](#create) - Create Service
* [update](#update) - Update Service
* [get](#get) - Get Service By Id
* [delete](#delete) - Delete Service

## list

List the existing services

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.services.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `page`                                                                          | *OptionalNullable[int]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_fields`                                                                 | List[[models.ServiceProperties](../../models/serviceproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_field_values`                                                           | List[*str*]                                                                     | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by`                                                                      | [OptionalNullable[models.ServiceProperties]](../../models/serviceproperties.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by_direction`                                                            | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)   | :heavy_minus_sign:                                                              | N/A                                                                             |
| `fields`                                                                        | List[[models.ServiceProperties](../../models/serviceproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `start_datetime`                                                                | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `end_datetime`                                                                  | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ListResponseServiceResponse](../../models/listresponseserviceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new service.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.services.create(name="<value>", description="yuck vice between gee ugh ha")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the service                                             |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The description of the service                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServiceResponse](../../models/serviceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing service.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.services.update(name="<value>", description="awful underneath retention too mobility char innocently dowse restfully", id=243447)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the service                                             |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The description of the service                                      |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the service                                               |
| `last_updated_comments`                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Update comments                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServiceResponse](../../models/serviceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a service by its ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.services.get(service_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServiceResponse](../../models/serviceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a service. A service with linked tools cannot be deleted.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.services.delete(service_id=545907, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |