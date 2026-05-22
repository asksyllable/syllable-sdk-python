# Organizations.SipIpRanges

## Overview

### Available Operations

* [list](#list) - List Organization Sip Ip Ranges
* [create](#create) - Create Organization Sip Ip Range
* [update](#update) - Update Organization Sip Ip Range
* [delete](#delete) - Delete Organization Sip Ip Range

## list

List SIP signaling/media IP ranges for the current organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="organization_sip_ip_ranges_list" method="get" path="/api/v1/organizations/sip_ip_ranges/" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.organizations.sip_ip_ranges.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.OrganizationSipIPRange]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create an unverified SIP signaling/media IP range for the current organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="organization_sip_ip_ranges_create" method="post" path="/api/v1/organizations/sip_ip_ranges/" -->
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.organizations.sip_ip_ranges.create(request={
        "type": models.OrganizationSipIPRangeType.MEDIA,
        "ip_range": "192.168.1.0/24",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.OrganizationSipIPRangeCreate](../../models/organizationsipiprangecreate.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.OrganizationSipIPRange](../../models/organizationsipiprange.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a SIP IP range. The verified status is managed by Syllable only.

### Example Usage

<!-- UsageSnippet language="python" operationID="organization_sip_ip_ranges_update" method="put" path="/api/v1/organizations/sip_ip_ranges/{sip_ip_range_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.organizations.sip_ip_ranges.update(sip_ip_range_id=165372, organization_sip_ip_range_update={
        "ip_range": "192.168.1.0/24",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `sip_ip_range_id`                                                                   | *int*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `organization_sip_ip_range_update`                                                  | [models.OrganizationSipIPRangeUpdate](../../models/organizationsipiprangeupdate.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.OrganizationSipIPRange](../../models/organizationsipiprange.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a SIP signaling/media IP range for the current organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="organization_sip_ip_ranges_delete" method="delete" path="/api/v1/organizations/sip_ip_ranges/{sip_ip_range_id}" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    ss_client.organizations.sip_ip_ranges.delete(sip_ip_range_id=394521)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sip_ip_range_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |