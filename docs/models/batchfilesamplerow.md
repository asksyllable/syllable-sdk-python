# BatchFileSampleRow

A row of a batch file as the agent receives it.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `reference_id`                           | *str*                                    | :heavy_check_mark:                       | Reference for the contact                | 12345                                    |
| `target`                                 | *str*                                    | :heavy_check_mark:                       | Phone number or email address to contact | +12125551234                             |
| `request_variables`                      | Dict[str, *str*]                         | :heavy_check_mark:                       | Values from the other columns            | {<br/>"first_name": "Jane"<br/>}         |