# TranscriptWordConfidence

Per-word STT confidence. `word` prefers the provider's punctuated form so the stored words
read the same way as the transcript they came from.


## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `word`                    | *str*                     | :heavy_check_mark:        | N/A                       |
| `confidence`              | *OptionalNullable[float]* | :heavy_minus_sign:        | N/A                       |
| `start`                   | *OptionalNullable[float]* | :heavy_minus_sign:        | N/A                       |
| `end`                     | *OptionalNullable[float]* | :heavy_minus_sign:        | N/A                       |