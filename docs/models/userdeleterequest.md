# UserDeleteRequest

Request model to delete a user.


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `email`                                 | *str*                                   | :heavy_check_mark:                      | The email address of the user to delete | user@email.com                          |
| `reason`                                | *str*                                   | :heavy_check_mark:                      | The reason for deleting the user        | User left the organization              |