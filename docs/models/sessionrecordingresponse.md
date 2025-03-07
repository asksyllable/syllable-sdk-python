# SessionRecordingResponse

Recording URLs for a given session.


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `session_id`                   | *OptionalNullable[str]*        | :heavy_minus_sign:             | The internal ID of the session |
| `recordings`                   | List[*str*]                    | :heavy_minus_sign:             | List of recording URLs         |