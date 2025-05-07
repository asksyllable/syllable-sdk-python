# InsightToolTestInput

Request model to test an insight tool.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `tool_name`                                           | *str*                                                 | :heavy_check_mark:                                    | Human readable name of insight tool configuration     | summary-tool                                          |
| `session_id`                                          | *int*                                                 | :heavy_check_mark:                                    | The session ID of the session to run the tool against | 283467                                                |