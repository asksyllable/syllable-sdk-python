# Tools
(*tools*)

## Overview

Operations related to tool configuration. A tool is a function that an           agent can call to perform actions like accessing databases, making API calls, or           processing data. For an agent to have access to a tool, the prompt associated with that           agent should be linked to the tool and include instructions to use it. For more           information, see [Console docs](https://docs.syllable.ai/Resources/Tools).

### Available Operations

* [list](#list) - Tool List
* [create](#create) - Create Tool
* [update](#update) - Update Tool
* [get_by_name](#get_by_name) - Tool Info
* [delete](#delete) - Delete Tool

## list

List the existing tools

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.list(page=0, limit=25, search_fields=[
        syllable_sdk.ToolProperties.NAME,
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
| `search_fields`                                                                                                                                        | List[[models.ToolProperties](../../models/toolproperties.md)]                                                                                          | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.ToolProperties]](../../models/toolproperties.md)                                                                              | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.ToolProperties](../../models/toolproperties.md)]                                                                                          | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseToolResponse](../../models/listresponsetoolresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new tool

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.create(request={
        "name": "Weather Fetcher",
        "definition": {
            "type": syllable_sdk.Type.ENDPOINT,
            "tool": {
                "function": {
                    "name": "get_weather",
                    "description": "Get the weather for a city",
                    "parameters": {

                    },
                },
            },
            "endpoint": {
                "url": "https://api.example.com",
                "method": syllable_sdk.ToolHTTPMethod.POST,
                "argument_location": syllable_sdk.ToolArgumentLocation.QUERY,
            },
            "defaults": {
                "key": {
                    "transform": {
                        "action": "default",
                        "when": {
                            "key": "key",
                            "value": "value",
                            "operator": "eq",
                        },
                    },
                },
            },
            "static_parameters": [
                {
                    "name": "temperature_unit",
                    "description": "Whether the temperature information should be fetched in Celsius or Fahrenheit",
                    "required": False,
                    "type": syllable_sdk.StaticToolParameterType.STRING,
                    "default": "fahrenheit",
                },
            ],
        },
        "service_id": 1,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ToolCreateRequest](../../models/toolcreaterequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolResponse](../../models/toolresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing tool

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.update(request={
        "name": "Weather Fetcher",
        "definition": {
            "type": syllable_sdk.Type.ENDPOINT,
            "tool": {
                "function": {
                    "name": "get_weather",
                    "description": "Get the weather for a city",
                    "parameters": {

                    },
                },
            },
            "endpoint": {
                "url": "https://api.example.com",
                "method": syllable_sdk.ToolHTTPMethod.GET,
                "argument_location": syllable_sdk.ToolArgumentLocation.FORM,
            },
            "defaults": "<value>",
            "static_parameters": [
                {
                    "name": "temperature_unit",
                    "description": "Whether the temperature information should be fetched in Celsius or Fahrenheit",
                    "required": False,
                    "type": syllable_sdk.StaticToolParameterType.STRING,
                    "default": "fahrenheit",
                },
            ],
        },
        "service_id": 1,
        "id": 1,
        "last_updated_comments": "Updated to use new API endpoint",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ToolUpdateRequest](../../models/toolupdaterequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolResponse](../../models/toolresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_name

Get the details of a specific tool

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.get_by_name(tool_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolDetailResponse](../../models/tooldetailresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a tool.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.delete(tool_name="<value>", reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |