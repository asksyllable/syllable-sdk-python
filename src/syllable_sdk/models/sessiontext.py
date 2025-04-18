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
from typing_extensions import NotRequired, TypedDict


class SessionTextTypedDict(TypedDict):
    r"""Information about a given message from a user to an agent or vice-versa."""

    timestamp: datetime
    r"""Timestamp of the message"""
    lang: NotRequired[Nullable[str]]
    r"""ISO 639 code of the language used for the message (may appear as \"unset\" if was not conclusively determined)"""
    source: NotRequired[Nullable[str]]
    r"""Whether the user or agent sent the message"""
    text: NotRequired[Nullable[str]]
    r"""Content of the message"""


class SessionText(BaseModel):
    r"""Information about a given message from a user to an agent or vice-versa."""

    timestamp: datetime
    r"""Timestamp of the message"""

    lang: OptionalNullable[str] = UNSET
    r"""ISO 639 code of the language used for the message (may appear as \"unset\" if was not conclusively determined)"""

    source: OptionalNullable[str] = UNSET
    r"""Whether the user or agent sent the message"""

    text: OptionalNullable[str] = UNSET
    r"""Content of the message"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["lang", "source", "text"]
        nullable_fields = ["lang", "source", "text"]
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
