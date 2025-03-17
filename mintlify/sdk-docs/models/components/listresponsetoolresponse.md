---
title: 'ListResponseToolResponse'
---

## Example Usage

```typescript
import { ListResponseToolResponse } from "syllable-sdk/models/components";

let value: ListResponseToolResponse = {
  items: [
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
      serviceId: 169819,
      id: 148379,
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
      lastUpdated: new Date("2025-04-27T11:48:28.988Z"),
      lastUpdatedBy: "user@email.com",
    },
  ],
  page: 567693,
  pageSize: 983000,
};
```

## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `items`                                                              | [components.ToolResponse](/sdk-docs/models/components/toolresponse)[] | TRUE                                                   | N/A                                                                  |
| `page`                                                               | *number*                                                             | TRUE                                                   | N/A                                                                  |
| `pageSize`                                                           | *number*                                                             | TRUE                                                   | N/A                                                                  |
| `totalPages`                                                         | *number*                                                             | FALSE                                                   | N/A                                                                  |
| `totalCount`                                                         | *number*                                                             | FALSE                                                   | N/A                                                                  |