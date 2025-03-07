# Channels
(*channels*)

## Overview

Operations related to channel configuration.           A channel is an organization-level point of communication, like a phone number or a web           chat. A channel can be associated with an agent by creating a channel target linking           them.

### Available Operations

* [list](#list) - Get Channels
* [list_targets](#list_targets) - Get Channel Targets
* [assign_target](#assign_target) - Assign A Channel Target
* [delete](#delete) - Delete Channel Target

## list

Get Channels

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `page`                                                                          | *OptionalNullable[int]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_fields`                                                                 | List[[models.ChannelProperties](../../models/channelproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search_field_values`                                                           | List[*str*]                                                                     | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by`                                                                      | [OptionalNullable[models.ChannelProperties]](../../models/channelproperties.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `order_by_direction`                                                            | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)   | :heavy_minus_sign:                                                              | N/A                                                                             |
| `fields`                                                                        | List[[models.ChannelProperties](../../models/channelproperties.md)]             | :heavy_minus_sign:                                                              | N/A                                                                             |
| `start_datetime`                                                                | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `end_datetime`                                                                  | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ListResponseChannel](../../models/listresponsechannel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_targets

Get Channel Targets

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.list_targets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `page`                                                                                      | *OptionalNullable[int]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_fields`                                                                             | List[[models.ChannelTargetProperties](../../models/channeltargetproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `search_field_values`                                                                       | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by`                                                                                  | [OptionalNullable[models.ChannelTargetProperties]](../../models/channeltargetproperties.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `order_by_direction`                                                                        | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)               | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `fields`                                                                                    | List[[models.ChannelTargetProperties](../../models/channeltargetproperties.md)]             | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `start_datetime`                                                                            | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `end_datetime`                                                                              | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListResponseChannelTargetResponse](../../models/listresponsechanneltargetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## assign_target

Assign A Channel Target

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.assign_target(channel_id_param=134365, agent_id=486589, channel_id=638424, target="<value>", target_mode=syllable_sdk.TargetModes.CHAT)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `channel_id_param`                                                                                                             | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | N/A                                                                                                                            |
| `agent_id`                                                                                                                     | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | The ID of the agent associated with the channel target                                                                         |
| `channel_id`                                                                                                                   | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | The ID of the channel associated with the channel target                                                                       |
| `target`                                                                                                                       | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | The name of the channel target (must correspond to an organization-level target)                                               |
| `target_mode`                                                                                                                  | [models.TargetModes](../../models/targetmodes.md)                                                                              | :heavy_check_mark:                                                                                                             | Available modes (communication methods) for channel targets.                                                                   |
| `fallback_target`                                                                                                              | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The fallback for the channel target (currently only supported for "voice" mode)                                                |
| `is_test`                                                                                                                      | *Optional[bool]*                                                                                                               | :heavy_minus_sign:                                                                                                             | Whether the channel target is intended for testing. If true, any sessions created through this target will be labeled as test. |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.ChannelTargetResponse](../../models/channeltargetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Hard-delete a channel target by ID

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.delete(channel_id="<id>", target_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `channel_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `target_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |