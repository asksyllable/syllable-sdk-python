# ToolParameterTransformAction

The action to perform on the tool parameter value: `default` means only set the value (using the `format` field) if the parameter doesn't exist or is empty, `override` means always set the value," and `remove` means "remove the parameter value."

## Example Usage

```python
from syllable_sdk.models import ToolParameterTransformAction

value = ToolParameterTransformAction.DEFAULT
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DEFAULT`  | default    |
| `OVERRIDE` | override   |
| `REMOVE`   | remove     |