# SessionAction

Information about a given tool invocation as part of a session.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp of the tool invocation                                     |
| `tool_name`                                                          | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Name of the tool that was invoked                                    |
| `tool_request`                                                       | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Request sent to the tool API, if applicable                          |
| `tool_result`                                                        | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Response received from the tool API, if applicable                   |
| `tool_error`                                                         | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Error received from the tool API, if applicable                      |