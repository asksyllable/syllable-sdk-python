---
title: 'SessionAction'
---

Information about a given tool invocation as part of a session.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | TRUE                                                   | Timestamp of the tool invocation                                     |
| `tool_name`                                                          | *OptionalNullable[str]*                                              | FALSE                                                   | Name of the tool that was invoked                                    |
| `tool_request`                                                       | *OptionalNullable[str]*                                              | FALSE                                                   | Request sent to the tool API, if applicable                          |
| `tool_result`                                                        | *OptionalNullable[str]*                                              | FALSE                                                   | Response received from the tool API, if applicable                   |
| `tool_error`                                                         | *OptionalNullable[str]*                                              | FALSE                                                   | Error received from the tool API, if applicable                      |