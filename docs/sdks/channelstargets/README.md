# ChannelsTargets
(*channels_targets*)

## Overview

### Available Operations

* [list_available](#list_available) - Available Targets List

## list_available

List the available phone numbers

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels_targets.list_available()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `page`                                                                                          | *OptionalNullable[int]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `limit`                                                                                         | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_fields`                                                                                 | List[[models.AvailableTargetProperties](../../models/availabletargetproperties.md)]             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_field_values`                                                                           | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `order_by`                                                                                      | [OptionalNullable[models.AvailableTargetProperties]](../../models/availabletargetproperties.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `order_by_direction`                                                                            | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                   | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `fields`                                                                                        | List[[models.AvailableTargetProperties](../../models/availabletargetproperties.md)]             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `start_datetime`                                                                                | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `end_datetime`                                                                                  | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.ListResponseAvailableTarget](../../models/listresponseavailabletarget.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |