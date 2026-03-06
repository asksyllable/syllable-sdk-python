# SayActionIf2

Condition to decide whether this item executes. Supported expression forms: (1) JMESPath string (default for plain strings), (2) typed JMESPath object {"type":"jp"|"jmespath","expression":"..."}, or (3) typed CEL object {"type":"cel","expression":"..."}. Example JMESPath string: "inputs.can_sign_consent == `true`".


## Supported Types

### `models.SayActionIf1`

```python
value: models.SayActionIf1 = /* values here */
```

### `models.CaseExpression`

```python
value: models.CaseExpression = /* values here */
```

### `str`

```python
value: str = /* values here */
```

