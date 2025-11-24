# Step


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the step.                                 |
| `goal`                                                             | *str*                                                              | :heavy_check_mark:                                                 | The goal of the step.                                              |
| `instructions`                                                     | List[[models.Instruction](../models/instruction.md)]               | :heavy_minus_sign:                                                 | The instructions for the step.                                     |
| `tools`                                                            | [Optional[models.StepTools]](../models/steptools.md)               | :heavy_minus_sign:                                                 | Configuration for tools available in a step.                       |
| `inputs`                                                           | List[[models.InputParameter](../models/inputparameter.md)]         | :heavy_minus_sign:                                                 | The inputs for the step.                                           |
| `on`                                                               | [Optional[models.StepEventActions]](../models/stepeventactions.md) | :heavy_minus_sign:                                                 | Actions to perform when events occur (enter, submit).              |
| `next`                                                             | List[[models.Next](../models/next.md)]                             | :heavy_minus_sign:                                                 | The next steps to execute.                                         |