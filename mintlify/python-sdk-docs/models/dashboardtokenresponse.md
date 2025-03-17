---
title: 'DashboardTokenResponse'
---

Basic information about a dashboard.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `embedded_id`                                   | *str*                                           | TRUE                              | Superset embedded ID of the dashboard           |
| `guest_token`                                   | *str*                                           | TRUE                              | Superset guest token of the dashboard           |
| `name`                                          | *str*                                           | TRUE                              | Name of the dashboard                           |
| `display_name`                                  | *str*                                           | TRUE                              | Display name of the dashboard                   |
| `superset_url`                                  | *str*                                           | TRUE                              | Superset URL of the dashboard                   |
| `rank`                                          | *int*                                           | TRUE                              | Dashboard importance, 0 is the highest          |
| `label`                                         | *str*                                           | TRUE                              | Dashboard label.  Typically report or dashboard |