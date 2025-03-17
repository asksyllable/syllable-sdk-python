---
title: 'ToolAgentInfo'
---

Information about an agent linked to a tool via a prompt.

## Example Usage

```typescript
import { ToolAgentInfo } from "syllable-sdk/models/components";

let value: ToolAgentInfo = {
  id: 1,
  name: "Test Agent",
};
```

## Fields

| Field                 | Type                  | Required              | Description           | Example               |
| --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| `id`                  | *number*              | TRUE    | The ID of the agent   | 1                     |
| `name`                | *string*              | TRUE    | The name of the agent | Test Agent            |