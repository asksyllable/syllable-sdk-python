---
title: 'ListResponseAgentResponse'
---

## Example Usage

```typescript
import { ListResponseAgentResponse } from "syllable-sdk/models/components";

let value: ListResponseAgentResponse = {
  items: [],
  page: 548814,
  pageSize: 715190,
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `items`                                                                | [components.AgentResponse](/sdk-docs/models/components/agentresponse)[] | TRUE                                                     | N/A                                                                    |
| `page`                                                                 | *number*                                                               | TRUE                                                     | N/A                                                                    |
| `pageSize`                                                             | *number*                                                               | TRUE                                                     | N/A                                                                    |
| `totalPages`                                                           | *number*                                                               | FALSE                                                     | N/A                                                                    |
| `totalCount`                                                           | *number*                                                               | FALSE                                                     | N/A                                                                    |