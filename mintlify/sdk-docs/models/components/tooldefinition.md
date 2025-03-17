---
title: 'ToolDefinition'
---

A tool that can be called from an LLM during the conversation. See https://docs.syllable.ai/Resources/Tools.

## Example Usage

```typescript
import { ToolDefinition } from "syllable-sdk/models/components";

let value: ToolDefinition = {
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
    argumentLocation: "query",
  },
  defaults: "<value>",
};
```

## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `type`                                                                                             | [components.Type](/sdk-docs/models/components/type)                                                 | FALSE                                                                                 | The action to take when the LLM calls the tool.                                                    |
| `tool`                                                                                             | [components.InternalTool](/sdk-docs/models/components/internaltool)                                 | TRUE                                                                                 | A tool definition to be used by the OpenAI API.                                                    |
| `endpoint`                                                                                         | [components.ToolHttpEndpoint](/sdk-docs/models/components/toolhttpendpoint)                         | FALSE                                                                                 | The configuration for an HTTP API call.                                                            |
| `defaults`                                                                                         | *components.Defaults*                                                                              | FALSE                                                                                 | The default values for the parameters of the function/tool call.                                   |
| `staticParameters`                                                                                 | [components.StaticToolParameter](/sdk-docs/models/components/statictoolparameter)[]                 | FALSE                                                                                 | Parameters for the tool whose values should be set at config time (i.e., not provided by the LLM). |
| `result`                                                                                           | *any*                                                                                              | FALSE                                                                                 | The optional result of the tool call. Only used for `context` tools.                               |