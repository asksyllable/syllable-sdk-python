# ServiceUpdateRequest

Request model to update an existing service.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `name`                                                    | *str*                                                     | :heavy_check_mark:                                        | The name of the service                                   | Weather tools                                             |
| `description`                                             | *str*                                                     | :heavy_check_mark:                                        | The description of the service                            | Service containing tools for fetching weather information |
| `id`                                                      | *int*                                                     | :heavy_check_mark:                                        | The internal ID of the service                            | 1                                                         |
| `last_updated_comments`                                   | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | Free text providing comment about what was updated        | Updated description to correct typo                       |