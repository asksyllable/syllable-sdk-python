# syllable-sdk-python
<!-- Start Summary [summary] -->
## Summary

SyllableSDK: 
# Syllable Platform SDK

Syllable SDK gives you the power of awesome AI agentry. 🚀

## Overview

The Syllable SDK provides a comprehensive set of tools and APIs to integrate powerful AI
capabilities into your communication applications. Whether you're building phone agents, chatbots,
virtual assistants, or any other AI-driven solutions, Syllable SDK has got you covered.

## Features

- **Agent Configuration**: Create and manage agents that can interact with users across various 
channels.
- **Channel Management**: Configure channels like SMS, web chat, and more to connect agents with 
users.
- **Custom Messages**: Set up custom messages that agents can deliver as greetings or responses.
- **Conversations**: Track and manage conversations between users and agents, including session 
management.
- **Tools and Workflows**: Leverage tools and workflows to enhance agent capabilities, such as data 
processing and API calls.
- **Data Sources**: Integrate data sources to provide agents with additional context and 
information.
- **Insights and Analytics**: Analyze conversations and sessions to gain insights into user 
interactions.
- **Permissions and Security**: Manage permissions to control access to various features and 
functionalities.
- **Language Support**: Define language groups to enable multilingual support for agents.
- **Outbound Campaigns**: Create and manage outbound communication campaigns to reach users 
effectively.
- **Session Labels**: Label sessions with evaluations of quality and descriptions of issues 
encountered.
- **Incident Management**: Track and manage incidents related to agent interactions.
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
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

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
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, limit=25, search_fields=[
        models.AgentProperties.NAME,
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
from syllable_sdk import SyllableSDK, models

async def main():

    async with SyllableSDK(
        api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
    ) as ss_client:

        res = await ss_client.agents.list_async(page=0, limit=25, search_fields=[
            models.AgentProperties.NAME,
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
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, limit=25, search_fields=[
        models.AgentProperties.NAME,
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

### [agents](docs/sdks/agents/README.md)

* [list](docs/sdks/agents/README.md#list) - Agent List
* [create](docs/sdks/agents/README.md#create) - Create Agent
* [update](docs/sdks/agents/README.md#update) - Update Agent
* [get_by_id](docs/sdks/agents/README.md#get_by_id) - Get Agent By Id
* [delete](docs/sdks/agents/README.md#delete) - Delete Agent
* [agent_get_available_voices](docs/sdks/agents/README.md#agent_get_available_voices) - Get Available Agent Voices

#### [agents.test](docs/sdks/test/README.md)

* [send_test_message](docs/sdks/test/README.md#send_test_message) - Send New Message

### [channels](docs/sdks/channels/README.md)

* [list](docs/sdks/channels/README.md#list) - Get Channels
* [delete](docs/sdks/channels/README.md#delete) - Delete Channel Target

#### [channels.targets](docs/sdks/targets/README.md)

* [available_targets](docs/sdks/targets/README.md#available_targets) - Available Targets List
* [list](docs/sdks/targets/README.md#list) - Get Channel Targets
* [create](docs/sdks/targets/README.md#create) - Assign A Channel Target
* [get_by_id](docs/sdks/targets/README.md#get_by_id) - Get A Channel Target
* [update](docs/sdks/targets/README.md#update) - Edit Channel Target

#### [channels.twilio](docs/sdks/twilio/README.md)

* [get_by_id](docs/sdks/twilio/README.md#get_by_id) - Get Twilio Channel By Id
* [update](docs/sdks/twilio/README.md#update) - Update Twilio Channel
* [create](docs/sdks/twilio/README.md#create) - Create Twilio Channel

#### [channels.twilio.numbers](docs/sdks/numbers/README.md)

* [add](docs/sdks/numbers/README.md#add) - Add Twilio Number
* [update](docs/sdks/numbers/README.md#update) - Update Twilio Number
* [list](docs/sdks/numbers/README.md#list) - List Twilio Phone Numbers

### [conversations](docs/sdks/conversations/README.md)

* [list](docs/sdks/conversations/README.md#list) - Conversations List

### [custom_messages](docs/sdks/custommessages/README.md)

* [list](docs/sdks/custommessages/README.md#list) - Custom Messages List
* [create](docs/sdks/custommessages/README.md#create) - Create Custom Message
* [update](docs/sdks/custommessages/README.md#update) - Update Custom Message
* [get_by_id](docs/sdks/custommessages/README.md#get_by_id) - Get Custom Message By Id
* [delete](docs/sdks/custommessages/README.md#delete) - Delete Custom Message

### [dashboards](docs/sdks/dashboards/README.md)

* [post_list_dashboard](docs/sdks/dashboards/README.md#post_list_dashboard) - Post List Dashboards
* [post_get_dashboard](docs/sdks/dashboards/README.md#post_get_dashboard) - Post Fetch Info
* [~~post_session_events_dashboard~~](docs/sdks/dashboards/README.md#post_session_events_dashboard) - Post Session Events :warning: **Deprecated**
* [~~post_session_summary_dashboard~~](docs/sdks/dashboards/README.md#post_session_summary_dashboard) - Post Session Summary :warning: **Deprecated**
* [~~post_session_transfers_dashboard~~](docs/sdks/dashboards/README.md#post_session_transfers_dashboard) - Post Session Transfers :warning: **Deprecated**
* [~~post_sessions_dashboard~~](docs/sdks/dashboards/README.md#post_sessions_dashboard) - Post Sessions :warning: **Deprecated**

### [data_sources](docs/sdks/datasources/README.md)

* [list](docs/sdks/datasources/README.md#list) - List Data Sources
* [create](docs/sdks/datasources/README.md#create) - Create Data Source
* [update](docs/sdks/datasources/README.md#update) - Update Data Source
* [get_by_id](docs/sdks/datasources/README.md#get_by_id) - Get Data Source
* [delete](docs/sdks/datasources/README.md#delete) - Delete Data Source

### [events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - Events List

### [incidents](docs/sdks/incidents/README.md)

* [list](docs/sdks/incidents/README.md#list) - List Incidents
* [create](docs/sdks/incidents/README.md#create) - Create Incident
* [update](docs/sdks/incidents/README.md#update) - Update Incident
* [incident_get_organizations](docs/sdks/incidents/README.md#incident_get_organizations) - Get Organizations
* [get_by_id](docs/sdks/incidents/README.md#get_by_id) - Get Incident By Id
* [delete](docs/sdks/incidents/README.md#delete) - Delete Incident

### [insights](docs/sdks/insightssdk/README.md)

* [list](docs/sdks/insightssdk/README.md#list) - Insights List

#### [insights.folders](docs/sdks/folders/README.md)

* [list](docs/sdks/folders/README.md#list) - List Insights Upload Folders
* [create](docs/sdks/folders/README.md#create) - Create Insights Upload Folder
* [get_by_id](docs/sdks/folders/README.md#get_by_id) - Get Insights Folder Details
* [delete](docs/sdks/folders/README.md#delete) - Delete Insights Folder
* [update](docs/sdks/folders/README.md#update) - Update Insights Folder
* [upload_file](docs/sdks/folders/README.md#upload_file) - Upload Insights  Upload Folder
* [list_files](docs/sdks/folders/README.md#list_files) - Fetch Insights Upload Files
* [move_files](docs/sdks/folders/README.md#move_files) - Move Insights Upload Files

#### [insights.tools](docs/sdks/insightstools/README.md)

* [list](docs/sdks/insightstools/README.md#list) - List Insight Tool Configurations
* [create](docs/sdks/insightstools/README.md#create) - Create Insight Tool Configuration
* [get_by_id](docs/sdks/insightstools/README.md#get_by_id) - Get Insight Tool Config By Id
* [delete](docs/sdks/insightstools/README.md#delete) - Delete Insight Tool Configuration
* [update](docs/sdks/insightstools/README.md#update) - Update Insights Tool Configuration
* [insights_tool_test](docs/sdks/insightstools/README.md#insights_tool_test) - Test Insights Tool
* [insight_tool_get_definitions](docs/sdks/insightstools/README.md#insight_tool_get_definitions) - Get Insight Tool Definitions

#### [insights.workflows](docs/sdks/workflows/README.md)

* [list](docs/sdks/workflows/README.md#list) - Insight Workflow List
* [create](docs/sdks/workflows/README.md#create) - Create Insight Workflow
* [get_by_id](docs/sdks/workflows/README.md#get_by_id) - Get Insight Workflow By Id
* [update](docs/sdks/workflows/README.md#update) - Update Insights Workflow
* [delete](docs/sdks/workflows/README.md#delete) - Delete Insights Workflow
* [inactivate](docs/sdks/workflows/README.md#inactivate) - Inactivate Insights Workflow
* [activate](docs/sdks/workflows/README.md#activate) - Activate Insights Workflow
* [queue_work](docs/sdks/workflows/README.md#queue_work) - Queue Insights Workflow For Sessions/Files

### [language_groups](docs/sdks/languagegroups/README.md)

* [list](docs/sdks/languagegroups/README.md#list) - List Language Groups
* [create](docs/sdks/languagegroups/README.md#create) - Create Language Group
* [update](docs/sdks/languagegroups/README.md#update) - Update Language Group
* [get_by_id](docs/sdks/languagegroups/README.md#get_by_id) - Get Language Group
* [delete](docs/sdks/languagegroups/README.md#delete) - Delete Language Group
* [language_groups_create_voice_sample](docs/sdks/languagegroups/README.md#language_groups_create_voice_sample) - Create Voice Sample

### [organizations](docs/sdks/organizations/README.md)

* [organizations_get](docs/sdks/organizations/README.md#organizations_get) - Get Current Organization
* [update](docs/sdks/organizations/README.md#update) - Update Current Organization
* [create](docs/sdks/organizations/README.md#create) - Create Organization
* [delete](docs/sdks/organizations/README.md#delete) - Delete Current Organization

### [outbound](docs/sdks/outbound/README.md)


#### [outbound.batches](docs/sdks/batches/README.md)

* [list](docs/sdks/batches/README.md#list) - List Outbound Communication Batches
* [create](docs/sdks/batches/README.md#create) - Create Outbound Communication Batch
* [get_by_id](docs/sdks/batches/README.md#get_by_id) - Get Outbound Communication Batch
* [update](docs/sdks/batches/README.md#update) - Update Outbound Communication Batch
* [delete](docs/sdks/batches/README.md#delete) - Delete Outbound Communication Batch
* [upload](docs/sdks/batches/README.md#upload) - Upload Outbound Communication Batch
* [results](docs/sdks/batches/README.md#results) - Fetch Outbound Communication Batch Results
* [add](docs/sdks/batches/README.md#add) - Create Outbound Communication Request
* [remove](docs/sdks/batches/README.md#remove) - Delete Requests By List Of Reference Ids

#### [outbound.campaigns](docs/sdks/campaigns/README.md)

* [list](docs/sdks/campaigns/README.md#list) - List Outbound Communication Campaigns
* [create](docs/sdks/campaigns/README.md#create) - Create Outbound Communication Campaign
* [get_by_id](docs/sdks/campaigns/README.md#get_by_id) - Get Outbound Communication Campaign
* [update](docs/sdks/campaigns/README.md#update) - Update Outbound Communication Campaign
* [delete](docs/sdks/campaigns/README.md#delete) - Delete Outbound Communication Campaign

### [permissions](docs/sdks/permissions/README.md)

* [list](docs/sdks/permissions/README.md#list) - List Permissions

### [prompts](docs/sdks/prompts/README.md)

* [list](docs/sdks/prompts/README.md#list) - Prompt List
* [create](docs/sdks/prompts/README.md#create) - Create Prompt
* [update](docs/sdks/prompts/README.md#update) - Update Prompt
* [get_by_id](docs/sdks/prompts/README.md#get_by_id) - Get Prompt By Id
* [delete](docs/sdks/prompts/README.md#delete) - Delete Prompt
* [prompts_history](docs/sdks/prompts/README.md#prompts_history) - Get Prompt History
* [prompt_get_supported_llms](docs/sdks/prompts/README.md#prompt_get_supported_llms) - Get Supported Llm Configs

### [roles](docs/sdks/roles/README.md)

* [list](docs/sdks/roles/README.md#list) - List Roles
* [create](docs/sdks/roles/README.md#create) - Create Role
* [update](docs/sdks/roles/README.md#update) - Update Role
* [get_by_id](docs/sdks/roles/README.md#get_by_id) - Get Role
* [delete](docs/sdks/roles/README.md#delete) - Delete Role

### [services](docs/sdks/services/README.md)

* [list](docs/sdks/services/README.md#list) - Service List
* [create](docs/sdks/services/README.md#create) - Create Service
* [update](docs/sdks/services/README.md#update) - Update Service
* [get_by_id](docs/sdks/services/README.md#get_by_id) - Get Service By Id
* [delete](docs/sdks/services/README.md#delete) - Delete Service

### [session_debug](docs/sdks/sessiondebug/README.md)

* [get_session_data_by_sid](docs/sdks/sessiondebug/README.md#get_session_data_by_sid) - Get Session Data By Sid
* [get_session_data_by_session_id](docs/sdks/sessiondebug/README.md#get_session_data_by_session_id) - Get Session Data By Session Id
* [get_session_tool_call_result_by_id](docs/sdks/sessiondebug/README.md#get_session_tool_call_result_by_id) - Get Session Tool Call Result By Id

### [session_labels](docs/sdks/sessionlabels/README.md)

* [get_by_id](docs/sdks/sessionlabels/README.md#get_by_id) - Get Label By Id
* [create](docs/sdks/sessionlabels/README.md#create) - Create Label
* [list](docs/sdks/sessionlabels/README.md#list) - Session Labels List

### [sessions](docs/sdks/sessions/README.md)

* [list](docs/sdks/sessions/README.md#list) - Sessions List
* [get_by_id](docs/sdks/sessions/README.md#get_by_id) - Get A Single Session By Id
* [generate_session_recording_urls](docs/sdks/sessions/README.md#generate_session_recording_urls) - Generate Recording Urls
* [session_recording_stream](docs/sdks/sessions/README.md#session_recording_stream) - Stream Recording

#### [sessions.full_summary](docs/sdks/fullsummary/README.md)

* [get_by_id](docs/sdks/fullsummary/README.md#get_by_id) - Get Full Session Summary By Id

#### [sessions.latency](docs/sdks/latency/README.md)

* [get_by_id](docs/sdks/latency/README.md#get_by_id) - Inspect Latency For Session

#### [sessions.transcript](docs/sdks/transcript/README.md)

* [get_by_id](docs/sdks/transcript/README.md#get_by_id) - Get Session Transcript By Id


### [takeouts](docs/sdks/takeouts/README.md)

* [create](docs/sdks/takeouts/README.md#create) - Create Takeout
* [takeouts_get_by_job_id](docs/sdks/takeouts/README.md#takeouts_get_by_job_id) - Get Takeout
* [takeouts_get_file](docs/sdks/takeouts/README.md#takeouts_get_file) - Get File

### [tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - Tool List
* [create](docs/sdks/tools/README.md#create) - Create Tool
* [update](docs/sdks/tools/README.md#update) - Update Tool
* [get_by_name](docs/sdks/tools/README.md#get_by_name) - Tool Info
* [delete](docs/sdks/tools/README.md#delete) - Delete Tool

### [users](docs/sdks/users/README.md)

* [list](docs/sdks/users/README.md#list) - List Users
* [create](docs/sdks/users/README.md#create) - Create User
* [update](docs/sdks/users/README.md#update) - Update User
* [delete](docs/sdks/users/README.md#delete) - Delete User
* [users_get_by_email](docs/sdks/users/README.md#users_get_by_email) - Get User
* [users_send_email](docs/sdks/users/README.md#users_send_email) - Send User Email
* [users_delete_account](docs/sdks/users/README.md#users_delete_account) - Request Removal Of This Account

### [v1](docs/sdks/v1/README.md)

* [list](docs/sdks/v1/README.md#list) - List Users
* [create](docs/sdks/v1/README.md#create) - Create User
* [update](docs/sdks/v1/README.md#update) - Update User
* [delete](docs/sdks/v1/README.md#delete) - Delete User
* [users_get_by_email](docs/sdks/v1/README.md#users_get_by_email) - Get User
* [users_send_email](docs/sdks/v1/README.md#users_send_email) - Send User Email
* [users_delete_account](docs/sdks/v1/README.md#users_delete_account) - Request Removal Of This Account

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.insights.folders.upload_file(folder_id=444923, call_id="<id>")

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from syllable_sdk import SyllableSDK, models
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, limit=25, search_fields=[
        models.AgentProperties.NAME,
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
from syllable_sdk import SyllableSDK, models
from syllable_sdk.utils import BackoffStrategy, RetryConfig


with SyllableSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, limit=25, search_fields=[
        models.AgentProperties.NAME,
    ], search_field_values=[
        "Some Object Name",
    ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SyllableSDKError`](./src/syllable_sdk/errors/syllablesdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import os
from syllable_sdk import SyllableSDK, errors, models


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:
    res = None
    try:

        res = ss_client.agents.list(page=0, limit=25, search_fields=[
            models.AgentProperties.NAME,
        ], search_field_values=[
            "Some Object Name",
        ], start_datetime="2023-01-01T00:00:00Z", end_datetime="2024-01-01T00:00:00Z")

        # Handle response
        print(res)


    except errors.SyllableSDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.HTTPValidationError):
            print(e.data.detail)  # Optional[List[models.ValidationError]]
```

### Error Classes
**Primary errors:**
* [`SyllableSDKError`](./src/syllable_sdk/errors/syllablesdkerror.py): The base class for HTTP error responses.
  * [`HTTPValidationError`](./src/syllable_sdk/errors/httpvalidationerror.py): Validation Error. Status code `422`. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SyllableSDKError`](./src/syllable_sdk/errors/syllablesdkerror.py)**:
* [`ResponseValidationError`](./src/syllable_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from syllable_sdk import SyllableSDK, models


with SyllableSDK(
    server_url="https://api.syllable.cloud",
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.list(page=0, limit=25, search_fields=[
        models.AgentProperties.NAME,
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
