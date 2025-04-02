"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
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


class JSONValueTypedDict(TypedDict):
    r"""JSON value of insight tool result"""


class JSONValue(BaseModel):
    r"""JSON value of insight tool result"""


class InsightsOutputTypedDict(TypedDict):
    r"""Response model for an insight tool."""

    id: int
    r"""Unique ID for insight tool"""
    session_id: int
    r"""Unique ID for session"""
    insight_tool_id: int
    r"""Unique ID for insight tool"""
    insight_tool_version: int
    r"""Version of insight tool"""
    insight_key: str
    r"""Key for insight tool result"""
    json_value: JSONValueTypedDict
    r"""JSON value of insight tool result"""
    string_value: NotRequired[Nullable[str]]
    r"""String value of insight tool result"""
    numeric_value: NotRequired[Nullable[float]]
    r"""Numeric value of insight tool result"""
    created_at: NotRequired[datetime]
    r"""Timestamp at which insight tool result was created"""
    updated_at: NotRequired[datetime]
    r"""Timestamp at which insight tool result was last updated"""


class InsightsOutput(BaseModel):
    r"""Response model for an insight tool."""

    id: int
    r"""Unique ID for insight tool"""

    session_id: int
    r"""Unique ID for session"""

    insight_tool_id: int
    r"""Unique ID for insight tool"""

    insight_tool_version: int
    r"""Version of insight tool"""

    insight_key: str
    r"""Key for insight tool result"""

    json_value: JSONValue
    r"""JSON value of insight tool result"""

    string_value: OptionalNullable[str] = UNSET
    r"""String value of insight tool result"""

    numeric_value: OptionalNullable[float] = UNSET
    r"""Numeric value of insight tool result"""

    created_at: Optional[datetime] = None
    r"""Timestamp at which insight tool result was created"""

    updated_at: Optional[datetime] = None
    r"""Timestamp at which insight tool result was last updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["string_value", "numeric_value", "created_at", "updated_at"]
        nullable_fields = ["string_value", "numeric_value"]
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
