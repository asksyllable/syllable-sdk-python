---
title: 'FunctionT'
---

A tool definition to be used by the OpenAI API.

See:
- https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling

## Example Usage

```typescript
import { FunctionT } from "syllable-sdk/models/components";

let value: FunctionT = {
  name: "<value>",
  description:
    "blank kiddingly overheard or astride baseboard councilman ambitious",
  parameters: {},
};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *string*                                                         | TRUE                                               | The name of the function/tool call.                              |
| `description`                                                    | *string*                                                         | TRUE                                               | The description of the tool.                                     |
| `parameters`                                                     | [components.ParametersT](/sdk-docs/models/components/parameterst) | TRUE                                               | The JSON Schema of parameters of the function/tool call.         |