# InsightsWorkflows
(*insights_workflows*)

## Overview

### Available Operations

* [list](#list) - Insight Workflow List
* [create](#create) - Create Insight Workflow
* [get](#get) - Get Insight Workflow By Id
* [delete](#delete) - Delete Insights Workflow

## list

List the existing insight_workflows

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_workflows.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `page`                                                                                          | *OptionalNullable[int]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `limit`                                                                                         | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_fields`                                                                                 | List[[models.InsightWorkflowProperties](../../models/insightworkflowproperties.md)]             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_field_values`                                                                           | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `order_by`                                                                                      | [OptionalNullable[models.InsightWorkflowProperties]](../../models/insightworkflowproperties.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `order_by_direction`                                                                            | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                   | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `fields`                                                                                        | List[[models.InsightWorkflowProperties](../../models/insightworkflowproperties.md)]             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `start_datetime`                                                                                | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `end_datetime`                                                                                  | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.ListResponseInsightWorkflowOutput](../../models/listresponseinsightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new tool in the insights

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_workflows.create(name="<value>", description="yuck vice between gee ugh ha", insight_tool_ids=[
        780486,
        760259,
        219974,
    ], conditions={}, status="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | Human readable name of Insight Workflow                                                 |
| `description`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Text description of Insight Workflow                                                    |
| `insight_tool_ids`                                                                      | List[*int*]                                                                             | :heavy_check_mark:                                                                      | List of Insight Tool IDs                                                                |
| `conditions`                                                                            | [models.InsightWorkflowInputConditions](../../models/insightworkflowinputconditions.md) | :heavy_check_mark:                                                                      | Conditions for Insight Workflow                                                         |
| `status`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | Status of the Insight Workflow                                                          |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.InsightWorkflowOutput](../../models/insightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a InsightWorkflow by ID.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_workflows.get(workflow_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsightWorkflowOutput](../../models/insightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a Insights workflow.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights_workflows.delete(workflow_id=545907)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |