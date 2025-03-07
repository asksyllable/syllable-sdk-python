# InsightsTools
(*insights_tools*)

## Overview

### Available Operations

* [list](#list) - Insight Tool List
* [get](#get) - Get Insight Tool By Id
* [update](#update) - Update Insights Tool

## list

List the existing insight_tools

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_tools.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `page`                                                                                  | *OptionalNullable[int]*                                                                 | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `search_fields`                                                                         | List[[models.InsightToolProperties](../../models/insighttoolproperties.md)]             | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `search_field_values`                                                                   | List[*str*]                                                                             | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `order_by`                                                                              | [OptionalNullable[models.InsightToolProperties]](../../models/insighttoolproperties.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `order_by_direction`                                                                    | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `fields`                                                                                | List[[models.InsightToolProperties](../../models/insighttoolproperties.md)]             | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `start_datetime`                                                                        | *OptionalNullable[str]*                                                                 | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `end_datetime`                                                                          | *OptionalNullable[str]*                                                                 | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ListResponseInsightToolOutput](../../models/listresponseinsighttooloutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a InsightTool by Name.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_tools.get(tool_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsightToolOutput](../../models/insighttooloutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a InsightTool.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_tools.update(tool_id=198183, name="<value>", description="awful underneath retention too mobility char innocently dowse restfully", version=243447, tool_arguments={}, insight_tool_definition_id=265006)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `tool_id`                                                                             | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `name`                                                                                | *str*                                                                                 | :heavy_check_mark:                                                                    | Human readable name of Insight Tool                                                   |
| `description`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Text description of Insight Tool                                                      |
| `version`                                                                             | *int*                                                                                 | :heavy_check_mark:                                                                    | Version number of Insight Tool                                                        |
| `tool_arguments`                                                                      | [models.InsightToolInputToolArguments](../../models/insighttoolinputtoolarguments.md) | :heavy_check_mark:                                                                    | Arguments for Insight Tool                                                            |
| `insight_tool_definition_id`                                                          | *int*                                                                                 | :heavy_check_mark:                                                                    | Unique ID for Insight Tool Definition                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.InsightToolOutput](../../models/insighttooloutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |