---
title: 'LanguageGroupAgentInfo'
---

Information about an agent linked to a language group.

## Example Usage

```typescript
import { LanguageGroupAgentInfo } from "syllable-sdk/models/components";

let value: LanguageGroupAgentInfo = {
  id: 1,
  name: "Test Agent",
};
```

## Fields

| Field                 | Type                  | Required              | Description           | Example               |
| --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| `id`                  | *number*              | TRUE    | The ID of the agent   | 1                     |
| `name`                | *string*              | TRUE    | The name of the agent | Test Agent            |