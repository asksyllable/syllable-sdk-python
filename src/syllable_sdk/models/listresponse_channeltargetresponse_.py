"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channeltargetresponse import ChannelTargetResponse, ChannelTargetResponseTypedDict
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


class ListResponseChannelTargetResponseTypedDict(TypedDict):
    items: List[ChannelTargetResponseTypedDict]
    page: int
    page_size: int
    total_pages: NotRequired[Nullable[int]]
    total_count: NotRequired[Nullable[int]]


class ListResponseChannelTargetResponse(BaseModel):
    items: List[ChannelTargetResponse]

    page: int

    page_size: int

    total_pages: OptionalNullable[int] = UNSET

    total_count: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["total_pages", "total_count"]
        nullable_fields = ["total_pages", "total_count"]
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
