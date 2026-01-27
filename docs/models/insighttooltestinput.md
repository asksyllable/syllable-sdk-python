# InsightToolTestInput

Request model to test an insight tool.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `tool_name`                                                    | *str*                                                          | :heavy_check_mark:                                             | Human readable name of insight tool configuration              | summary-tool                                                   |
| `session_id`                                                   | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | The session ID of the session against which to run the tool    |                                                                |
| `upload_file_id`                                               | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | The file ID of the uploaded file against which to run the tool |                                                                |