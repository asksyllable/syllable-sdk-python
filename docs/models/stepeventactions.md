# StepEventActions

Actions to perform when events occur (enter, submit).


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `start`                                                                    | List[[models.StepEventActionsStart](../models/stepeventactionsstart.md)]   | :heavy_minus_sign:                                                         | Actions to execute on the first input from the user.                       |
| `enter`                                                                    | List[[models.Enter](../models/enter.md)]                                   | :heavy_minus_sign:                                                         | Actions to execute when entering a step (before collecting inputs).        |
| `submit`                                                                   | List[[models.StepEventActionsSubmit](../models/stepeventactionssubmit.md)] | :heavy_minus_sign:                                                         | Actions to execute when the tool/step is submitted by the LLM.             |