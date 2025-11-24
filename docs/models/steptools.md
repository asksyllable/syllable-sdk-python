# StepTools

Configuration for tools available in a step.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `call`                                                                          | *OptionalNullable[bool]*                                                        | :heavy_minus_sign:                                                              | Whether to force immediate tool call without user interaction.                  |
| `allow`                                                                         | List[*str*]                                                                     | :heavy_minus_sign:                                                              | List of allowed tool names for this step.                                       |
| `allow_go_to_step`                                                              | *OptionalNullable[bool]*                                                        | :heavy_minus_sign:                                                              | Whether to expose the go_to_step escape hatch to the LLM. Defaults to disabled. |