# PermissionResponse

Information about a permission.


## Fields

| Field                          | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `name`                         | *str*                          | :heavy_check_mark:             | Name of the permission         | agents_read                    |
| `display_name`                 | *str*                          | :heavy_check_mark:             | Display name of the permission | View                           |
| `description`                  | *OptionalNullable[str]*        | :heavy_minus_sign:             | Description of the permission  | Fetch agent information        |