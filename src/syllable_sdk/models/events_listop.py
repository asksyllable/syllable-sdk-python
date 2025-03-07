"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .eventproperties import EventProperties
from .orderbydirection import OrderByDirection
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from syllable_sdk.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EventsListRequestTypedDict(TypedDict):
    page: NotRequired[Nullable[int]]
    limit: NotRequired[int]
    search_fields: NotRequired[List[EventProperties]]
    search_field_values: NotRequired[List[str]]
    order_by: NotRequired[Nullable[EventProperties]]
    order_by_direction: NotRequired[Nullable[OrderByDirection]]
    fields: NotRequired[Nullable[List[EventProperties]]]
    start_datetime: NotRequired[Nullable[str]]
    end_datetime: NotRequired[Nullable[str]]


class EventsListRequest(BaseModel):
    page: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 25

    search_fields: Annotated[
        Optional[List[EventProperties]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    search_field_values: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    order_by: Annotated[
        OptionalNullable[EventProperties],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    order_by_direction: Annotated[
        OptionalNullable[OrderByDirection],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    fields: Annotated[
        OptionalNullable[List[EventProperties]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    start_datetime: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    end_datetime: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "page",
            "limit",
            "search_fields",
            "search_field_values",
            "order_by",
            "order_by_direction",
            "fields",
            "start_datetime",
            "end_datetime",
        ]
        nullable_fields = [
            "page",
            "order_by",
            "order_by_direction",
            "fields",
            "start_datetime",
            "end_datetime",
        ]
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
