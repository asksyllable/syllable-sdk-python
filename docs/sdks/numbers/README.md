# Channels.Twilio.Numbers

## Overview

Operations related to setting up phone numbers in Twilio for use in           channels.

### Available Operations

* [channels_twilio_numbers_a2p_compliance_check](#channels_twilio_numbers_a2p_compliance_check) - Verify Twilio Us A2P Compliance
* [add](#add) - Add Twilio Number
* [update](#update) - Update Twilio Number
* [list](#list) - List Twilio Phone Numbers

## channels_twilio_numbers_a2p_compliance_check

Return whether Twilio shows this number on a US A2P messaging path with an approved brand.

### Example Usage

<!-- UsageSnippet language="python" operationID="channels_twilio_numbers_a2p_compliance_check" method="post" path="/api/v1/channels/twilio/{channel_id}/numbers/verify-a2p-compliance" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.twilio.numbers.channels_twilio_numbers_a2p_compliance_check(channel_id=661482, a2p_messaging_path_check_request={
        "phone": "+18042221111",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `channel_id`                                                                        | *int*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `a2p_messaging_path_check_request`                                                  | [models.A2pMessagingPathCheckRequest](../../models/a2pmessagingpathcheckrequest.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.A2pMessagingPathCheckResponse](../../models/a2pmessagingpathcheckresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## add

Purchase a Twilio number and associate it with a channel.

### Example Usage

<!-- UsageSnippet language="python" operationID="channels_twilio_numbers_add" method="post" path="/api/v1/channels/twilio/{channel_id}/numbers" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.twilio.numbers.add(channel_id=314558, twilio_number_add_request={
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
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a Twilio number and associate it with a channel.

### Example Usage

<!-- UsageSnippet language="python" operationID="channels_twilio_numbers_update" method="put" path="/api/v1/channels/twilio/{channel_id}/numbers" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.twilio.numbers.update(channel_id=815949, twilio_number_update_request={
        "friendly_name": "Support Line",
        "phone_sid": "PN123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `channel_id`                                                                  | *int*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `twilio_number_update_request`                                                | [models.TwilioNumberUpdateRequest](../../models/twilionumberupdaterequest.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.TwilioNumberUpdateResponse](../../models/twilionumberupdateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

List Twilio phone numbers.

### Example Usage

<!-- UsageSnippet language="python" operationID="channels_twilio_numbers_list" method="get" path="/api/v1/channels/twilio/{channel_id}/numbers" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.channels.twilio.numbers.list(channel_id=739627)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `channel_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TwilioListNumbersResponse](../../models/twiliolistnumbersresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |