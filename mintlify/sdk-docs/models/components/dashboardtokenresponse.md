---
title: 'DashboardTokenResponse'
---

Basic information about a dashboard.

## Example Usage

```typescript
import { DashboardTokenResponse } from "syllable-sdk/models/components";

let value: DashboardTokenResponse = {
  embeddedId: "<id>",
  guestToken: "<value>",
  name: "<value>",
  displayName: "Lavina69",
  supersetUrl: "https://smart-in-joke.name/",
  rank: 955047,
  label: "<value>",
};
```

## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `embeddedId`                                    | *string*                                        | TRUE                              | Superset embedded ID of the dashboard           |
| `guestToken`                                    | *string*                                        | TRUE                              | Superset guest token of the dashboard           |
| `name`                                          | *string*                                        | TRUE                              | Name of the dashboard                           |
| `displayName`                                   | *string*                                        | TRUE                              | Display name of the dashboard                   |
| `supersetUrl`                                   | *string*                                        | TRUE                              | Superset URL of the dashboard                   |
| `rank`                                          | *number*                                        | TRUE                              | Dashboard importance, 0 is the highest          |
| `label`                                         | *string*                                        | TRUE                              | Dashboard label.  Typically report or dashboard |