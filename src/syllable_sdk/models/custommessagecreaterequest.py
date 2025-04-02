"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .custommessagerule import CustomMessageRule, CustomMessageRuleTypedDict
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


class CustomMessageCreateRequestTypedDict(TypedDict):
    r"""Request model to create a custom message."""

    name: str
    r"""The name of the custom message"""
    text: str
    r"""The default message that the agent will deliver if no rules are set or no rules match the current timestamp."""
    label: NotRequired[Nullable[str]]
    r"""The label of the custom message"""
    rules: NotRequired[List[CustomMessageRuleTypedDict]]
    r"""Rules for time-specific message variants"""
    type: NotRequired[str]
    r"""Type of the custom message (must be \"greeting\" for now)"""


class CustomMessageCreateRequest(BaseModel):
    r"""Request model to create a custom message."""

    name: str
    r"""The name of the custom message"""

    text: str
    r"""The default message that the agent will deliver if no rules are set or no rules match the current timestamp."""

    label: OptionalNullable[str] = UNSET
    r"""The label of the custom message"""

    rules: Optional[List[CustomMessageRule]] = None
    r"""Rules for time-specific message variants"""

    type: Optional[str] = "greeting"
    r"""Type of the custom message (must be \"greeting\" for now)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["label", "rules", "type"]
        nullable_fields = ["label"]
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
