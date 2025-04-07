# InsightsSDK
(*insights*)

## Overview

Operations related to insights results. An insight is a tool that processes          conversation data to extract information and generate reports.

### Available Operations

* [list](#list) - Insights List

## list

List the evaluated insights for sessions.

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.list(page=0, search_fields=[
        syllable_sdk.InsightsProperties.INSIGHT_TOOL_ID,
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
| `search_fields`                                                                                                                                        | List[[models.InsightsProperties](../../models/insightsproperties.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.InsightsProperties]](../../models/insightsproperties.md)                                                                      | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.InsightsProperties](../../models/insightsproperties.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseInsightsOutput](../../models/listresponseinsightsoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |