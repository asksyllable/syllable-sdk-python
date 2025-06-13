# PermissionGroupResponse

Information about a group of permissions related to the same feature.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | Name of the permission group                                          | Agents                                                                |
| `description`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Description of the permission group                                   | View agents, create and edit agent configurations, and delete agents. |
| `permissions`                                                         | List[[models.PermissionResponse](../models/permissionresponse.md)]    | :heavy_check_mark:                                                    | Permissions in the group                                              |                                                                       |