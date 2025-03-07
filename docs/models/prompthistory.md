# PromptHistory

Record of a change to a prompt. Values reflect post-change state.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp of the change                                              |
| `prompt_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | ID of the prompt                                                     |
| `prompt_text`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Text of the prompt                                                   |
| `prompt_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Name of the prompt                                                   |
| `user_email`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Email address of the user who made the change                        |
| `prompt_description`                                                 | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Description of the prompt                                            |
| `llm_config`                                                         | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | String representation of LLM config for the prompt                   |
| `comments`                                                           | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Comments describing the change                                       |