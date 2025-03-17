---
title: 'PromptHistory'
---

Record of a change to a prompt. Values reflect post-change state.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | TRUE                                                   | Timestamp of the change                                              |
| `prompt_id`                                                          | *str*                                                                | TRUE                                                   | ID of the prompt                                                     |
| `prompt_text`                                                        | *str*                                                                | TRUE                                                   | Text of the prompt                                                   |
| `prompt_name`                                                        | *str*                                                                | TRUE                                                   | Name of the prompt                                                   |
| `user_email`                                                         | *str*                                                                | TRUE                                                   | Email address of the user who made the change                        |
| `prompt_description`                                                 | *OptionalNullable[str]*                                              | FALSE                                                   | Description of the prompt                                            |
| `llm_config`                                                         | *OptionalNullable[str]*                                              | FALSE                                                   | String representation of LLM config for the prompt                   |
| `comments`                                                           | *OptionalNullable[str]*                                              | FALSE                                                   | Comments describing the change                                       |