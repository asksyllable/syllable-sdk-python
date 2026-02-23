# ValidationIssue

A single validation finding with severity, location, and description.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | Stable machine-readable identifier (kebab-case)        |
| `severity`                                             | [Optional[models.Severity]](../models/severity.md)     | :heavy_minus_sign:                                     | N/A                                                    |
| `message`                                              | *str*                                                  | :heavy_check_mark:                                     | Human-readable description                             |
| `path`                                                 | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | JSONPath-style location (e.g. $.context.task.steps[2]) |
| `value`                                                | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | The offending value, when it adds clarity              |