# Numbers
(*channels.twilio.numbers*)

## Overview

Operations related to setting up phone numbers in Twilio for use in           channels.

### Available Operations

* [add](#add) - Add Twilio Number

## add

Purchase a Twilio number and associate it with a channel.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.twilio.numbers.add(channel_id=551477, twilio_number_add_request={
        "friendly_name": "Support Line",
        "area_code": "804",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `channel_id`                                                            | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `twilio_number_add_request`                                             | [models.TwilioNumberAddRequest](../../models/twilionumberaddrequest.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.TwilioNumberAddResponse](../../models/twilionumberaddresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |