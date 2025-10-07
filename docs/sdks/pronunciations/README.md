# Pronunciations
(*pronunciations*)

## Overview

### Available Operations

* [pronunciations_upload_csv](#pronunciations_upload_csv) - Upload Pronunciations Csv

## pronunciations_upload_csv

Upload Pronunciations Csv

### Example Usage

<!-- UsageSnippet language="python" operationID="pronunciations_upload_csv" method="post" path="/api/v1/pronunciations/csv" -->
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.pronunciations.pronunciations_upload_csv(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.BodyPronunciationsUploadCsv](../../models/bodypronunciationsuploadcsv.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.PronunciationsCsvUploadResponse](../../models/pronunciationscsvuploadresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |