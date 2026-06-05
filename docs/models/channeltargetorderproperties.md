# ChannelTargetOrderProperties

Subset of [[ChannelTargetProperties]] that is valid as ``order_by``. Filter-only fields are
excluded so the generated OpenAPI client does not surface them as sortable.

## Example Usage

```python
from syllable_sdk.models import ChannelTargetOrderProperties

value = ChannelTargetOrderProperties.ID
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `ID`              | id                |
| `CHANNEL_ID`      | channel_id        |
| `CHANNEL_NAME`    | channel_name      |
| `AGENT_ID`        | agent_id          |
| `TARGET`          | target            |
| `TARGET_MODE`     | target_mode       |
| `FALLBACK_TARGET` | fallback_target   |
| `IS_TEST`         | is_test           |
| `UPDATED_AT`      | updated_at        |
| `A2P_VERIFIED`    | a2p_verified      |