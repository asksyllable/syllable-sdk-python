---
title: 'ListResponsePromptResponse'
---

## Example Usage

```typescript
import { ListResponsePromptResponse } from "syllable-sdk/models/components";

let value: ListResponsePromptResponse = {
  items: [
    {
      name: "<value>",
      type: "<value>",
      llmConfig: {
        version: "2024-05-13",
        apiVersion: "2024-06-01",
      },
      id: 448369,
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
            defaults: "<value>",
          },
          serviceId: 866789,
          id: 627735,
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
          lastUpdated: new Date("2024-03-15T23:09:38.803Z"),
          lastUpdatedBy: "user@email.com",
        },
      ],
    },
  ],
  page: 416692,
  pageSize: 810839,
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `items`                                                                  | [components.PromptResponse](/sdk-docs/models/components/promptresponse)[] | TRUE                                                       | N/A                                                                      |
| `page`                                                                   | *number*                                                                 | TRUE                                                       | N/A                                                                      |
| `pageSize`                                                               | *number*                                                                 | TRUE                                                       | N/A                                                                      |
| `totalPages`                                                             | *number*                                                                 | FALSE                                                       | N/A                                                                      |
| `totalCount`                                                             | *number*                                                                 | FALSE                                                       | N/A                                                                      |