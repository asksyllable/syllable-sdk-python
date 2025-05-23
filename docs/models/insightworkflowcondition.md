# InsightWorkflowCondition

Model for the conditions that trigger an insight workflow.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `min_duration`                                               | *OptionalNullable[int]*                                      | :heavy_minus_sign:                                           | Minimum duration of the calls in seconds                     | 120                                                          |
| `max_duration`                                               | *OptionalNullable[int]*                                      | :heavy_minus_sign:                                           | Maximum duration of the calls in seconds                     | 600                                                          |
| `sample_rate`                                                | *OptionalNullable[int]*                                      | :heavy_minus_sign:                                           | Sample rate as a percentage of calls                         | 2                                                            |
| `agent_list`                                                 | [OptionalNullable[models.AgentList]](../models/agentlist.md) | :heavy_minus_sign:                                           | List of agent IDs                                            | [<br/>"866324",<br/>"826325"<br/>]                           |
| `prompt_list`                                                | List[*str*]                                                  | :heavy_minus_sign:                                           | List of prompts IDs                                          | [<br/>"123324"<br/>]                                         |
| `folder_list`                                                | List[*int*]                                                  | :heavy_minus_sign:                                           | List of folder IDs                                           | [<br/>16754,<br/>67535<br/>]                                 |