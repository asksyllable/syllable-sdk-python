# InsightsFolderFileMove

Request model to move files between insight upload folders.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `destination_folder_id`                               | *int*                                                 | :heavy_check_mark:                                    | System-assign folder ID                               | 182764                                                |
| `file_id_list`                                        | List[*int*]                                           | :heavy_check_mark:                                    | List of system-assigned IDs for the files to be moved | [12334,23445,34556]                                   |