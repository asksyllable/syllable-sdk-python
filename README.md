# syllable-sdk-python
<!-- Start Summary [summary] -->
## Summary

SyllableSDK: 
# Syllable Platform SDK

Syllable SDK gives you the power of awesome AI agentry. 🚀

## Overview

The Syllable SDK provides a comprehensive set of tools and APIs to integrate powerful AI  
capabilities into your communication applications. Whether you're building chatbots, virtual
assistants, or any other AI-driven solutions, Syllable SDK has got you covered.

## Features

- **Natural Language Processing (NLP)**: Understand and generate human language with ease.
- **Machine Learning Models**: Leverage pre-trained models or train your own custom models.
- **Speech Recognition**: Convert speech to text and vice versa.
- **Data Analytics**: Analyze and visualize data to gain insights.
- **Integration**: Seamlessly integrate with other services and platforms.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [syllable-sdk-python](#syllable-sdk-python)
* [Syllable Platform SDK](#syllable-platform-sdk)
  * [Overview](#overview)
  * [Features](#features)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/asksyllable/syllable-sdk-python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/asksyllable/syllable-sdk-python.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from syllable-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "syllable-sdk",
# ]
# ///

from syllable_sdk import SyllableSDK

sdk = SyllableSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type   | Scheme  | Environment Variable         |
| ---------------- | ------ | ------- | ---------------------------- |
| `api_key_header` | apiKey | API key | `SYLLABLESDK_API_KEY_HEADER` |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [agents](docs/sdks/agents/README.md)

* [list](docs/sdks/agents/README.md#list) - Agent List
* [create](docs/sdks/agents/README.md#create) - Create Agent
* [update](docs/sdks/agents/README.md#update) - Update Agent
* [get_by_id](docs/sdks/agents/README.md#get_by_id) - Get Agent By Id
* [delete](docs/sdks/agents/README.md#delete) - Delete Agent
* [get_available_voices](docs/sdks/agents/README.md#get_available_voices) - Get Available Agent Voices

#### [agents.test](docs/sdks/test/README.md)

* [send_message](docs/sdks/test/README.md#send_message) - Send New Message

### [channels](docs/sdks/channels/README.md)

* [list](docs/sdks/channels/README.md#list) - Get Channels
* [list_targets](docs/sdks/channels/README.md#list_targets) - Get Channel Targets
* [assign_target](docs/sdks/channels/README.md#assign_target) - Assign A Channel Target
* [delete](docs/sdks/channels/README.md#delete) - Delete Channel Target

#### [channels.targets](docs/sdks/targets/README.md)

* [get](docs/sdks/targets/README.md#get) - Get A Channel Target
* [update](docs/sdks/targets/README.md#update) - Edit Channel Target

### [channels_targets](docs/sdks/channelstargets/README.md)

* [list_available](docs/sdks/channelstargets/README.md#list_available) - Available Targets List

### [conversations](docs/sdks/conversations/README.md)

* [list](docs/sdks/conversations/README.md#list) - Conversations List

### [custom_messages](docs/sdks/custommessages/README.md)

* [list](docs/sdks/custommessages/README.md#list) - Custom Messages List
* [create](docs/sdks/custommessages/README.md#create) - Create Custom Message
* [update](docs/sdks/custommessages/README.md#update) - Update Custom Message
* [get](docs/sdks/custommessages/README.md#get) - Get Custom Message By Id
* [delete](docs/sdks/custommessages/README.md#delete) - Delete Custom Message

### [dashboards](docs/sdks/dashboards/README.md)

* [list](docs/sdks/dashboards/README.md#list) - Post List Dashboards
* [fetch_info](docs/sdks/dashboards/README.md#fetch_info) - Post Fetch Info
* [~~session_events~~](docs/sdks/dashboards/README.md#session_events) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary~~](docs/sdks/dashboards/README.md#post_session_summary) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers~~](docs/sdks/dashboards/README.md#post_session_transfers) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions~~](docs/sdks/dashboards/README.md#post_sessions) - Post Sessions :warning: **Deprecated**

### [data_sources](docs/sdks/datasources/README.md)

* [list](docs/sdks/datasources/README.md#list) - List Data Sources
* [create](docs/sdks/datasources/README.md#create) - Create Data Source
* [update](docs/sdks/datasources/README.md#update) - Update Data Source
* [get](docs/sdks/datasources/README.md#get) - Get Data Source
* [delete](docs/sdks/datasources/README.md#delete) - Delete Data Source

### [events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - Events List

### [insights](docs/sdks/insights/README.md)


#### [insights.tools](docs/sdks/insightstools/README.md)

* [create](docs/sdks/insightstools/README.md#create) - Create Insight Tool
* [get_definitions](docs/sdks/insightstools/README.md#get_definitions) - Get Insight Tool Definitions

#### [insights.workflows](docs/sdks/workflows/README.md)

* [update](docs/sdks/workflows/README.md#update) - Update Insights Workflow

### [insights_tools](docs/sdks/insightstools/README.md)

* [list](docs/sdks/insightstools/README.md#list) - Insight Tool List
* [get](docs/sdks/insightstools/README.md#get) - Get Insight Tool By Id
* [update](docs/sdks/insightstools/README.md#update) - Update Insights Tool

### [insights_workflows](docs/sdks/insightsworkflows/README.md)

* [list](docs/sdks/insightsworkflows/README.md#list) - Insight Workflow List
* [create](docs/sdks/insightsworkflows/README.md#create) - Create Insight Workflow
* [get](docs/sdks/insightsworkflows/README.md#get) - Get Insight Workflow By Id
* [delete](docs/sdks/insightsworkflows/README.md#delete) - Delete Insights Workflow

### [language_groups](docs/sdks/languagegroups/README.md)

* [list](docs/sdks/languagegroups/README.md#list) - List Language Groups
* [create](docs/sdks/languagegroups/README.md#create) - Create Language Group
* [update](docs/sdks/languagegroups/README.md#update) - Update Language Group
* [get_by_id](docs/sdks/languagegroups/README.md#get_by_id) - Get Language Group
* [delete](docs/sdks/languagegroups/README.md#delete) - Delete Language Group

### [prompts](docs/sdks/prompts/README.md)

* [list](docs/sdks/prompts/README.md#list) - Prompt List
* [create](docs/sdks/prompts/README.md#create) - Create Prompt
* [update](docs/sdks/prompts/README.md#update) - Update Prompt
* [get_by_id](docs/sdks/prompts/README.md#get_by_id) - Get Prompt By Id
* [delete](docs/sdks/prompts/README.md#delete) - Delete Prompt
* [history](docs/sdks/prompts/README.md#history) - Get Prompt History

### [services](docs/sdks/services/README.md)

* [list](docs/sdks/services/README.md#list) - Service List
* [create](docs/sdks/services/README.md#create) - Create Service
* [update](docs/sdks/services/README.md#update) - Update Service
* [get](docs/sdks/services/README.md#get) - Get Service By Id
* [delete](docs/sdks/services/README.md#delete) - Delete Service

### [session_labels](docs/sdks/sessionlabels/README.md)

* [get](docs/sdks/sessionlabels/README.md#get) - Get Label By Id
* [create](docs/sdks/sessionlabels/README.md#create) - Create Label
* [list](docs/sdks/sessionlabels/README.md#list) - Session Labels List

### [sessions](docs/sdks/sessions/README.md)

* [list](docs/sdks/sessions/README.md#list) - Sessions List
* [get_full_summary](docs/sdks/sessions/README.md#get_full_summary) - Get Full Session Summary By Id
* [get_by_id](docs/sdks/sessions/README.md#get_by_id) - Get A Single Session By Id
* [stream_recording](docs/sdks/sessions/README.md#stream_recording) - Stream Recording

#### [sessions.recording](docs/sdks/recording/README.md)

* [generate_urls](docs/sdks/recording/README.md#generate_urls) - Generate Recording Urls

#### [sessions.summary](docs/sdks/summary/README.md)

* [get_by_id](docs/sdks/summary/README.md#get_by_id) - Get Session Summary By Id

#### [sessions.transcript](docs/sdks/transcript/README.md)

* [get](docs/sdks/transcript/README.md#get) - Get Session Transcript By Id


### [tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - Tool List
* [create](docs/sdks/tools/README.md#create) - Create Tool
* [update](docs/sdks/tools/README.md#update) - Update Tool
* [get_by_name](docs/sdks/tools/README.md#get_by_name) - Tool Info
* [delete](docs/sdks/tools/README.md#delete) - Delete Tool

### [v1](docs/sdks/v1/README.md)

* [list](docs/sdks/v1/README.md#list) - Post List Dashboards
* [fetch_info](docs/sdks/v1/README.md#fetch_info) - Post Fetch Info
* [~~session_events~~](docs/sdks/v1/README.md#session_events) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary~~](docs/sdks/v1/README.md#post_session_summary) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers~~](docs/sdks/v1/README.md#post_session_transfers) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions~~](docs/sdks/v1/README.md#post_sessions) - Post Sessions :warning: **Deprecated**

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| models.HTTPValidationError | 422         | application/json |
| models.APIError            | 4XX, 5XX    | \*/\*            |

### Example

```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:
    res = None
    try:

        res = ss_client.agents.list()

        # Handle response
        print(res)

    except models.HTTPValidationError as e:
        # handle e.data: models.HTTPValidationErrorData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    server_url="https://api.syllable.cloud",
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from syllable_sdk import SyllableSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SyllableSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from syllable_sdk import SyllableSDK
from syllable_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SyllableSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SyllableSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from syllable_sdk import SyllableSDK
def main():

    with SyllableSDK(
        api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
    ) as ss_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SyllableSDK(
        api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
    ) as ss_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from syllable_sdk import SyllableSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SyllableSDK(debug_logger=logging.getLogger("syllable_sdk"))
```

You can also enable a default debug logger by setting an environment variable `SYLLABLESDK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
