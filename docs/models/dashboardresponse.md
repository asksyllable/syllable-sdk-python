# DashboardResponse

Basic information about a dashboard with a description.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Name of the dashboard                              | session_summary                                    |
| `display_name`                                     | *str*                                              | :heavy_check_mark:                                 | Display name of the dashboard                      | Session Summary                                    |
| `rank`                                             | *int*                                              | :heavy_check_mark:                                 | Dashboard importance (0 is the highest)            | 0                                                  |
| `label`                                            | *str*                                              | :heavy_check_mark:                                 | Dashboard label. Typically "report" or "dashboard" | dashboard                                          |