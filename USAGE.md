<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, search_fields=[
        syllable_sdk.AgentProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import syllable_sdk
from syllable_sdk import SyllableSDK

async def main():

    async with SyllableSDK(
        api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
    ) as ss_client:

        res = await ss_client.agents.list_async(page=0, search_fields=[
            syllable_sdk.AgentProperties.NAME,
        ], search_field_values=[
            "Some Object Name",
        ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->