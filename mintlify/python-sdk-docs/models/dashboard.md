---
title: 'Dashboard'
---

Deprecated.  Please update to use DashboardTokenResponse.
Basic information about a dashboard.


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `embedded_id`                         | *str*                                 | TRUE                    | Superset embedded ID of the dashboard |
| `guest_token`                         | *str*                                 | TRUE                    | Superset guest token of the dashboard |
| `name`                                | *str*                                 | TRUE                    | Name of the dashboard                 |
| `superset_url`                        | *str*                                 | TRUE                    | Superset URL of the dashboard         |