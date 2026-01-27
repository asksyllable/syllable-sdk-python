# InsightsWorkflowQueueSession

Session identifier for workflow queue.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `workflow_name`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | Unique name for workflow                                                     | summary-workflow                                                             |
| `session_id_list`                                                            | List[*int*]                                                                  | :heavy_minus_sign:                                                           | List of session identifiers                                                  |                                                                              |
| `file_id_list`                                                               | List[*int*]                                                                  | :heavy_minus_sign:                                                           | List of file IDs to be processed. This is only applicable for upload folders |                                                                              |