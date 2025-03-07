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


class PromptUpdateRequestTypedDict(TypedDict):
    name: str
    r"""The prompt name"""
    type: str
    r"""The type of the prompt"""
    llm_config: PromptLlmConfigTypedDict
    id: int
    r"""The prompt ID"""
    description: NotRequired[Nullable[str]]
    r"""The description of the prompt"""
    context: NotRequired[Nullable[str]]
    r"""The prompt text"""
    tools: NotRequired[List[str]]
    r"""Names of tools to which the prompt has access"""
    edit_comments: NotRequired[Nullable[str]]
    r"""The comments for the most recent edit to the prompt"""
    include_default_tools: NotRequired[bool]
    r"""Whether to include the default tools (`hangup`, `summary`) in the list of tools for the prompt. If you remove one of the default tools from your prompt, you might want to disable this option so that the tool is not added again when updated."""


class PromptUpdateRequest(BaseModel):
    name: str
    r"""The prompt name"""

    type: str
    r"""The type of the prompt"""

    llm_config: PromptLlmConfig

    id: int
    r"""The prompt ID"""

    description: OptionalNullable[str] = UNSET
    r"""The description of the prompt"""

    context: OptionalNullable[str] = UNSET
    r"""The prompt text"""

    tools: Optional[List[str]] = None
    r"""Names of tools to which the prompt has access"""

    edit_comments: OptionalNullable[str] = UNSET
    r"""The comments for the most recent edit to the prompt"""

    include_default_tools: Optional[bool] = True
    r"""Whether to include the default tools (`hangup`, `summary`) in the list of tools for the prompt. If you remove one of the default tools from your prompt, you might want to disable this option so that the tool is not added again when updated."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "context",
            "tools",
            "edit_comments",
            "include_default_tools",
        ]
        nullable_fields = ["description", "context", "edit_comments"]
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
