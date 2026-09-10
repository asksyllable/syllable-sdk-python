# DaoExperimentTargetSummary

The channel target an experiment splits, resolved for display.

Enough to name the target on the experiment card without a second read: the Console shows the
target itself and the channel it belongs to, and links to neither by ID.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *int*                                                        | :heavy_check_mark:                                           | The internal ID of the channel target                        | 1                                                            |
| `target`                                                     | *str*                                                        | :heavy_check_mark:                                           | The target itself, such as a phone number                    | +19995551234                                                 |
| `target_mode`                                                | [models.TargetModes](../models/targetmodes.md)               | :heavy_check_mark:                                           | Available modes (communication methods) for channel targets. |                                                              |
| `channel_id`                                                 | *int*                                                        | :heavy_check_mark:                                           | The channel the target belongs to                            | 1                                                            |
| `channel_name`                                               | *str*                                                        | :heavy_check_mark:                                           | The name of that channel                                     | Main line                                                    |