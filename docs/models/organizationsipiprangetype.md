# OrganizationSipIPRangeType

The type of SIP IP range. Signaling IP ranges are used for SIP signaling traffic (e.g. SIP INVITE,
SIP REFER, SIP OPTIONS, etc.), while media IP ranges are used for SIP media traffic
(audio and video).

## Example Usage

```python
from syllable_sdk.models import OrganizationSipIPRangeType

value = OrganizationSipIPRangeType.SIGNALING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `SIGNALING` | signaling   |
| `MEDIA`     | media       |