---
title: 'ToolFunction'
---

A function available to an agent.

See:
- https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling

## Example Usage

```typescript
import { ToolFunction } from "syllable-sdk/models/components";

let value: ToolFunction = {
  name: "weather_fetcher",
  description: "Fetches weather data",
  parameters: {},
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `name`                                                   | *string*                                                 | TRUE                                       | The name of the function/tool call.                      | weather_fetcher                                          |
| `description`                                            | *string*                                                 | TRUE                                       | The description of the tool.                             | Fetches weather data                                     |
| `parameters`                                             | *any*                                                    | TRUE                                       | The JSON Schema of parameters of the function/tool call. | {}                                                       |