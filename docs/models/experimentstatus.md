# ExperimentStatus

Status of an experiment.

The column is a varchar and not a database enum, so a new value here does not need a migration.

## Example Usage

```python
from syllable_sdk.models import ExperimentStatus

value = ExperimentStatus.DRAFT
```


## Values

| Name      | Value     |
| --------- | --------- |
| `DRAFT`   | draft     |
| `RUNNING` | running   |
| `STOPPED` | stopped   |