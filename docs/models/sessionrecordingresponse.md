# SessionRecordingResponse

Recording URLs for a given session.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `session_id`                                                                   | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | The internal ID of the session                                                 | 1                                                                              |
| `recordings`                                                                   | List[*str*]                                                                    | :heavy_minus_sign:                                                             | List of recording URLs                                                         | [<br/>"https://example.com/recording1.mp3",<br/>"https://example.com/recording2.mp3"<br/>] |