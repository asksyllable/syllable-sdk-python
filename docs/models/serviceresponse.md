# ServiceResponse

A service is a collection of tools.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The name of the service                                              |
| `description`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The description of the service                                       |
| `id`                                                                 | *int*                                                                | :heavy_check_mark:                                                   | The ID of the service                                                |
| `last_updated`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The timestamp of the most recent update to the service               |
| `last_updated_by`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The email of the user who last updated the service                   |
| `tools`                                                              | List[*str*]                                                          | :heavy_check_mark:                                                   | Names of tools that belong to the service                            |
| `last_updated_comments`                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Update comments                                                      |