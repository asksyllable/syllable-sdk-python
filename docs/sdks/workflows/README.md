# Workflows
(*insights.workflows*)

## Overview

Operations related to insights workflows. An workflow is series of tool           invocations that processes conversation data to extract information and generate           reports.

### Available Operations

* [list](#list) - Insight Workflow List
* [create](#create) - Create Insight Workflow
* [get_by_id](#get_by_id) - Get Insight Workflow By Id
* [update](#update) - Update Insights Workflow
* [delete](#delete) - Delete Insights Workflow
* [inactivate](#inactivate) - Inactivate Insights Workflow
* [activate](#activate) - Activate Insights Workflow
* [queue_work](#queue_work) - Queue Insights Workflow For Sessions/Files

## list

List the existing insight_workflows

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_list" method="get" path="/api/v1/insights/workflows/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.list(page=0, limit=25, search_fields=[
        models.InsightWorkflowProperties.NAME,
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
| `search_fields`                                                                                                                                        | List[[models.InsightWorkflowProperties](../../models/insightworkflowproperties.md)]                                                                    | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.InsightWorkflowProperties]](../../models/insightworkflowproperties.md)                                                        | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.InsightWorkflowProperties](../../models/insightworkflowproperties.md)]                                                                    | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseInsightWorkflowOutput](../../models/listresponseinsightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new tool in the insights

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_create" method="post" path="/api/v1/insights/workflows/" -->
```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import parse_datetime


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.create(request={
        "name": "summary-workflow",
        "source": "agent",
        "description": "Default workflow - generates a summary of the call",
        "insight_tool_ids": [
            1,
        ],
        "conditions": {
            "min_duration": 120,
            "max_duration": 600,
            "sample_rate": 0.1,
            "agent_list": [
                866324,
                826325,
            ],
            "prompt_list": [
                "123324",
            ],
            "folder_list": [
                16754,
                67535,
            ],
            "sheet_info": {
                "sheet_id": "1AGOCYz05AZYYOMzow2EYlgdDXSXaWIhyA3-zCxBm4go",
                "sheet_name": "Q1 Sales Data",
            },
        },
        "start_datetime": parse_datetime("2025-10-22T00:00:00Z"),
        "end_datetime": parse_datetime("2025-10-23T00:00:00Z"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.InsightWorkflowInput](../../models/insightworkflowinput.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsightWorkflowOutput](../../models/insightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Get a InsightWorkflow by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_get_by_id" method="get" path="/api/v1/insights/workflows/{workflow_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.get_by_id(workflow_id=788857)

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
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a InsightWorkflow.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_update" method="put" path="/api/v1/insights/workflows/{workflow_id}" -->
```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import parse_datetime


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.update(workflow_id=766381, insight_workflow_input={
        "name": "summary-workflow",
        "source": "agent",
        "description": "Default workflow - generates a summary of the call",
        "insight_tool_ids": [
            1,
        ],
        "conditions": {
            "min_duration": 120,
            "max_duration": 600,
            "sample_rate": 0.1,
            "agent_list": [
                866324,
                826325,
            ],
            "prompt_list": [
                "123324",
            ],
            "folder_list": [
                16754,
                67535,
            ],
            "sheet_info": {
                "sheet_id": "1AGOCYz05AZYYOMzow2EYlgdDXSXaWIhyA3-zCxBm4go",
                "sheet_name": "Q1 Sales Data",
            },
        },
        "start_datetime": parse_datetime("2025-10-22T00:00:00Z"),
        "end_datetime": parse_datetime("2025-10-23T00:00:00Z"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `insight_workflow_input`                                            | [models.InsightWorkflowInput](../../models/insightworkflowinput.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsightWorkflowOutput](../../models/insightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete an Insights workflow.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_delete" method="delete" path="/api/v1/insights/workflows/{workflow_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.delete(workflow_id=609419)

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
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## inactivate

Inactivate an InsightWorkflow.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_inactivate" method="put" path="/api/v1/insights/workflows/{workflow_id}/inactivate" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.inactivate(workflow_id=248768)

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
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## activate

Activate an InsightWorkflow.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_activate" method="put" path="/api/v1/insights/workflows/{workflow_id}/activate" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.activate(workflow_id=303095, insight_workflow_activate={
        "is_acknowledged": True,
        "estimate": {
            "backfill_count": 100,
            "backfill_duration": 1000,
            "estimated_daily_count": 10,
            "estimated_daily_duration": 3674.11,
            "estimated_daily_cost": 45.25,
            "estimated_backfill_cost": 4561,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `workflow_id`                                                             | *int*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `insight_workflow_activate`                                               | [models.InsightWorkflowActivate](../../models/insightworkflowactivate.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.InsightWorkflowOutput](../../models/insightworkflowoutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## queue_work

Manually queue sessions for insights workflow evaluation.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights_workflow_queue_work" method="post" path="/api/v1/insights/workflows/queue-work" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.queue_work(request={
        "workflow_name": "summary-workflow",
        "session_id_list": [
            12334,
            23445,
            34556,
        ],
        "file_id_list": [
            1234,
            1678,
            2224,
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.InsightsWorkflowQueueSession](../../models/insightsworkflowqueuesession.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |