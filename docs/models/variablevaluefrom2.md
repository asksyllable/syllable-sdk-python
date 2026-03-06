# VariableValuefrom2

Expression that computes the value. Supported expression forms: (1) JMESPath string (default for plain strings), (2) typed JMESPath object {"type":"jp"|"jmespath","expression":"..."}, or (3) typed CEL object {"type":"cel","expression":"..."}. Mutually exclusive with value.


## Supported Types

### `models.VariableValuefrom1`

```python
value: models.VariableValuefrom1 = /* values here */
```

### `models.CaseExpression`

```python
value: models.CaseExpression = /* values here */
```

### `str`

```python
value: str = /* values here */
```

