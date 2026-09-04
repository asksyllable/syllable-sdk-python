# OnUnknown

Whether to dial requests whose enrichment is unresolved (no lookup data). Applied per rule: it decides what a rule contributes when *that rule's* attribute is unresolved, and never overrides a rule the request definitively failed -- so a request that fails one rule is still skipped even if a different rule's attribute is missing. "Unresolved" covers a missing value and also the value Twilio returns to mean "looked up, could not answer": for line_type that is 'unknown' (a valid number whose line type it could not determine), and for caller_type both no CNAM data at all (non-US numbers) and 'UNDETERMINED' (a US number it looked up but could not classify).

## Example Usage

```python
from syllable_sdk.models import OnUnknown

value = OnUnknown.INCLUDE
```


## Values

| Name      | Value     |
| --------- | --------- |
| `INCLUDE` | include   |
| `EXCLUDE` | exclude   |