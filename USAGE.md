<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from syllable_sdk import SyllableSDK

async def main():

    async with SyllableSDK(
        api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
    ) as ss_client:

        res = await ss_client.agents.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->