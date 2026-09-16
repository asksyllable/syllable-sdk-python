# ExperimentResultsResponse

What an experiment has collected so far.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `experiment_id`                                                                | *int*                                                                          | :heavy_check_mark:                                                             | The internal ID of the experiment                                              | 1                                                                              |
| `variants`                                                                     | List[[models.ExperimentVariantResult](../models/experimentvariantresult.md)]   | :heavy_check_mark:                                                             | The variants of the experiment, in the same order as the experiment lists them |                                                                                |