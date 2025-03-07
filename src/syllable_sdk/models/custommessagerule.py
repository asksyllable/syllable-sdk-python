"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dayofweek import DayOfWeek
import pydantic
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomMessageRuleTypedDict(TypedDict):
    description: str
    r"""The description of the rule"""
    invert: bool
    r"""Whether the rule logic should be inverted (i.e. \"not\")"""
    text: str
    r"""Message text associated with the rule"""
    time_range_start: NotRequired[Nullable[str]]
    r"""The start of the time range for the rule in 24-hour format hh:mm (should be null for \"all day\" cases)"""
    time_range_end: NotRequired[Nullable[str]]
    r"""The end of the time range for the rule in 24-hour format hh:mm (should be null for \"all day\" cases)"""
    date_: NotRequired[Nullable[str]]
    r"""The date for the rule in YYYY-MM-DD format"""
    days_of_week: NotRequired[Nullable[List[DayOfWeek]]]
    r"""The days of the week for the rule"""


class CustomMessageRule(BaseModel):
    description: str
    r"""The description of the rule"""

    invert: bool
    r"""Whether the rule logic should be inverted (i.e. \"not\")"""

    text: str
    r"""Message text associated with the rule"""

    time_range_start: OptionalNullable[str] = UNSET
    r"""The start of the time range for the rule in 24-hour format hh:mm (should be null for \"all day\" cases)"""

    time_range_end: OptionalNullable[str] = UNSET
    r"""The end of the time range for the rule in 24-hour format hh:mm (should be null for \"all day\" cases)"""

    date_: Annotated[OptionalNullable[str], pydantic.Field(alias="date")] = UNSET
    r"""The date for the rule in YYYY-MM-DD format"""

    days_of_week: OptionalNullable[List[DayOfWeek]] = UNSET
    r"""The days of the week for the rule"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["time_range_start", "time_range_end", "date", "days_of_week"]
        nullable_fields = ["time_range_start", "time_range_end", "date", "days_of_week"]
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
