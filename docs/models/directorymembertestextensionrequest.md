# DirectoryMemberTestExtensionRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `member_id`                                                          | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp for test                                                   |
| `language_code`                                                      | [OptionalNullable[models.LanguageCode]](../models/languagecode.md)   | :heavy_minus_sign:                                                   | Optional language code for test                                      |