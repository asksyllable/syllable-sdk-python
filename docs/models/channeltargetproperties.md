# ChannelTargetProperties

Names of channel target fields supported for filtering on the full channel targets list
endpoint. Superset of [[ChannelTargetOrderProperties]] — includes filter-only fields like
``target_mode_list`` that are not valid as ``order_by``.

## Example Usage

```python
from syllable_sdk.models import ChannelTargetProperties

value = ChannelTargetProperties.ID
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `ID`               | id                 |
| `CHANNEL_ID`       | channel_id         |
| `CHANNEL_NAME`     | channel_name       |
| `AGENT_ID`         | agent_id           |
| `TARGET`           | target             |
| `TARGET_MODE`      | target_mode        |
| `TARGET_MODE_LIST` | target_mode_list   |
| `FALLBACK_TARGET`  | fallback_target    |
| `IS_TEST`          | is_test            |
| `UPDATED_AT`       | updated_at         |
| `A2P_VERIFIED`     | a2p_verified       |