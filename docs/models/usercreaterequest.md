# UserCreateRequest

Request model to create a user.


## Fields

| Field                               | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `email`                             | *str*                               | :heavy_check_mark:                  | Email address of the user           | user@syllable.ai                    |
| `first_name`                        | *OptionalNullable[str]*             | :heavy_minus_sign:                  | First name of the user              | Jane                                |
| `last_name`                         | *OptionalNullable[str]*             | :heavy_minus_sign:                  | Last name of the user               | Smith                               |
| `role_id`                           | *int*                               | :heavy_check_mark:                  | ID of the role assigned to the user | 1                                   |