# AvailableTarget

An available organization-level channel target (i.e., one for which a channel target has not
been created in the current suborg).


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `organization_id`                                               | *int*                                                           | :heavy_check_mark:                                              | Internal ID of the org with which the target is associated.     | 1                                                               |
| `channel_id`                                                    | *int*                                                           | :heavy_check_mark:                                              | Internal ID of the channel with which the target is associated. | 1                                                               |
| `channel_name`                                                  | *Nullable[str]*                                                 | :heavy_check_mark:                                              | Name of the channel with which the target is associated.        | Twilio                                                          |
| `target`                                                        | *str*                                                           | :heavy_check_mark:                                              | Org-level target.                                               | +19995551234                                                    |