---
title: 'Dashboard'
---

Deprecated.  Please update to use DashboardTokenResponse.
Basic information about a dashboard.

## Example Usage

```typescript
import { Dashboard } from "syllable-sdk/models/components";

let value: Dashboard = {
  embeddedId: "<id>",
  guestToken: "<value>",
  name: "<value>",
  supersetUrl: "https://total-fort.org",
};
```

## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `embeddedId`                          | *string*                              | TRUE                    | Superset embedded ID of the dashboard |
| `guestToken`                          | *string*                              | TRUE                    | Superset guest token of the dashboard |
| `name`                                | *string*                              | TRUE                    | Name of the dashboard                 |
| `supersetUrl`                         | *string*                              | TRUE                    | Superset URL of the dashboard         |