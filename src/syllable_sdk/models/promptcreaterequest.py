"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .promptllmconfig import PromptLlmConfig, PromptLlmConfigTypedDict
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PromptCreateRequestTypedDict(TypedDict):
    r"""Request model to create a prompt."""

    name: str
    r"""The prompt name"""
    type: str
    r"""The type of the prompt"""
    llm_config: PromptLlmConfigTypedDict
    r"""LLM configuration for a prompt."""
    description: NotRequired[Nullable[str]]
    r"""The description of the prompt"""
    context: NotRequired[Nullable[str]]
    r"""The prompt text that will be sent to the LLM at the beginning of the conversation"""
    tools: NotRequired[List[str]]
    r"""Names of tools to which the prompt has access"""
    include_default_tools: NotRequired[bool]
    r"""Whether to include the default tools (`summary`, `hangup`) in the list of tools for the prompt. If you disable this during creation, you might want to disable it during updates as well, otherwise the default tools will be added when updating the prompt."""


class PromptCreateRequest(BaseModel):
    r"""Request model to create a prompt."""

    name: str
    r"""The prompt name"""

    type: str
    r"""The type of the prompt"""

    llm_config: PromptLlmConfig
    r"""LLM configuration for a prompt."""

    description: OptionalNullable[str] = UNSET
    r"""The description of the prompt"""

    context: OptionalNullable[str] = UNSET
    r"""The prompt text that will be sent to the LLM at the beginning of the conversation"""

    tools: Optional[List[str]] = None
    r"""Names of tools to which the prompt has access"""

    include_default_tools: Optional[bool] = True
    r"""Whether to include the default tools (`summary`, `hangup`) in the list of tools for the prompt. If you disable this during creation, you might want to disable it during updates as well, otherwise the default tools will be added when updating the prompt."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "context", "tools", "include_default_tools"]
        nullable_fields = ["description", "context"]
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
