# DetailLegacySessionLink


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `code`                           | [errors.Code](../errors/code.md) | :heavy_check_mark:               | Identifies a legacy session link |
| `session_id`                     | *str*                            | :heavy_check_mark:               | The requested transcript ID      |
| `redirect_to`                    | *str*                            | :heavy_check_mark:               | The transcript path to open      |
| `message`                        | *str*                            | :heavy_check_mark:               | Why this request was rejected    |