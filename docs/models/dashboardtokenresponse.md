# DashboardTokenResponse

Basic information about a dashboard.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `embedded_id`                                      | *str*                                              | :heavy_check_mark:                                 | Superset embedded ID of the dashboard              | 976ef486-d1ea-49c7-ba81-18e955d80286               |
| `guest_token`                                      | *str*                                              | :heavy_check_mark:                                 | Superset guest token of the dashboard              | some-guest-token                                   |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Name of the dashboard                              | session_summary                                    |
| `display_name`                                     | *str*                                              | :heavy_check_mark:                                 | Display name of the dashboard                      | Session Summary                                    |
| `superset_url`                                     | *str*                                              | :heavy_check_mark:                                 | Base Superset URL of the dashboard                 | https://somesuperseturl.com                        |
| `rank`                                             | *int*                                              | :heavy_check_mark:                                 | Dashboard importance (0 is the highest)            | 0                                                  |
| `label`                                            | *str*                                              | :heavy_check_mark:                                 | Dashboard label. Typically "report" or "dashboard" | dashboard                                          |