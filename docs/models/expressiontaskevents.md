# ExpressionTaskEvents

Actions to perform when events occur (enter, submit).


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `start`                                                                            | List[[models.ExpressionTaskEventsStart](../models/expressiontaskeventsstart.md)]   | :heavy_minus_sign:                                                                 | Actions to execute on the first input from the user.                               |
| `submit`                                                                           | List[[models.ExpressionTaskEventsSubmit](../models/expressiontaskeventssubmit.md)] | :heavy_minus_sign:                                                                 | Actions to execute when the tool/step is submitted by the LLM.                     |