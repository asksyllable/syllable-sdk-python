---
title: 'InternalTool'
---

A tool definition to be used by the OpenAI API.


## Fields

| Field                                                                                                                        | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `function`                                                                                                                   | [models.ToolFunction](../models/toolfunction.md)                                                                             | TRUE                                                                                                           | A function available to an agent.<br/><br/>See:<br/>- https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling |
| `type`                                                                                                                       | *Optional[Literal["function"]]*                                                                                              | FALSE                                                                                                           | Always `function`.                                                                                                           |