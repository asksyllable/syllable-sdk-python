# CommunicationBatchUpdate


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `paused`                                                              | *OptionalNullable[bool]*                                              | :heavy_minus_sign:                                                    | Whether the batch is on HOLD. When on HOLD, no outreach will be made. | **Example 1:** true<br/>**Example 2:** false                          |
| `expires_on`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_minus_sign:                                                    | Timestamp of batch expiration                                         | 2027-01-01T06:00:00Z                                                  |