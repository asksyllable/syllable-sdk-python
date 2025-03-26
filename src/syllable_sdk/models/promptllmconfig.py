"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .promptllmprovider import PromptLlmProvider
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PromptLlmConfigTypedDict(TypedDict):
    r"""LLM configuration for a prompt."""

    provider: NotRequired[PromptLlmProvider]
    r"""LLM API provider."""
    model: NotRequired[str]
    r"""Name of the model. Must match the deployment name in Azure AI Studio."""
    version: NotRequired[Nullable[str]]
    r"""Optional model version."""
    api_version: NotRequired[Nullable[str]]
    r"""Version of the API. (Currently only used for Azure OpenAI.)"""


class PromptLlmConfig(BaseModel):
    r"""LLM configuration for a prompt."""

    provider: Optional[PromptLlmProvider] = None
    r"""LLM API provider."""

    model: Optional[str] = "gpt-4o"
    r"""Name of the model. Must match the deployment name in Azure AI Studio."""

    version: OptionalNullable[str] = UNSET
    r"""Optional model version."""

    api_version: OptionalNullable[str] = UNSET
    r"""Version of the API. (Currently only used for Azure OpenAI.)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["provider", "model", "version", "api_version"]
        nullable_fields = ["version", "api_version"]
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
