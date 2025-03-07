# DashboardTokenResponse

Basic information about a dashboard.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `embedded_id`                                   | *str*                                           | :heavy_check_mark:                              | Superset embedded ID of the dashboard           |
| `guest_token`                                   | *str*                                           | :heavy_check_mark:                              | Superset guest token of the dashboard           |
| `name`                                          | *str*                                           | :heavy_check_mark:                              | Name of the dashboard                           |
| `display_name`                                  | *str*                                           | :heavy_check_mark:                              | Display name of the dashboard                   |
| `superset_url`                                  | *str*                                           | :heavy_check_mark:                              | Superset URL of the dashboard                   |
| `rank`                                          | *int*                                           | :heavy_check_mark:                              | Dashboard importance, 0 is the highest          |
| `label`                                         | *str*                                           | :heavy_check_mark:                              | Dashboard label.  Typically report or dashboard |