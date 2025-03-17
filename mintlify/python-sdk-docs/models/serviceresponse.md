---
title: 'ServiceResponse'
---

A service is a collection of tools.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | TRUE                                                   | The name of the service                                              |
| `description`                                                        | *str*                                                                | TRUE                                                   | The description of the service                                       |
| `id`                                                                 | *int*                                                                | TRUE                                                   | The ID of the service                                                |
| `last_updated`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | TRUE                                                   | The timestamp of the most recent update to the service               |
| `last_updated_by`                                                    | *str*                                                                | TRUE                                                   | The email of the user who last updated the service                   |
| `tools`                                                              | List[*str*]                                                          | TRUE                                                   | Names of tools that belong to the service                            |
| `last_updated_comments`                                              | *OptionalNullable[str]*                                              | FALSE                                                   | Update comments                                                      |