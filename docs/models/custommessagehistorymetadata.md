# CustomMessageHistoryMetadata

Metadata for a saved Message version, without its content.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `custom_message_id`                                                  | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `version_number`                                                     | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `snapshot_schema_version`                                            | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `operation`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_by`                                                         | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | N/A                                                                  |
| `comments`                                                           | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | N/A                                                                  |
| `restored_from_version`                                              | *Nullable[int]*                                                      | :heavy_check_mark:                                                   | N/A                                                                  |