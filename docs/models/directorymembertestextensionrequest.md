# DirectoryMemberTestExtensionRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `member_id`                                                        | *int*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `timestamp`                                                        | *str*                                                              | :heavy_check_mark:                                                 | Timestamp for test in ISO 8601 format (e.g., 2025-12-04T14:29:39)  |
| `language_code`                                                    | [OptionalNullable[models.LanguageCode]](../models/languagecode.md) | :heavy_minus_sign:                                                 | Optional language code for test                                    |