# InsightsSyllableSDKTools
(*insights.tools*)

## Overview

Operations related to insights tools. An insight is a tool that processes           conversation data to extract information and generate reports.

### Available Operations

* [create](#create) - Create Insight Tool
* [get_definitions](#get_definitions) - Get Insight Tool Definitions

## create

Create a new tool in the insights

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.tools.create(name="<value>", description="yuck vice between gee ugh ha", version=920994, tool_arguments={}, insight_tool_definition_id=780486)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
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

## get_definitions

Get a InsightTool by Name.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.tools.get_definitions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.InsightToolDefinition]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |