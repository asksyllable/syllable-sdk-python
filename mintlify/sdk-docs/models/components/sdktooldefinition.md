---
title: 'SDKToolDefinition'
---

## Example Usage

```typescript
import { SDKToolDefinition } from "syllable-sdk/models/components";

let value: SDKToolDefinition = {
  tool: {
    function: {
      name: "<value>",
      description: "eek where kindly materialise antique failing hence",
      parameters: {},
    },
  },
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | [components.Type](/sdk-docs/models/components/type)                       | FALSE                                                       | The action to take when GPT calls the tool.                              |
| `tool`                                                                   | [components.SDKInternalTool](/sdk-docs/models/components/sdkinternaltool) | TRUE                                                       | A tool definition to be used by the OpenAI API.                          |
| `endpoint`                                                               | [components.HttpEndpoint](/sdk-docs/models/components/httpendpoint)       | FALSE                                                       | The configuration for an HTTP API call.                                  |
| `defaults`                                                               | *components.Defaults*                                                    | FALSE                                                       | The default values for the parameters of the function/tool call.         |
| `result`                                                                 | [components.Result](/sdk-docs/models/components/result)                   | FALSE                                                       | The optional result of the tool call. Only used for `context` tools.     |