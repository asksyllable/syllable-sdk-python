# Incidents
(*incidents*)

## Overview

Operations related to incidents.

### Available Operations

* [list](#list) - List Incidents
* [create](#create) - Create Incident
* [update](#update) - Update Incident
* [incident_get_organizations](#incident_get_organizations) - Get Organizations
* [get_by_id](#get_by_id) - Get Incident By Id
* [delete](#delete) - Delete Incident

## list

List service incidents with pagination and filtering

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.list(page=0, limit=25, search_fields=[
        syllable_sdk.IncidentProperties.UPDATED_AT,
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
| `search_fields`                                                                                                                                        | List[[models.IncidentProperties](../../models/incidentproperties.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.IncidentProperties]](../../models/incidentproperties.md)                                                                      | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.IncidentProperties](../../models/incidentproperties.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseIncidentResponse](../../models/listresponseincidentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new incident

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import parse_datetime


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.create(request={
        "description": "Service outage in region X",
        "start_datetime": parse_datetime("2023-10-01T08:00:00Z"),
        "resolution_datetime": parse_datetime("2023-10-01T12:00:00Z"),
        "impact_category": "High",
        "sessions_impacted": 1500,
        "markdown": "**Incident Details**",
        "organization_id": 123,
        "sub_organization_id": 456,
        "sub_organization": "SubOrg A",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.IncidentCreateRequest](../../models/incidentcreaterequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.IncidentResponse](../../models/incidentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing incident

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import parse_datetime


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.update(request={
        "description": "Service outage in region X",
        "start_datetime": parse_datetime("2023-10-01T08:00:00Z"),
        "resolution_datetime": parse_datetime("2023-10-01T12:00:00Z"),
        "impact_category": "High",
        "sessions_impacted": 1500,
        "markdown": "**Incident Details**",
        "organization_id": 123,
        "sub_organization_id": 456,
        "sub_organization": "SubOrg A",
        "id": 1,
        "created_at": parse_datetime("2023-10-01T08:00:00Z"),
        "updated_at": parse_datetime("2023-10-01T08:00:00Z"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.IncidentUpdateRequest](../../models/incidentupdaterequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.IncidentResponse](../../models/incidentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## incident_get_organizations

Get all organizations

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.incident_get_organizations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.IncidentOrganizationResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_by_id

Get incident by ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.get_by_id(incident_id=835824)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentResponse](../../models/incidentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete an incident by ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.incidents.delete(incident_id=400877, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |