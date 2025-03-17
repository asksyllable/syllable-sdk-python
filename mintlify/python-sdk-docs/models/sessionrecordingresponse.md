---
title: 'SessionRecordingResponse'
---

Recording URLs for a given session.


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `session_id`                   | *OptionalNullable[str]*        | FALSE             | The internal ID of the session |
| `recordings`                   | List[*str*]                    | FALSE             | List of recording URLs         |