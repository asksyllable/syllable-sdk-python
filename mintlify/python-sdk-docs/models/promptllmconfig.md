---
title: 'PromptLlmConfig'
---


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `provider`                                                            | [Optional[models.PromptLlmProvider]](../models/promptllmprovider.md)  | FALSE                                                    | LLM API provider.                                                     |                                                                       |
| `model`                                                               | *Optional[str]*                                                       | FALSE                                                    | Name of the model. Must match the deployment name in Azure AI Studio. | gpt-4o                                                                |
| `version`                                                             | *OptionalNullable[str]*                                               | FALSE                                                    | Optional model version.                                               | 2024-05-13                                                            |
| `api_version`                                                         | *OptionalNullable[str]*                                               | FALSE                                                    | Version of the API. (Currently only used for Azure OpenAI.)           | 2024-06-01                                                            |