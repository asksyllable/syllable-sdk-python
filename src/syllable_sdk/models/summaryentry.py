"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .latencycategory import LatencyCategory
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing_extensions import NotRequired, TypedDict


class SummaryEntryTypedDict(TypedDict):
    r"""A summary entry is an aggregation of latency entries by category and sub-category.
    It contains the total and average latency for each category.
    """

    category: LatencyCategory
    event_count: int
    sum_ms: float
    sum_str: str
    average_ms: float
    average_str: str
    sub_category: NotRequired[Nullable[str]]


class SummaryEntry(BaseModel):
    r"""A summary entry is an aggregation of latency entries by category and sub-category.
    It contains the total and average latency for each category.
    """

    category: LatencyCategory

    event_count: int

    sum_ms: float

    sum_str: str

    average_ms: float

    average_str: str

    sub_category: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["sub_category"]
        nullable_fields = ["sub_category"]
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
