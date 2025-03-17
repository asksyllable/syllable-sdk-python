# DataSources
(*data_sources*)

## Overview

### Available Operations

* [list](#list) - List Data Sources
* [create](#create) - Create Data Source
* [update](#update) - Update Data Source
* [get](#get) - Get Data Source
* [delete](#delete) - Delete Data Source

## list

Fetch metadata about all data sources, not including their text.

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.data_sources.list(page=0, search_fields=[
        syllable_sdk.DataSourceProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            | Example                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The page number from which to start (0-indexed)                                                                                                        | 0                                                                                                                                                      |
| `limit`                                                                                                                                                | *Optional[int]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | The maximum number of items to return                                                                                                                  | 25                                                                                                                                                     |
| `search_fields`                                                                                                                                        | List[[models.DataSourceProperties](../../models/datasourceproperties.md)]                                                                              | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.DataSourceProperties]](../../models/datasourceproperties.md)                                                                  | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.DataSourceProperties](../../models/datasourceproperties.md)]                                                                              | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseDataSourceMetadataResponse](../../models/listresponsedatasourcemetadataresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new data source.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.data_sources.create(name="Rain", chunk=False, text="<value>", description="Information about rain.", labels=[
        "Weather Info",
    ], chunk_delimiter="")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              | Example                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The data source name. Must be unique within suborg. Cannot contain whitespace.                                                                                                           | Rain                                                                                                                                                                                     |
| `chunk`                                                                                                                                                                                  | *bool*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                       | Whether the content should be split into smaller chunks. (This feature is coming in the future - currently this value will always be treated as False.)                                  | false                                                                                                                                                                                    |
| `text`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Information that the data source will provide to the agent accessing it.                                                                                                                 |                                                                                                                                                                                          |
| `description`                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                       | The description of the data source.                                                                                                                                                      | Information about rain.                                                                                                                                                                  |
| `labels`                                                                                                                                                                                 | List[*str*]                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                       | Searchable labels for the data source. Can be included in agent.prompt_tool_defaults for a given tool to give the agent access to data sources with those labels when calling that tool. | [<br/>"Weather Info"<br/>]                                                                                                                                                               |
| `chunk_delimiter`                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                       | String that should be treated as delimiter between intended chunks. (This feature is coming in the future - currently this value will always be treated as None.)                        |                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |                                                                                                                                                                                          |

### Response

**[models.DataSourceDetailResponse](../../models/datasourcedetailresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing data source.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.data_sources.update(name="Rain", chunk=False, id=1, text="<value>", description="Information about rain.", labels=[
        "Weather Info",
    ], chunk_delimiter="", edit_comments="Added new info")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              | Example                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The data source name. Must be unique within suborg. Cannot contain whitespace.                                                                                                           | Rain                                                                                                                                                                                     |
| `chunk`                                                                                                                                                                                  | *bool*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                       | Whether the content should be split into smaller chunks. (This feature is coming in the future - currently this value will always be treated as False.)                                  | false                                                                                                                                                                                    |
| `id`                                                                                                                                                                                     | *int*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The data source ID.                                                                                                                                                                      | 1                                                                                                                                                                                        |
| `text`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Information that the data source will provide to the agent accessing it.                                                                                                                 |                                                                                                                                                                                          |
| `description`                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                       | The description of the data source.                                                                                                                                                      | Information about rain.                                                                                                                                                                  |
| `labels`                                                                                                                                                                                 | List[*str*]                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                       | Searchable labels for the data source. Can be included in agent.prompt_tool_defaults for a given tool to give the agent access to data sources with those labels when calling that tool. | [<br/>"Weather Info"<br/>]                                                                                                                                                               |
| `chunk_delimiter`                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                       | String that should be treated as delimiter between intended chunks. (This feature is coming in the future - currently this value will always be treated as None.)                        |                                                                                                                                                                                          |
| `edit_comments`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                       | The comments for the most recent edit to the data source                                                                                                                                 | Added new info                                                                                                                                                                           |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |                                                                                                                                                                                          |

### Response

**[models.DataSourceDetailResponse](../../models/datasourcedetailresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Fetch a given data source, including its text.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.data_sources.get(data_source_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data_source_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DataSourceDetailResponse](../../models/datasourcedetailresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a given data source.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.data_sources.delete(data_source_id=545907, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data_source_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |