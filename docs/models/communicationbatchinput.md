# CommunicationBatchInput


## Fields

| Field                            | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `batch_id`                       | *str*                            | :heavy_check_mark:               | Unique ID for conversation batch | 20250407.9                       |
| `campaign_id`                    | *int*                            | :heavy_check_mark:               | Unique ID for campaign           | 1                                |
| `expires_on`                     | *OptionalNullable[str]*          | :heavy_minus_sign:               | Timestamp of batch expiration    | 2025-04-08T00:00:00Z             |