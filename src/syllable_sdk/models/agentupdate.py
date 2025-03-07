"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agentsttprovider import AgentSttProvider
from .agenttooldefaults import AgentToolDefaults, AgentToolDefaultsTypedDict
from .agentwaitsound import AgentWaitSound
import pydantic
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AgentUpdateTypedDict(TypedDict):
    name: str
    r"""The agent name"""
    type: str
    r"""The agent type. Can be an arbitrary string"""
    prompt_id: int
    r"""ID of the prompt associated with the agent"""
    custom_message_id: int
    r"""ID of the custom message that should be delivered at the beginning of a conversation with the agent"""
    timezone: str
    r"""The time zone in which the agent operates"""
    variables: Dict[str, str]
    r"""Custom context variables for the conversation session. Keys should be prefixed with \"vars.\"."""
    tool_headers: Nullable[Dict[str, str]]
    r"""Optional headers to include in tool calls for agent."""
    id: int
    r"""The agent ID"""
    description: NotRequired[Nullable[str]]
    r"""The agent description"""
    label: NotRequired[Nullable[str]]
    r"""The agent label"""
    language_group_id: NotRequired[Nullable[int]]
    r"""ID of the language group associated with the agent"""
    prompt_tool_defaults: NotRequired[List[AgentToolDefaultsTypedDict]]
    r"""User-configured parameter values for the agent's tools"""
    languages: NotRequired[List[str]]
    r"""BCP 47 codes of languages the agent supports"""
    agent_initiated: NotRequired[bool]
    r"""Whether the agent initiates conversation with a user after the custom message is delivered"""
    stt_provider: NotRequired[Nullable[AgentSttProvider]]
    r"""Speech-to-text provider for the agent."""
    wait_sound: NotRequired[Nullable[AgentWaitSound]]
    r"""Sound to play while waiting for a response from the LLM."""


class AgentUpdate(BaseModel):
    name: str
    r"""The agent name"""

    type: str
    r"""The agent type. Can be an arbitrary string"""

    prompt_id: int
    r"""ID of the prompt associated with the agent"""

    custom_message_id: int
    r"""ID of the custom message that should be delivered at the beginning of a conversation with the agent"""

    timezone: str
    r"""The time zone in which the agent operates"""

    variables: Dict[str, str]
    r"""Custom context variables for the conversation session. Keys should be prefixed with \"vars.\"."""

    tool_headers: Nullable[Dict[str, str]]
    r"""Optional headers to include in tool calls for agent."""

    id: int
    r"""The agent ID"""

    description: OptionalNullable[str] = UNSET
    r"""The agent description"""

    label: OptionalNullable[str] = UNSET
    r"""The agent label"""

    language_group_id: OptionalNullable[int] = UNSET
    r"""ID of the language group associated with the agent"""

    prompt_tool_defaults: Optional[List[AgentToolDefaults]] = None
    r"""User-configured parameter values for the agent's tools"""

    languages: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""BCP 47 codes of languages the agent supports"""

    agent_initiated: Optional[bool] = False
    r"""Whether the agent initiates conversation with a user after the custom message is delivered"""

    stt_provider: OptionalNullable[AgentSttProvider] = UNSET
    r"""Speech-to-text provider for the agent."""

    wait_sound: OptionalNullable[AgentWaitSound] = UNSET
    r"""Sound to play while waiting for a response from the LLM."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "label",
            "language_group_id",
            "prompt_tool_defaults",
            "languages",
            "agent_initiated",
            "stt_provider",
            "wait_sound",
        ]
        nullable_fields = [
            "tool_headers",
            "description",
            "label",
            "language_group_id",
            "stt_provider",
            "wait_sound",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
