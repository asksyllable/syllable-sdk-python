# InsightsFolderInput

Request model to create/update an insight upload folder.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `name`                                         | *str*                                          | :heavy_check_mark:                             | Human-readable name of insight folder          | customer-complaints                            |
| `label`                                        | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | optional label assigned to insight folder      | support                                        |
| `description`                                  | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | Text description of insight upload folder      | Call recordings related to customer complaints |