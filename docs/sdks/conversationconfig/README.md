# ConversationConfig

## Overview

### Available Operations

* [get_bridge_phrases_config](#get_bridge_phrases_config) - Get Bridge Phrases Config
* [update_bridge_phrases_config](#update_bridge_phrases_config) - Update Bridge Phrases Config

## get_bridge_phrases_config

Get the bridge phrases configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_bridge_phrases_config" method="get" path="/api/v1/conversation-config/bridges" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.conversation_config.get_bridge_phrases_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Agent ID to fetch config for                                        |
| `tool_name`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Tool name to fetch config for                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BridgePhrasesConfig](../../models/bridgephrasesconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_bridge_phrases_config

Update the bridge phrases configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_bridge_phrases_config" method="put" path="/api/v1/conversation-config/bridges" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.conversation_config.update_bridge_phrases_config(bridge_phrases_config={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bridge_phrases_config`                                             | [models.BridgePhrasesConfig](../../models/bridgephrasesconfig.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `agent_id`                                                          | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Agent ID to update config for                                       |
| `tool_name`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Tool name to update config for                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BridgePhrasesConfig](../../models/bridgephrasesconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |