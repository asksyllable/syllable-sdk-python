# StartEnum

Controls when the workflow activation lifecycle runs. `auto` activates at session start; `manual` activates on first invocation.

## Example Usage

```python
from syllable_sdk.models import StartEnum

value = StartEnum.AUTO
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `MANUAL` | manual   |