# Workflows
(*insights.workflows*)

## Overview

Operations related to insights workflows. An workflow is series of tool           invocations that processes conversation data to extract information and generate reports.

### Available Operations

* [update](#update) - Update Insights Workflow

## update

Update a InsightWorkflow.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.workflows.update(workflow_id=265006, name="<value>", description="awful underneath retention too mobility char innocently dowse restfully", insight_tool_ids=[

    ], conditions={}, status="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `workflow_id`                                                                           | *int*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
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