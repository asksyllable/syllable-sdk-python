# ReasoningToolMode

Function covers automatic/required selection; forced function selects a named tool.

Parallel function is retained as shorthand for function with parallel calls enabled.

## Example Usage

```python
from syllable_sdk.models import ReasoningToolMode

value = ReasoningToolMode.NONE
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `NONE`              | none                |
| `FUNCTION`          | function            |
| `FORCED_FUNCTION`   | forced_function     |
| `PARALLEL_FUNCTION` | parallel_function   |