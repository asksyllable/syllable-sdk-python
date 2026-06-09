# LineTypeBucket

Friendly line-type buckets a campaign can be restricted to dial.

These map to raw Twilio Lookup v2 line types via
``lib.twilio.line_type_lookup.LINE_TYPE_BUCKETS``.

## Example Usage

```python
from syllable_sdk.models import LineTypeBucket

value = LineTypeBucket.MOBILE
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `MOBILE`   | mobile     |
| `LANDLINE` | landline   |
| `VOIP`     | voip       |