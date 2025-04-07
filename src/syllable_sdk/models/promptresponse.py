"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .promptllmconfig import PromptLlmConfig, PromptLlmConfigTypedDict
from .toolresponse import ToolResponse, ToolResponseTypedDict
import pydantic
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PromptResponseTypedDict(TypedDict):
    r"""Response model for prompt operations.
    A prompt defines the behavior of an agent by delivering instructions to the LLM about how the
    agent should behave. A prompt can be linked to one or more agents. A prompt can also be linked to
    tools to allow an agent using it to use those tools. For more information, see
    [Console docs](https://docs.syllable.ai/Resources/Prompts).
    """

    name: str
    r"""The prompt name"""
    type: str
    r"""The type of the prompt"""
    llm_config: PromptLlmConfigTypedDict
    r"""LLM configuration for a prompt."""
    id: int
    r"""The internal ID of the prompt"""
    last_updated: Nullable[str]
    r"""The last updated date of the prompt"""
    description: NotRequired[Nullable[str]]
    r"""The description of the prompt"""
    context: NotRequired[Nullable[str]]
    r"""The prompt text that will be sent to the LLM at the beginning of the conversation"""
    tools: NotRequired[List[str]]
    r"""Names of the tools to which the prompt has access (DEPRECATED - use information from full tools field instead)"""
    edit_comments: NotRequired[Nullable[str]]
    r"""The comments for the most recent edit to the prompt"""
    last_updated_by: NotRequired[Nullable[str]]
    r"""Email address of the user who most recently updated the prompt"""
    agent_count: NotRequired[Nullable[int]]
    r"""The number of agents using the prompt"""
    tools_full: NotRequired[Nullable[List[ToolResponseTypedDict]]]
    r"""Full definitions of tools to which the prompt has access"""


class PromptResponse(BaseModel):
    r"""Response model for prompt operations.
    A prompt defines the behavior of an agent by delivering instructions to the LLM about how the
    agent should behave. A prompt can be linked to one or more agents. A prompt can also be linked to
    tools to allow an agent using it to use those tools. For more information, see
    [Console docs](https://docs.syllable.ai/Resources/Prompts).
    """

    name: str
    r"""The prompt name"""

    type: str
    r"""The type of the prompt"""

    llm_config: PromptLlmConfig
    r"""LLM configuration for a prompt."""

    id: int
    r"""The internal ID of the prompt"""

    last_updated: Nullable[str]
    r"""The last updated date of the prompt"""

    description: OptionalNullable[str] = UNSET
    r"""The description of the prompt"""

    context: OptionalNullable[str] = UNSET
    r"""The prompt text that will be sent to the LLM at the beginning of the conversation"""

    tools: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Names of the tools to which the prompt has access (DEPRECATED - use information from full tools field instead)"""

    edit_comments: OptionalNullable[str] = UNSET
    r"""The comments for the most recent edit to the prompt"""

    last_updated_by: OptionalNullable[str] = UNSET
    r"""Email address of the user who most recently updated the prompt"""

    agent_count: OptionalNullable[int] = UNSET
    r"""The number of agents using the prompt"""

    tools_full: OptionalNullable[List[ToolResponse]] = UNSET
    r"""Full definitions of tools to which the prompt has access"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "context",
            "tools",
            "edit_comments",
            "last_updated_by",
            "agent_count",
            "tools_full",
        ]
        nullable_fields = [
            "description",
            "context",
            "edit_comments",
            "last_updated",
            "last_updated_by",
            "agent_count",
            "tools_full",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
