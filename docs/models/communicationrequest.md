# CommunicationRequest


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `reference_id`                               | *str*                                        | :heavy_check_mark:                           | ID for target outreach (unique within batch) | 12345                                        |
| `target`                                     | *str*                                        | :heavy_check_mark:                           | Target phone number                          | 512-555-1234                                 |
| `request_variables`                          | Dict[str, *str*]                             | :heavy_check_mark:                           | Variables for request                        |                                              |