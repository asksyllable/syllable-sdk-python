"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from syllable_sdk import models, utils
from syllable_sdk._hooks import SDKHooks
from syllable_sdk.agents import Agents
from syllable_sdk.channels import Channels
from syllable_sdk.conversations import Conversations
from syllable_sdk.custom_messages import CustomMessages
from syllable_sdk.dashboards import Dashboards
from syllable_sdk.data_sources import DataSources
from syllable_sdk.events import Events
from syllable_sdk.incidents import Incidents
from syllable_sdk.insights_sdk import InsightsSDK
from syllable_sdk.language_groups import LanguageGroups
from syllable_sdk.outbound import Outbound
from syllable_sdk.prompts import Prompts
from syllable_sdk.services import Services
from syllable_sdk.session_debug import SessionDebug
from syllable_sdk.session_labels import SessionLabels
from syllable_sdk.sessions import Sessions
from syllable_sdk.takeouts import Takeouts
from syllable_sdk.tools import Tools
from syllable_sdk.types import OptionalNullable, UNSET
from syllable_sdk.users import Users
from syllable_sdk.v1 import V1
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref


class SyllableSDK(BaseSDK):
    r"""SyllableSDK:
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


    """

    agents: Agents
    r"""Operations related to agent configuration. When a user interacts with the           Syllable system, they do so by communicating with an agent.           An agent is linked to a prompt, a custom message, and one or more channel targets to           define its behavior and capabilities. For more information, see           [Console docs](https://docs.syllable.ai/workspaces/Agents)."""
    channels: Channels
    r"""Operations related to channel configuration.           A channel is an organization-level point of communication, like a phone number or a web           chat. A channel can be associated with an agent by creating a channel target linking           them."""
    conversations: Conversations
    r"""Operations related to conversations.           A conversation is a record of messages between a user and an agent, and is composed of           one or more sessions."""
    data_sources: DataSources
    r"""Operations related to data sources. A data source is a blob of text that           can be made available to an agent's general info tools to provide more context to the           agent when generating its responses. For more information, see           [Console docs](https://docs.syllable.ai/Resources/DataSources)."""
    events: Events
    r"""Operations related to events. An event represents a specific occurrence           during a session. Currently the API/SDK only supports fetching logged events."""
    incidents: Incidents
    r"""Operations related to incidents."""
    insights: InsightsSDK
    r"""Operations related to insights results. An insight is a tool that processes          conversation data to extract information and generate reports."""
    custom_messages: CustomMessages
    r"""Operations related to custom message configuration.           A custom message is a pre-configured message delivered by an agent as a greeting at the           beginning of a conversation. Multiple agents can use the same custom mesasage. A custom           message has one or more rules defined, which allow for different messages to be           dynamically selected and delivered at runtime based on the current time and either           date or day of the week. For more information, see           [Console docs](https://docs.syllable.ai/Resources/Messages)."""
    prompts: Prompts
    r"""Operations related to prompts. A prompt defines the behavior of an           agent by delivering instructions to the LLM about how the agent should behave.           A prompt can be linked to one or more agents. A prompt can also be linked to tools to           allow an agent using the prompt to use them. For more information, see           [Console docs](https://docs.syllable.ai/Resources/Prompts)."""
    services: Services
    r"""Operations related to service configuration. A service is a collection of           tools."""
    session_labels: SessionLabels
    r"""Operations related to labeling sessions with evaluations of quality and           descriptions of issues the user encountered or other details. For more information, see           [Console docs](https://docs.syllable.ai/workspaces/Sessions)."""
    sessions: Sessions
    r"""Operations related to sessions. A session is a building block of a           conversation. For more information, see           [Console docs](https://docs.syllable.ai/workspaces/Sessions)."""
    session_debug: SessionDebug
    tools: Tools
    r"""Operations related to tool configuration. A tool is a function that an           agent can call to perform actions like accessing databases, making API calls, or           processing data. For an agent to have access to a tool, the prompt associated with that           agent should be linked to the tool and include instructions to use it. For more           information, see [Console docs](https://docs.syllable.ai/Resources/Tools)."""
    dashboards: Dashboards
    r"""Operations related to dashboards. Currently the API/SDK           only supports fetching basic information about dashboards."""
    outbound: Outbound
    language_groups: LanguageGroups
    r"""Operations related to language groups. A language group is a           collection of language, voice, and DTMF configuration that can be linked to an agent to           define the languages and voices it supports. For more information, see           [Console docs](https://docs.syllable.ai/Resources/LanguageGroups)."""
    takeouts: Takeouts
    users: Users
    v1: V1

    def __init__(
        self,
        api_key_header: Optional[
            Union[Optional[str], Callable[[], Optional[str]]]
        ] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param api_key_header: The api_key_header required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(api_key_header):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(api_key_header=api_key_header())
        else:
            security = models.Security(api_key_header=api_key_header)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.agents = Agents(self.sdk_configuration)
        self.channels = Channels(self.sdk_configuration)
        self.conversations = Conversations(self.sdk_configuration)
        self.data_sources = DataSources(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
        self.incidents = Incidents(self.sdk_configuration)
        self.insights = InsightsSDK(self.sdk_configuration)
        self.custom_messages = CustomMessages(self.sdk_configuration)
        self.prompts = Prompts(self.sdk_configuration)
        self.services = Services(self.sdk_configuration)
        self.session_labels = SessionLabels(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.session_debug = SessionDebug(self.sdk_configuration)
        self.tools = Tools(self.sdk_configuration)
        self.dashboards = Dashboards(self.sdk_configuration)
        self.outbound = Outbound(self.sdk_configuration)
        self.language_groups = LanguageGroups(self.sdk_configuration)
        self.takeouts = Takeouts(self.sdk_configuration)
        self.users = Users(self.sdk_configuration)
        self.v1 = V1(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
