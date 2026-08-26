# CardClickRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `action_id`                                             | *str*                                                   | :heavy_check_mark:                                      | Human-readable identifier for the card action.          |
| `action_type`                                           | [models.ActionType](../models/actiontype.md)            | :heavy_check_mark:                                      | The type of action triggers, either "action", or "cta". |