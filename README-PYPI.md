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
* [syllable-sdk-python](https://github.com/asksyllable/syllable-sdk-python/blob/master/#syllable-sdk-python)
* [Syllable Platform SDK](https://github.com/asksyllable/syllable-sdk-python/blob/master/#syllable-platform-sdk)
  * [Overview](https://github.com/asksyllable/syllable-sdk-python/blob/master/#overview)
  * [Features](https://github.com/asksyllable/syllable-sdk-python/blob/master/#features)
  * [SDK Installation](https://github.com/asksyllable/syllable-sdk-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/asksyllable/syllable-sdk-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/asksyllable/syllable-sdk-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/asksyllable/syllable-sdk-python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/asksyllable/syllable-sdk-python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/asksyllable/syllable-sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/asksyllable/syllable-sdk-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/asksyllable/syllable-sdk-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/asksyllable/syllable-sdk-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/asksyllable/syllable-sdk-python/blob/master/#resource-management)
  * [Debugging](https://github.com/asksyllable/syllable-sdk-python/blob/master/#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install syllable-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add syllable-sdk
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [agents](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#list) - Agent List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#create) - Create Agent
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#update) - Update Agent
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#get_by_id) - Get Agent By Id
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#delete) - Delete Agent
* [agent_get_available_voices](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/agents/README.md#agent_get_available_voices) - Get Available Agent Voices

#### [agents.test](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/test/README.md)

* [send_test_message](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/test/README.md#send_test_message) - Send New Message

### [channels](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/channels/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/channels/README.md#list) - Get Channels
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/channels/README.md#delete) - Delete Channel Target

#### [channels.targets](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md)

* [available_targets](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md#available_targets) - Available Targets List
* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md#list) - Get Channel Targets
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md#create) - Assign A Channel Target
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md#get_by_id) - Get A Channel Target
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/targets/README.md#update) - Edit Channel Target

### [conversations](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/conversations/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/conversations/README.md#list) - Conversations List

### [custom_messages](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md#list) - Custom Messages List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md#create) - Create Custom Message
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md#update) - Update Custom Message
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md#get_by_id) - Get Custom Message By Id
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/custommessages/README.md#delete) - Delete Custom Message

### [dashboards](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md)

* [post_list_dashboard](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_list_dashboard) - Post List Dashboards
* [post_get_dashboard](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_get_dashboard) - Post Fetch Info
* [~~post_session_events_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_session_events_dashboard) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_session_summary_dashboard) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_session_transfers_dashboard) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/dashboards/README.md#post_sessions_dashboard) - Post Sessions :warning: **Deprecated**

### [data_sources](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md#list) - List Data Sources
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md#create) - Create Data Source
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md#update) - Update Data Source
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md#get_by_id) - Get Data Source
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/datasources/README.md#delete) - Delete Data Source

### [events](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/events/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/events/README.md#list) - Events List

### [insights](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insights/README.md)


#### [insights.tools](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md#list) - Insight Tool List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md#create) - Create Insight Tool
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md#get_by_id) - Get Insight Tool By Id
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md#update) - Update Insights Tool
* [insight_tool_get_definitions](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/insightstools/README.md#insight_tool_get_definitions) - Get Insight Tool Definitions

#### [insights.workflows](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md#list) - Insight Workflow List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md#create) - Create Insight Workflow
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md#get_by_id) - Get Insight Workflow By Id
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md#update) - Update Insights Workflow
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/workflows/README.md#delete) - Delete Insights Workflow

### [language_groups](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md#list) - List Language Groups
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md#create) - Create Language Group
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md#update) - Update Language Group
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md#get_by_id) - Get Language Group
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/languagegroups/README.md#delete) - Delete Language Group

### [prompts](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#list) - Prompt List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#create) - Create Prompt
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#update) - Update Prompt
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#get_by_id) - Get Prompt By Id
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#delete) - Delete Prompt
* [prompts_history](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/prompts/README.md#prompts_history) - Get Prompt History

### [services](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md#list) - Service List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md#create) - Create Service
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md#update) - Update Service
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md#get_by_id) - Get Service By Id
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/services/README.md#delete) - Delete Service

### [session_debug](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessiondebug/README.md)

* [get_session_data_by_sid](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessiondebug/README.md#get_session_data_by_sid) - Get Session Data By Sid
* [get_session_data_by_session_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessiondebug/README.md#get_session_data_by_session_id) - Get Session Data By Session Id
* [get_session_tool_call_result_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessiondebug/README.md#get_session_tool_call_result_by_id) - Get Session Tool Call Result By Id

### [session_labels](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessionlabels/README.md)

* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessionlabels/README.md#get_by_id) - Get Label By Id
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessionlabels/README.md#create) - Create Label
* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessionlabels/README.md#list) - Session Labels List

### [sessions](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessions/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessions/README.md#list) - Sessions List
* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessions/README.md#get_by_id) - Get A Single Session By Id
* [generate_session_recording_urls](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessions/README.md#generate_session_recording_urls) - Generate Recording Urls
* [session_recording_stream](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/sessions/README.md#session_recording_stream) - Stream Recording

#### [sessions.full_summary](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/fullsummary/README.md)

* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/fullsummary/README.md#get_by_id) - Get Full Session Summary By Id

#### [sessions.summary](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/summary/README.md)

* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/summary/README.md#get_by_id) - Get Session Summary By Id

#### [sessions.transcript](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/transcript/README.md)

* [get_by_id](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/transcript/README.md#get_by_id) - Get Session Transcript By Id


### [tools](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md)

* [list](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md#list) - Tool List
* [create](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md#create) - Create Tool
* [update](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md#update) - Update Tool
* [get_by_name](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md#get_by_name) - Tool Info
* [delete](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/tools/README.md#delete) - Delete Tool

### [v1](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md)

* [post_list_dashboard](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_list_dashboard) - Post List Dashboards
* [post_get_dashboard](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_get_dashboard) - Post Fetch Info
* [~~post_session_events_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_session_events_dashboard) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_session_summary_dashboard) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_session_transfers_dashboard) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions_dashboard~~](https://github.com/asksyllable/syllable-sdk-python/blob/master/docs/sdks/v1/README.md#post_sessions_dashboard) - Post Sessions :warning: **Deprecated**

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, search_fields=[
        syllable_sdk.AgentProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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
import syllable_sdk
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:
    res = None
    try:

        res = ss_client.agents.list(page=0, search_fields=[
            syllable_sdk.AgentProperties.NAME,
        ], search_field_values=[
            "Some Object Name",
        ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

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
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    server_url="https://api.syllable.cloud",
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
