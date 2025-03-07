"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .languageconfig import LanguageConfig, LanguageConfigTypedDict
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import List
from typing_extensions import NotRequired, TypedDict


class LanguageGroupUpdateRequestTypedDict(TypedDict):
    name: str
    r"""The name of the language group."""
    language_configs: List[LanguageConfigTypedDict]
    r"""Voice and DTMF configurations for each language in the group."""
    skip_current_language_in_message: bool
    r"""Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu."""
    id: int
    r"""The ID of the language group to update."""
    description: NotRequired[Nullable[str]]
    r"""Description of the language group."""
    edit_comments: NotRequired[Nullable[str]]
    r"""Comments for the most recent edit to the language group."""


class LanguageGroupUpdateRequest(BaseModel):
    name: str
    r"""The name of the language group."""

    language_configs: List[LanguageConfig]
    r"""Voice and DTMF configurations for each language in the group."""

    skip_current_language_in_message: bool
    r"""Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu."""

    id: int
    r"""The ID of the language group to update."""

    description: OptionalNullable[str] = UNSET
    r"""Description of the language group."""

    edit_comments: OptionalNullable[str] = UNSET
    r"""Comments for the most recent edit to the language group."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "edit_comments"]
        nullable_fields = ["description", "edit_comments"]
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
