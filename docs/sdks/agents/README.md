# Agents
(*agents*)

## Overview

Operations related to agent configuration. When a user interacts with the           Syllable system, they do so by communicating with an agent.           An agent is linked to a prompt, a custom message, and one or more channel targets to           define its behavior and capabilities. For more information, see           [Console docs](https://docs.syllable.ai/workspaces/Agents).

### Available Operations

* [list](#list) - Agent List
* [create](#create) - Create Agent
* [update](#update) - Update Agent
* [get_by_id](#get_by_id) - Get Agent By Id
* [delete](#delete) - Delete Agent
* [agent_get_available_voices](#agent_get_available_voices) - Get Available Agent Voices

## list

List the existing agents

### Example Usage

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

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            | Example                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The page number from which to start (0-indexed)                                                                                                        | 0                                                                                                                                                      |
| `limit`                                                                                                                                                | *Optional[int]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | The maximum number of items to return                                                                                                                  | 25                                                                                                                                                     |
| `search_fields`                                                                                                                                        | List[[models.AgentProperties](../../models/agentproperties.md)]                                                                                        | :heavy_minus_sign:                                                                                                                                     | String names of fields to search. Correspond by index to search field values                                                                           | name                                                                                                                                                   |
| `search_field_values`                                                                                                                                  | List[*str*]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                     | Values of fields to search. Correspond by index to search fields. Unless field name contains "list", an individual search field value cannot be a list | Some Object Name                                                                                                                                       |
| `order_by`                                                                                                                                             | [OptionalNullable[models.AgentProperties]](../../models/agentproperties.md)                                                                            | :heavy_minus_sign:                                                                                                                                     | The field whose value should be used to order the results                                                                                              |                                                                                                                                                        |
| `order_by_direction`                                                                                                                                   | [OptionalNullable[models.OrderByDirection]](../../models/orderbydirection.md)                                                                          | :heavy_minus_sign:                                                                                                                                     | The direction in which to order the results                                                                                                            |                                                                                                                                                        |
| `fields`                                                                                                                                               | List[[models.AgentProperties](../../models/agentproperties.md)]                                                                                        | :heavy_minus_sign:                                                                                                                                     | The fields to include in the response                                                                                                                  |                                                                                                                                                        |
| `start_datetime`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The start datetime for filtering results                                                                                                               | 2023-01-01T00:00:00Z                                                                                                                                   |
| `end_datetime`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                     | The end datetime for filtering results                                                                                                                 | 2024-01-01T00:00:00Z                                                                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |                                                                                                                                                        |

### Response

**[models.ListResponseAgentResponse](../../models/listresponseagentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new agent

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.create(name="<value>", type_="ca_v1", prompt_id=486589, custom_message_id=638424, timezone="America/New_York", variables={

    }, tool_headers={
        "key": "<value>",
        "key1": "<value>",
    }, stt_provider=syllable_sdk.AgentSttProvider.GOOGLE_STT_V2, wait_sound=syllable_sdk.AgentWaitSound.KEYBOARD_1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The agent name                                                                                                                                                        |                                                                                                                                                                       |
| `type`                                                                                                                                                                | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The agent type. Can be an arbitrary string                                                                                                                            | ca_v1                                                                                                                                                                 |
| `prompt_id`                                                                                                                                                           | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | ID of the prompt associated with the agent                                                                                                                            |                                                                                                                                                                       |
| `custom_message_id`                                                                                                                                                   | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | ID of the custom message that should be delivered at the beginning of a conversation with the agent                                                                   |                                                                                                                                                                       |
| `timezone`                                                                                                                                                            | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The time zone in which the agent operates                                                                                                                             | America/New_York                                                                                                                                                      |
| `variables`                                                                                                                                                           | Dict[str, *str*]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                    | Custom context variables for the conversation session. Keys should be prefixed with "vars.".                                                                          |                                                                                                                                                                       |
| `tool_headers`                                                                                                                                                        | Dict[str, *str*]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                    | Optional headers to include in tool calls for agent.                                                                                                                  |                                                                                                                                                                       |
| `description`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | The agent description                                                                                                                                                 |                                                                                                                                                                       |
| `label`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | The agent label                                                                                                                                                       |                                                                                                                                                                       |
| `language_group_id`                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | ID of the language group associated with the agent                                                                                                                    |                                                                                                                                                                       |
| `prompt_tool_defaults`                                                                                                                                                | List[[models.AgentToolDefaults](../../models/agenttooldefaults.md)]                                                                                                   | :heavy_minus_sign:                                                                                                                                                    | User-configured parameter values for the agent's tools                                                                                                                |                                                                                                                                                                       |
| `languages`                                                                                                                                                           | List[*str*]                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>BCP 47 codes of languages the agent supports | [<br/>"en-US",<br/>"es-US"<br/>]                                                                                                                                      |
| `agent_initiated`                                                                                                                                                     | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Whether the agent initiates conversation with a user after the custom message is delivered                                                                            |                                                                                                                                                                       |
| `stt_provider`                                                                                                                                                        | [OptionalNullable[models.AgentSttProvider]](../../models/agentsttprovider.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                    | Speech-to-text provider for the agent.                                                                                                                                | Google STT V1                                                                                                                                                         |
| `wait_sound`                                                                                                                                                          | [OptionalNullable[models.AgentWaitSound]](../../models/agentwaitsound.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                    | Sound to play while waiting for a response from the LLM.                                                                                                              | No Sound                                                                                                                                                              |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |

### Response

**[models.AgentResponse](../../models/agentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an existing agent

### Example Usage

```python
import os
import syllable_sdk
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.update(name="<value>", type_="ca_v1", prompt_id=857478, custom_message_id=597129, timezone="America/Chicago", variables={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, tool_headers={
        "key": "<value>",
        "key1": "<value>",
    }, id=54062, stt_provider=syllable_sdk.AgentSttProvider.GOOGLE_STT_V2, wait_sound=syllable_sdk.AgentWaitSound.KEYBOARD_1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The agent name                                                                                                                                                        |                                                                                                                                                                       |
| `type`                                                                                                                                                                | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The agent type. Can be an arbitrary string                                                                                                                            | ca_v1                                                                                                                                                                 |
| `prompt_id`                                                                                                                                                           | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | ID of the prompt associated with the agent                                                                                                                            |                                                                                                                                                                       |
| `custom_message_id`                                                                                                                                                   | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | ID of the custom message that should be delivered at the beginning of a conversation with the agent                                                                   |                                                                                                                                                                       |
| `timezone`                                                                                                                                                            | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The time zone in which the agent operates                                                                                                                             | America/New_York                                                                                                                                                      |
| `variables`                                                                                                                                                           | Dict[str, *str*]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                    | Custom context variables for the conversation session. Keys should be prefixed with "vars.".                                                                          |                                                                                                                                                                       |
| `tool_headers`                                                                                                                                                        | Dict[str, *str*]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                    | Optional headers to include in tool calls for agent.                                                                                                                  |                                                                                                                                                                       |
| `id`                                                                                                                                                                  | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The agent ID                                                                                                                                                          |                                                                                                                                                                       |
| `description`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | The agent description                                                                                                                                                 |                                                                                                                                                                       |
| `label`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | The agent label                                                                                                                                                       |                                                                                                                                                                       |
| `language_group_id`                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                    | ID of the language group associated with the agent                                                                                                                    |                                                                                                                                                                       |
| `prompt_tool_defaults`                                                                                                                                                | List[[models.AgentToolDefaults](../../models/agenttooldefaults.md)]                                                                                                   | :heavy_minus_sign:                                                                                                                                                    | User-configured parameter values for the agent's tools                                                                                                                |                                                                                                                                                                       |
| `languages`                                                                                                                                                           | List[*str*]                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>BCP 47 codes of languages the agent supports | [<br/>"en-US",<br/>"es-US"<br/>]                                                                                                                                      |
| `agent_initiated`                                                                                                                                                     | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Whether the agent initiates conversation with a user after the custom message is delivered                                                                            |                                                                                                                                                                       |
| `stt_provider`                                                                                                                                                        | [OptionalNullable[models.AgentSttProvider]](../../models/agentsttprovider.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                    | Speech-to-text provider for the agent.                                                                                                                                | Google STT V1                                                                                                                                                         |
| `wait_sound`                                                                                                                                                          | [OptionalNullable[models.AgentWaitSound]](../../models/agentwaitsound.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                    | Sound to play while waiting for a response from the LLM.                                                                                                              | No Sound                                                                                                                                                              |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |

### Response

**[models.AgentResponse](../../models/agentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_by_id

Get an agent by ID.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.get_by_id(agent_id=931598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentResponse](../../models/agentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete Agent

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.delete(agent_id=545907, reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## agent_get_available_voices

Get available agent voices.

### Example Usage

```python
import os
from syllable_sdk import SyllableSDK


with SyllableSDK(
    api_key_header=os.getenv("SYLLABLESDK_API_KEY_HEADER", ""),
) as ss_client:

    res = ss_client.agents.agent_get_available_voices()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AgentVoice]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |