"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .languageconfig import LanguageConfig, LanguageConfigTypedDict
from .languagegroupagentinfo import (
    LanguageGroupAgentInfo,
    LanguageGroupAgentInfoTypedDict,
)
from datetime import datetime
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


class LanguageGroupResponseTypedDict(TypedDict):
    r"""A language group is a collection of language, voice, and DTMF configuration that can be
    linked to an agent to define the languages and voices it supports. For more information, see
    [Console docs](https://docs.syllable.ai/Resources/LanguageGroups).
    """

    name: str
    r"""The name of the language group."""
    language_configs: List[LanguageConfigTypedDict]
    r"""Voice and DTMF configurations for each language in the group."""
    skip_current_language_in_message: bool
    r"""Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu."""
    id: int
    r"""The ID of the language group to update."""
    updated_at: datetime
    r"""Timestamp of the last update to the language group."""
    last_updated_by: str
    r"""Email of the user who last updated the language group."""
    description: NotRequired[Nullable[str]]
    r"""Description of the language group."""
    edit_comments: NotRequired[Nullable[str]]
    r"""Comments for the most recent edit to the language group."""
    agents_info: NotRequired[Nullable[List[LanguageGroupAgentInfoTypedDict]]]
    r"""IDs and names of the agents linked to the language group"""


class LanguageGroupResponse(BaseModel):
    r"""A language group is a collection of language, voice, and DTMF configuration that can be
    linked to an agent to define the languages and voices it supports. For more information, see
    [Console docs](https://docs.syllable.ai/Resources/LanguageGroups).
    """

    name: str
    r"""The name of the language group."""

    language_configs: List[LanguageConfig]
    r"""Voice and DTMF configurations for each language in the group."""

    skip_current_language_in_message: bool
    r"""Whether a message using the language group to generate a language DTMF menu should skip the agent's current language in the menu."""

    id: int
    r"""The ID of the language group to update."""

    updated_at: datetime
    r"""Timestamp of the last update to the language group."""

    last_updated_by: str
    r"""Email of the user who last updated the language group."""

    description: OptionalNullable[str] = UNSET
    r"""Description of the language group."""

    edit_comments: OptionalNullable[str] = UNSET
    r"""Comments for the most recent edit to the language group."""

    agents_info: OptionalNullable[List[LanguageGroupAgentInfo]] = UNSET
    r"""IDs and names of the agents linked to the language group"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "edit_comments", "agents_info"]
        nullable_fields = ["description", "edit_comments", "agents_info"]
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
