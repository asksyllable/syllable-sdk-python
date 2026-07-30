# From2

Expression evaluated against the parsed tool response body (the JSON the external tool returned). Supported forms: (1) JMESPath string (default for plain strings) — a bare field name for raw passthrough, or a boolean/computed expression for derived values, (2) typed JMESPath object {"type":"jp"|"jmespath","expression":"..."}, or (3) typed CEL object {"type":"cel","expression":"..."}.


## Supported Types

### `models.From1`

```python
value: models.From1 = /* values here */
```

### `models.CaseExpression`

```python
value: models.CaseExpression = /* values here */
```

### `str`

```python
value: str = /* values here */
```

