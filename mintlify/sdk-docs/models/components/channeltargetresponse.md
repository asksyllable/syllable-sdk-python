---
title: 'ChannelTargetResponse'
---

A channel target links a channel to an agent, allowing users to communicate with the agent
through that channel. For more information, see
[Console docs](https://docs.syllable.ai/Resources/Channels).

## Example Usage

```typescript
import { ChannelTargetResponse } from "syllable-sdk/models/components";

let value: ChannelTargetResponse = {
  agentId: 120196,
  channelId: 296140,
  target: "<value>",
  targetMode: "voice",
  id: 317983,
  channelName: "<value>",
  updatedAt: new Date("2024-03-30T00:46:25.708Z"),
  lastUpdatedBy: "<value>",
  agent: {
    name: "<value>",
    type: "ca_v1",
    promptId: 64147,
    customMessageId: 692472,
    timezone: "America/Chicago",
    variables: {
      "key": "<value>",
    },
    toolHeaders: {
      "key": "<value>",
    },
    sttProvider: "Google STT V1",
    waitSound: "Keyboard 2",
    id: 93940,
    updatedAt: new Date("2024-09-23T05:41:47.829Z"),
    lastUpdatedBy: "<value>",
    prompt: {
      name: "<value>",
      type: "<value>",
      llmConfig: {
        version: "2024-05-13",
        apiVersion: "2024-06-01",
      },
      id: 929297,
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
              method: "get",
              argumentLocation: "path",
            },
            defaults: "<value>",
          },
          serviceId: 716327,
          id: 289406,
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
          lastUpdated: new Date("2023-07-20T18:39:56.110Z"),
          lastUpdatedBy: "user@email.com",
        },
      ],
    },
    customMessage: {
      name: "<value>",
      text: "<value>",
      rules: [
        {
          description: "oof failing other insignificant woot purse salty",
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
      id: 100226,
      updatedAt: new Date("2025-10-04T18:04:14.419Z"),
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
            method: "post",
            argumentLocation: "query",
          },
          defaults: "<value>",
        },
        serviceId: 868126,
        id: 162493,
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
        lastUpdated: new Date("2024-11-05T15:40:43.604Z"),
        lastUpdatedBy: "user@email.com",
      },
    ],
    languageGroup: {
      name: "Call Center 1 Languages",
      description: "Languages spoken by operators at Call Center 1",
      languageConfigs: [
        {
          languageCode: "yue-HK",
          voiceProvider: "Google",
          voiceDisplayName: "River",
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
      updatedAt: new Date("2024-09-15T17:37:32.983Z"),
      lastUpdatedBy: "user@mail.com",
    },
  },
};
```

## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `agentId`                                                                                                                      | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the agent associated with the channel target                                                                         |
| `channelId`                                                                                                                    | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the channel associated with the channel target                                                                       |
| `target`                                                                                                                       | *string*                                                                                                                       | TRUE                                                                                                             | The name of the channel target (must correspond to an organization-level target)                                               |
| `targetMode`                                                                                                                   | [components.TargetModes](/sdk-docs/models/components/targetmodes)                                                               | TRUE                                                                                                             | Available modes (communication methods) for channel targets.                                                                   |
| `fallbackTarget`                                                                                                               | *string*                                                                                                                       | FALSE                                                                                                             | The fallback for the channel target (currently only supported for "voice" mode)                                                |
| `isTest`                                                                                                                       | *boolean*                                                                                                                      | FALSE                                                                                                             | Whether the channel target is intended for testing. If true, any sessions created through this target will be labeled as test. |
| `id`                                                                                                                           | *number*                                                                                                                       | TRUE                                                                                                             | The ID of the channel target                                                                                                   |
| `channelName`                                                                                                                  | *string*                                                                                                                       | TRUE                                                                                                             | The name of the channel associated with the channel target                                                                     |
| `updatedAt`                                                                                                                    | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                  | TRUE                                                                                                             | Timestamp of the most recent update to the channel target                                                                      |
| `lastUpdatedBy`                                                                                                                | *string*                                                                                                                       | TRUE                                                                                                             | Email of the user who last updated the channel target                                                                          |
| `agent`                                                                                                                        | [components.AgentResponse](/sdk-docs/models/components/agentresponse)                                                           | FALSE                                                                                                             | Definition of the agent for the channel target                                                                                 |