---
title: 'ToolDetailResponse'
---

A tool is a function that an agent can call to perform actions like accessing databases,
making API calls, or processing data. For an agent to have access to a tool, the prompt
associated with that agent should be linked to the tool and include instructions to use it.
For more information, see [Console docs](https://docs.syllable.ai/Resources/Tools).

## Example Usage

```typescript
import { ToolDetailResponse } from "syllable-sdk/models/components";

let value: ToolDetailResponse = {
  name: "Weather Fetcher",
  definition: {
    tool: {
      function: {
        name: "weather_fetcher",
        description: "Fetches weather data",
        parameters: {},
      },
    },
    endpoint: {
      url: "https://api.example.com",
      method: "get",
      argumentLocation: "body",
    },
    defaults: "<value>",
  },
  serviceId: 4654,
  id: 424854,
  promptsInfo: [
    {
      id: 1,
      name: "Test Prompt",
    },
  ],
  agentsInfo: [
    {
      id: 1,
      name: "Test Agent",
    },
  ],
  lastUpdated: new Date("2024-12-28T23:02:26.348Z"),
  lastUpdatedBy: "user@email.com",
  fields: [
    "<value>",
  ],
};
```

## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                       | *string*                                                                                                     | TRUE                                                                                           | The name of the tool                                                                                         | Weather Fetcher                                                                                              |
| `definition`                                                                                                 | [components.ToolDefinition](/sdk-docs/models/components/tooldefinition)                                       | TRUE                                                                                           | A tool that can be called from an LLM during the conversation. See https://docs.syllable.ai/Resources/Tools. |                                                                                                              |
| `serviceId`                                                                                                  | *number*                                                                                                     | TRUE                                                                                           | The service to which this tool belongs                                                                       |                                                                                                              |
| `id`                                                                                                         | *number*                                                                                                     | TRUE                                                                                           | The ID of the tool                                                                                           |                                                                                                              |
| `lastUpdatedComments`                                                                                        | *string*                                                                                                     | FALSE                                                                                           | Update comments                                                                                              |                                                                                                              |
| `serviceName`                                                                                                | *string*                                                                                                     | FALSE                                                                                           | The name of the service to which the tool belongs                                                            |                                                                                                              |
| `promptsInfo`                                                                                                | [components.ToolPromptInfo](/sdk-docs/models/components/toolpromptinfo)[]                                     | FALSE                                                                                           | IDs and names of the prompts linked to the tool                                                              |                                                                                                              |
| `agentsInfo`                                                                                                 | [components.ToolAgentInfo](/sdk-docs/models/components/toolagentinfo)[]                                       | FALSE                                                                                           | IDs and names of the agents linked to the tool via a prompt                                                  |                                                                                                              |
| `lastUpdated`                                                                                                | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                | TRUE                                                                                           | The timestamp of the most recent update to the service                                                       |                                                                                                              |
| `lastUpdatedBy`                                                                                              | *string*                                                                                                     | TRUE                                                                                           | The email of the user who last updated the tool                                                              | user@email.com                                                                                               |
| `fields`                                                                                                     | *string*[]                                                                                                   | TRUE                                                                                           | Fields that the tool accepts as input                                                                        |                                                                                                              |