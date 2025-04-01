# TakeoutStatusResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `job_id`                                                             | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `status`                                                             | [models.TakeoutRequestStatus](../models/takeoutrequeststatus.md)     | :heavy_check_mark:                                                   | Status of a takeout request.                                         |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `download_links`                                                     | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |