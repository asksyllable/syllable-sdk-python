---
title: 'DashboardResponse'
---

Basic information about a dashboard with a description.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `name`                                          | *str*                                           | TRUE                              | Name of the dashboard                           |
| `display_name`                                  | *str*                                           | TRUE                              | Display name of the dashboard                   |
| `rank`                                          | *int*                                           | TRUE                              | Dashboard importance, 0 is the highest          |
| `label`                                         | *str*                                           | TRUE                              | Dashboard label.  Typically report or dashboard |