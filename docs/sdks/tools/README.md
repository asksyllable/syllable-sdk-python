# Tools
(*tools*)

## Overview

Operations related to tool configuration. A tool is a function that an           agent can call to perform actions like accessing databases, making API calls, or           processing data. For an agent to have access to a tool, the prompt associated with that           agent should be linked to the tool and include instructions to use it.

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
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.tools.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `page`                                                                        | *OptionalNullable[int]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `search_fields`                                                               | List[[models.ToolProperties](../../models/toolproperties.md)]                 | :heavy_minus_sign:                                                            | N/A                                                                           |
| `search_field_values`                                                         | List[*str*]                                                                   | :heavy_minus_sign:                                                            | N/A                                                                           |
| `order_by`                                                                    | [OptionalNullable[models.ToolProperties]](../../models/toolproperties.md)     | :heavy_minus_sign:                                                            | N/A                                                                           |
| `order_by_direction`                                                          | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md) | :heavy_minus_sign:                                                            | N/A                                                                           |
| `fields`                                                                      | List[[models.ToolProperties](../../models/toolproperties.md)]                 | :heavy_minus_sign:                                                            | N/A                                                                           |
| `start_datetime`                                                              | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `end_datetime`                                                                | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

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

    res = ss_client.tools.create(name="Weather Fetcher", definition={
        "tool": {
            "function": {
                "name": "weather_fetcher",
                "description": "Fetches weather data",
                "parameters": {

                },
            },
            "type": "function",
        },
        "endpoint": {
            "url": "https://api.example.com",
            "method": syllable_sdk.ToolHTTPMethod.GET,
            "argument_location": syllable_sdk.ToolArgumentLocation.PATH,
        },
        "defaults": "<value>",
    }, service_id=134365)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                       | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The name of the tool                                                                                         | Weather Fetcher                                                                                              |
| `definition`                                                                                                 | [models.ToolDefinition](../../models/tooldefinition.md)                                                      | :heavy_check_mark:                                                                                           | A tool that can be called from an LLM during the conversation. See https://docs.syllable.ai/Resources/Tools. |                                                                                                              |
| `service_id`                                                                                                 | *int*                                                                                                        | :heavy_check_mark:                                                                                           | The service to which this tool belongs                                                                       |                                                                                                              |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

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

    res = ss_client.tools.update(name="Weather Fetcher", definition={
        "tool": {
            "function": {
                "name": "weather_fetcher",
                "description": "Fetches weather data",
                "parameters": {

                },
            },
            "type": "function",
        },
        "endpoint": {
            "url": "https://api.example.com",
            "method": syllable_sdk.ToolHTTPMethod.POST,
            "argument_location": syllable_sdk.ToolArgumentLocation.PATH,
        },
        "defaults": "<value>",
    }, service_id=991464, id=627690)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                       | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The name of the tool                                                                                         | Weather Fetcher                                                                                              |
| `definition`                                                                                                 | [models.ToolDefinition](../../models/tooldefinition.md)                                                      | :heavy_check_mark:                                                                                           | A tool that can be called from an LLM during the conversation. See https://docs.syllable.ai/Resources/Tools. |                                                                                                              |
| `service_id`                                                                                                 | *int*                                                                                                        | :heavy_check_mark:                                                                                           | The service to which this tool belongs                                                                       |                                                                                                              |
| `id`                                                                                                         | *int*                                                                                                        | :heavy_check_mark:                                                                                           | The ID of the tool                                                                                           |                                                                                                              |
| `last_updated_comments`                                                                                      | *OptionalNullable[str]*                                                                                      | :heavy_minus_sign:                                                                                           | Update comments                                                                                              |                                                                                                              |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

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