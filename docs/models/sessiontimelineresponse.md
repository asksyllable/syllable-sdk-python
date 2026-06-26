# SessionTimelineResponse

Consolidated, time-ordered timeline of a session's events.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `session_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Internal ID of the session                                           |
| `session_start`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Timestamp of the first event; the zero point for all offsets         |
| `events`                                                             | List[[models.TimelineEvent](../models/timelineevent.md)]             | :heavy_check_mark:                                                   | All events, ordered by timestamp ascending                           |