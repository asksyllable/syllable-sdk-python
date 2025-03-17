---
title: 'AgentResponse'
---

When a user interacts with the Syllable system, they do so by communicating with an agent.
An agent is linked to a prompt, a custom message, and one or more channel targets to define its
behavior and capabilities. For more information, see
[Console docs](https://docs.syllable.ai/workspaces/Agents).

## Example Usage

```typescript
import { AgentResponse } from "syllable-sdk/models/components";

let value: AgentResponse = {
  name: "<value>",
  type: "ca_v1",
  promptId: 602763,
  customMessageId: 544883,
  timezone: "America/New_York",
  variables: {
    "key": "<value>",
  },
  toolHeaders: {
    "key": "<value>",
  },
  sttProvider: "Google STT V2",
  waitSound: "Keyboard 1",
  id: 891773,
  updatedAt: new Date("2025-11-22T04:11:06.908Z"),
  lastUpdatedBy: "<value>",
  prompt: {
    name: "<value>",
    type: "<value>",
    llmConfig: {
      version: "2024-05-13",
      apiVersion: "2024-06-01",
    },
    id: 383441,
    lastUpdated: "<value>",
    lastUpdatedBy: "user@email.com",
    toolsFull: [
      {
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
            method: "post",
            argumentLocation: "path",
          },
          defaults: {
            "key": {
              transform: {
                action: "default",
                when: {
                  key: "key",
                  value: "value",
                },
              },
            },
          },
        },
        serviceId: 925597,
        id: 71036,
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
        lastUpdated: new Date("2023-04-06T11:50:56.757Z"),
        lastUpdatedBy: "user@email.com",
      },
    ],
  },
  customMessage: {
    name: "<value>",
    text: "<value>",
    rules: [
      {
        description: "successfully how gee",
        timeRangeStart: "09:00",
        timeRangeEnd: "17:00",
        date: "2025-01-01",
        daysOfWeek: [
          "mo",
          "tu",
          "we",
          "th",
          "fr",
        ],
        invert: false,
        text: "Sorry, we're closed today",
      },
    ],
    id: 943749,
    updatedAt: new Date("2025-01-17T06:36:04.132Z"),
    lastUpdatedBy: "user@email.com",
  },
  channelTargets: [],
  tools: [
    {
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
          argumentLocation: "form",
        },
        defaults: {
          "key": {
            transform: {
              action: "default",
              when: {
                key: "key",
                value: "value",
              },
            },
          },
        },
      },
      serviceId: 60225,
      id: 666767,
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
      lastUpdated: new Date("2025-01-05T00:27:30.681Z"),
      lastUpdatedBy: "user@email.com",
    },
  ],
  languageGroup: {
    name: "Call Center 1 Languages",
    description: "Languages spoken by operators at Call Center 1",
    languageConfigs: [
      {
        languageCode: "en-US",
        voiceProvider: "OpenAI",
        voiceDisplayName: "Coral",
        dtmfCode: 1,
      },
    ],
    skipCurrentLanguageInMessage: false,
    id: 1,
    editComments: "Added Spanish support.",
    agentsInfo: [
      {
        id: 1,
        name: "Test Agent",
      },
    ],
    updatedAt: new Date("2024-02-03T15:02:53.228Z"),
    lastUpdatedBy: "user@mail.com",
  },
};
```

## Fields

| Field                                                                                                                                                                 | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                | *string*                                                                                                                                                              | TRUE                                                                                                                                                    | The agent name                                                                                                                                                        |                                                                                                                                                                       |
| `description`                                                                                                                                                         | *string*                                                                                                                                                              | FALSE                                                                                                                                                    | The agent description                                                                                                                                                 |                                                                                                                                                                       |
| `label`                                                                                                                                                               | *string*                                                                                                                                                              | FALSE                                                                                                                                                    | The agent label                                                                                                                                                       |                                                                                                                                                                       |
| `type`                                                                                                                                                                | *string*                                                                                                                                                              | TRUE                                                                                                                                                    | The agent type. Can be an arbitrary string                                                                                                                            | ca_v1                                                                                                                                                                 |
| `promptId`                                                                                                                                                            | *number*                                                                                                                                                              | TRUE                                                                                                                                                    | ID of the prompt associated with the agent                                                                                                                            |                                                                                                                                                                       |
| `customMessageId`                                                                                                                                                     | *number*                                                                                                                                                              | TRUE                                                                                                                                                    | ID of the custom message that should be delivered at the beginning of a conversation with the agent                                                                   |                                                                                                                                                                       |
| `languageGroupId`                                                                                                                                                     | *number*                                                                                                                                                              | FALSE                                                                                                                                                    | ID of the language group associated with the agent                                                                                                                    |                                                                                                                                                                       |
| `timezone`                                                                                                                                                            | *string*                                                                                                                                                              | TRUE                                                                                                                                                    | The time zone in which the agent operates                                                                                                                             | America/New_York                                                                                                                                                      |
| `promptToolDefaults`                                                                                                                                                  | [components.AgentToolDefaults](/sdk-docs/models/components/agenttooldefaults)[]                                                                                        | FALSE                                                                                                                                                    | User-configured parameter values for the agent's tools                                                                                                                |                                                                                                                                                                       |
| ~~`languages`~~                                                                                                                                                       | *string*[]                                                                                                                                                            | FALSE                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>BCP 47 codes of languages the agent supports | [<br/>"en-US",<br/>"es-US"<br/>]                                                                                                                                      |
| `variables`                                                                                                                                                           | Record                                                                                                                                              | TRUE                                                                                                                                                    | Custom context variables for the conversation session. Keys should be prefixed with "vars.".                                                                          |                                                                                                                                                                       |
| `toolHeaders`                                                                                                                                                         | Record                                                                                                                                              | TRUE                                                                                                                                                    | Optional headers to include in tool calls for agent.                                                                                                                  |                                                                                                                                                                       |
| `agentInitiated`                                                                                                                                                      | *boolean*                                                                                                                                                             | FALSE                                                                                                                                                    | Whether the agent initiates conversation with a user after the custom_message is delivered                                                                            |                                                                                                                                                                       |
| `sttProvider`                                                                                                                                                         | *string*                                                                                                                                                              | FALSE                                                                                                                                                    | Speech-to-text provider for the agent.                                                                                                                                | Google STT V1                                                                                                                                                         |
| `waitSound`                                                                                                                                                           | *string*                                                                                                                                                              | FALSE                                                                                                                                                    | Sound to play while waiting for a response from the LLM.                                                                                                              | No Sound                                                                                                                                                              |
| `id`                                                                                                                                                                  | *number*                                                                                                                                                              | TRUE                                                                                                                                                    | The agent ID                                                                                                                                                          |                                                                                                                                                                       |
| `updatedAt`                                                                                                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                                                         | TRUE                                                                                                                                                    | Timestamp of most recent update                                                                                                                                       |                                                                                                                                                                       |
| `lastUpdatedBy`                                                                                                                                                       | *string*                                                                                                                                                              | TRUE                                                                                                                                                    | Email of the user who last updated the agent                                                                                                                          |                                                                                                                                                                       |
| `prompt`                                                                                                                                                              | [components.PromptResponse](/sdk-docs/models/components/promptresponse)                                                                                                | FALSE                                                                                                                                                    | The prompt associated with the agent.                                                                                                                                 |                                                                                                                                                                       |
| `customMessage`                                                                                                                                                       | [components.CustomMessageResponse](/sdk-docs/models/components/custommessageresponse)                                                                                  | FALSE                                                                                                                                                    | The custom message associated with the agent. Will be delivered as a greeting at the beginning of a conversation.                                                     |                                                                                                                                                                       |
| `channelTargets`                                                                                                                                                      | [components.ChannelTargetResponse](/sdk-docs/models/components/channeltargetresponse)[]                                                                                | FALSE                                                                                                                                                    | Channel targets associated with the agent                                                                                                                             |                                                                                                                                                                       |
| `tools`                                                                                                                                                               | [components.ToolResponse](/sdk-docs/models/components/toolresponse)[]                                                                                                  | FALSE                                                                                                                                                    | Tools associated with the agent                                                                                                                                       |                                                                                                                                                                       |
| `languageGroup`                                                                                                                                                       | [components.LanguageGroupResponse](/sdk-docs/models/components/languagegroupresponse)                                                                                  | FALSE                                                                                                                                                    | The language group associated with the agent                                                                                                                          |                                                                                                                                                                       |