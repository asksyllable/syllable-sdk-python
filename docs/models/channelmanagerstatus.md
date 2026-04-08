# ChannelManagerStatus

Status of an outbound communication request (voice, SMS, or email).

## Example Usage

```python
from syllable_sdk.models import ChannelManagerStatus

value = ChannelManagerStatus.PENDING
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `PENDING`            | PENDING              |
| `DUPLICATE`          | DUPLICATE            |
| `INVALID`            | INVALID              |
| `FAILED`             | FAILED               |
| `PROCESSED`          | PROCESSED            |
| `DROPPED`            | DROPPED              |
| `DEFERRED`           | DEFERRED             |
| `BOUNCED`            | BOUNCED              |
| `DELIVERED`          | DELIVERED            |
| `OPENED`             | OPENED               |
| `CLICKED`            | CLICKED              |
| `SPAM_REPORT`        | SPAM_REPORT          |
| `UNSUBSCRIBED`       | UNSUBSCRIBED         |
| `PRIOR_UNSUBSCRIBED` | PRIOR_UNSUBSCRIBED   |
| `PRIOR_SPAM_REPORT`  | PRIOR_SPAM_REPORT    |
| `PRIOR_DROPPED`      | PRIOR_DROPPED        |
| `PRIOR_BOUNCED`      | PRIOR_BOUNCED        |
| `SENT`               | SENT                 |
| `ACCEPTED`           | ACCEPTED             |
| `QUEUED`             | QUEUED               |
| `SENDING`            | SENDING              |
| `UNDELIVERED`        | UNDELIVERED          |
| `DELIVERY_UNKNOWN`   | DELIVERY_UNKNOWN     |
| `DELIVERY_FAILED`    | DELIVERY_FAILED      |
| `IN_PROGRESS`        | IN-PROGRESS          |
| `BUSY`               | BUSY                 |
| `CANCELED`           | CANCELED             |
| `COMPLETED`          | COMPLETED            |
| `NO_ANSWER`          | NO-ANSWER            |
| `MACHINE`            | MACHINE              |
| `HUMAN`              | HUMAN                |
| `UNKNOWN`            | UNKNOWN              |