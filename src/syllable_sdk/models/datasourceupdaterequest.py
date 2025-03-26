"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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


class DataSourceUpdateRequestTypedDict(TypedDict):
    r"""Request model to update an existing data source."""

    name: str
    r"""The data source name. Must be unique within suborg. Cannot contain whitespace."""
    chunk: bool
    r"""Whether the content should be split into smaller chunks. (This feature is coming in the future - currently this value will always be treated as False.)"""
    id: int
    r"""The data source ID."""
    text: str
    r"""Information that the data source will provide to the agent accessing it. It is recommended to include a sentence at the beginning providing context to the LLM for the information in the data source."""
    description: NotRequired[Nullable[str]]
    r"""The description of the data source."""
    labels: NotRequired[List[str]]
    r"""Searchable labels for the data source. Can be included in agent.prompt_tool_defaults for a given tool to give the agent access to data sources with those labels when calling that tool."""
    chunk_delimiter: NotRequired[Nullable[str]]
    r"""String that should be treated as delimiter between intended chunks. (This feature is coming in the future - currently this value will always be treated as None.)"""
    edit_comments: NotRequired[Nullable[str]]
    r"""The comments for the most recent edit to the data source"""


class DataSourceUpdateRequest(BaseModel):
    r"""Request model to update an existing data source."""

    name: str
    r"""The data source name. Must be unique within suborg. Cannot contain whitespace."""

    chunk: bool
    r"""Whether the content should be split into smaller chunks. (This feature is coming in the future - currently this value will always be treated as False.)"""

    id: int
    r"""The data source ID."""

    text: str
    r"""Information that the data source will provide to the agent accessing it. It is recommended to include a sentence at the beginning providing context to the LLM for the information in the data source."""

    description: OptionalNullable[str] = UNSET
    r"""The description of the data source."""

    labels: Optional[List[str]] = None
    r"""Searchable labels for the data source. Can be included in agent.prompt_tool_defaults for a given tool to give the agent access to data sources with those labels when calling that tool."""

    chunk_delimiter: OptionalNullable[str] = UNSET
    r"""String that should be treated as delimiter between intended chunks. (This feature is coming in the future - currently this value will always be treated as None.)"""

    edit_comments: OptionalNullable[str] = UNSET
    r"""The comments for the most recent edit to the data source"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "labels", "chunk_delimiter", "edit_comments"]
        nullable_fields = ["description", "chunk_delimiter", "edit_comments"]
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
