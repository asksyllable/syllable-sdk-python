---
title: 'PromptLlmConfig'
---

## Example Usage

```typescript
import { PromptLlmConfig } from "syllable-sdk/models/components";

let value: PromptLlmConfig = {
  version: "2024-05-13",
  apiVersion: "2024-06-01",
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `provider`                                                                   | [components.PromptLlmProvider](/sdk-docs/models/components/promptllmprovider) | FALSE                                                           | LLM API provider.                                                            |                                                                              |
| `model`                                                                      | *string*                                                                     | FALSE                                                           | Name of the model. Must match the deployment name in Azure AI Studio.        | gpt-4o                                                                       |
| `version`                                                                    | *string*                                                                     | FALSE                                                           | Optional model version.                                                      | 2024-05-13                                                                   |
| `apiVersion`                                                                 | *string*                                                                     | FALSE                                                           | Version of the API. (Currently only used for Azure OpenAI.)                  | 2024-06-01                                                                   |