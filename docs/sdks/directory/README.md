# Directory

## Overview

Operations related to directory

### Available Operations

* [list](#list) - Directory Member List
* [create](#create) - Create Directory Member
* [directory_member_history](#directory_member_history) - Get Directory Member History
* [get_by_id](#get_by_id) - Get Directory Member By Id
* [update](#update) - Update Directory Member
* [delete](#delete) - Delete Directory Member
* [directory_member_test_extension](#directory_member_test_extension) - Test Directory Member Extension
* [directory_member_restore](#directory_member_restore) - Restore Directory Member
* [directory_member_bulk_load](#directory_member_bulk_load) - Bulk Load Directory Members
* [directory_member_download](#directory_member_download) - Download Directory Members

## list

List the directory_members

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_list" method="get" path="/api/v1/directory_members/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.list(include_deleted=False, page=0, limit=25, search_fields=[
        models.DirectoryMemberProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `include_deleted`                                                                                                  | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | If true, include soft-deleted members in the list. Default excludes them.                                          |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `page`                                                                                                             | *OptionalNullable[int]*                                                                                            | :heavy_minus_sign:                                                                                                 | Page number (0-based)                                                                                              |
| `limit`                                                                                                            | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Items per page                                                                                                     |
| `search_fields`                                                                                                    | List[[models.DirectoryMemberProperties](../../models/directorymemberproperties.md)]                                | :heavy_minus_sign:                                                                                                 | Fields to search; aligns with search_field_values                                                                  |
| `search_field_values`                                                                                              | List[*str*]                                                                                                        | :heavy_minus_sign:                                                                                                 | Values for search_fields in matching order                                                                         |
| `order_by`                                                                                                         | [OptionalNullable[models.DirectoryMemberProperties]](../../models/directorymemberproperties.md)                    | :heavy_minus_sign:                                                                                                 | Field to order results by                                                                                          |
| `order_by_direction`                                                                                               | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                      | :heavy_minus_sign:                                                                                                 | Direction to order results                                                                                         |
| `fields`                                                                                                           | List[[models.DirectoryMemberProperties](../../models/directorymemberproperties.md)]                                | :heavy_minus_sign:                                                                                                 | Fields to include in response                                                                                      |
| `start_datetime`                                                                                                   | *OptionalNullable[str]*                                                                                            | :heavy_minus_sign:                                                                                                 | Start datetime for filtering results                                                                               |
| `end_datetime`                                                                                                     | *OptionalNullable[str]*                                                                                            | :heavy_minus_sign:                                                                                                 | End datetime for filtering results                                                                                 |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.ListResponseDirectoryMember](../../models/listresponsedirectorymember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new member in the directory

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_create" method="post" path="/api/v1/directory_members/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.create(directory_member_create={
        "name": "Jane Doe",
        "type": "contact",
        "extensions": [
            {
                "name": "work",
                "numbers": [
                    {
                        "number": "+1234567890",
                        "rules": [
                            {
                                "language": "en",
                            },
                        ],
                    },
                ],
            },
        ],
        "contact_tags": {
            "tag1": [
                "value1",
            ],
            "tag2": [
                "value2",
            ],
        },
        "comments": "Updated to add new extension",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `directory_member_create`                                                                                          | [models.DirectoryMemberCreate](../../models/directorymembercreate.md)                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.DirectoryMember](../../models/directorymember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## directory_member_history

Get version history for a directory member (contact).
Version 1 is always the oldest; order_by_direction only controls response order.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_history" method="get" path="/api/v1/directory_members/{member_id}/history" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.directory_member_history(member_id=371893, page=0, limit=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `member_id`                                                                                                        | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `page`                                                                                                             | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Page number (0-based)                                                                                              |
| `limit`                                                                                                            | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Items per page                                                                                                     |
| `order_by_direction`                                                                                               | [Optional[models.OrderByDirection]](../../models/orderbydirection.md)                                              | :heavy_minus_sign:                                                                                                 | Sort by oldest first (asc) or newest first (desc). Version 1 is always the oldest.                                 |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.ListResponseDirectoryMemberHistoryResponse](../../models/listresponsedirectorymemberhistoryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Get a DirectoryMember by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_get_by_id" method="get" path="/api/v1/directory_members/{member_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.get_by_id(member_id=562571)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `member_id`                                                                                                        | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.DirectoryMember](../../models/directorymember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a DirectoryMember.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_update" method="put" path="/api/v1/directory_members/{member_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.update(member_id=941217, directory_member_update={
        "name": "Jane Doe",
        "type": "contact",
        "extensions": [
            {
                "name": "work",
                "numbers": [
                    {
                        "number": "+1234567890",
                        "rules": [
                            {
                                "language": "en",
                            },
                        ],
                    },
                ],
            },
        ],
        "contact_tags": {
            "tag1": [
                "value1",
            ],
            "tag2": [
                "value2",
            ],
        },
        "comments": "Updated phone number",
        "id": 1,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `member_id`                                                                                                        | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `directory_member_update`                                                                                          | [models.DirectoryMemberUpdate](../../models/directorymemberupdate.md)                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.DirectoryMember](../../models/directorymember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a DirectoryMember.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_delete" method="delete" path="/api/v1/directory_members/{member_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.delete(member_id=569311, comment="The Apollotech B340 is an affordable wireless mouse with reliable connectivity, 12 months battery life and modern design")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `member_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `comment`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Comment stored in version history for this deletion                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## directory_member_test_extension

Test directory member extension at a specific timestamp and language.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_test_extension" method="get" path="/api/v1/directory_members/{member_id}/test" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.directory_member_test_extension(member_id=922412, timestamp="2024-07-02T14:32:47.235Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `member_id`                                                           | *int*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `timestamp`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Timestamp for test in ISO 8601 format (e.g., 2025-12-04T14:29:39)     |
| `language_code`                                                       | [OptionalNullable[models.LanguageCode]](../../models/languagecode.md) | :heavy_minus_sign:                                                    | Optional language code for test                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.DirectoryMemberTestResponse](../../models/directorymembertestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## directory_member_restore

Restore a soft-deleted directory member.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_restore" method="put" path="/api/v1/directory_members/{member_id}/restore" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.directory_member_restore(member_id=507482, directory_member_restore={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `member_id`                                                                         | *int*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `directory_member_restore`                                                          | [models.DirectoryMemberRestore](../../models/directorymemberrestore.md)             | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `response_format`                                                                   | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md) | :heavy_minus_sign:                                                                  | Directory response format for the restored member.                                  |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DirectoryMember](../../models/directorymember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## directory_member_bulk_load

Update Directory Members in chunks of 100.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_bulk_load" method="put" path="/api/v1/directory_members/upload/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.directory_member_bulk_load(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.BodyDirectoryMemberBulkLoad](../../models/bodydirectorymemberbulkload.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## directory_member_download

Download the entire directory as a JSON file.

### Example Usage

<!-- UsageSnippet language="python" operationID="directory_member_download" method="get" path="/api/v1/directory_members/download/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.directory.directory_member_download()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `response_format`                                                                                                  | [Optional[models.DirectoryResponseFormat]](../../models/directoryresponseformat.md)                                | :heavy_minus_sign:                                                                                                 | Directory response format: normalized (default) strips @hours and formats times; raw returns stored @hours values. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |