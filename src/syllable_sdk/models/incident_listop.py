"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .incidentproperties import IncidentProperties
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


class IncidentListRequestTypedDict(TypedDict):
    page: NotRequired[Nullable[int]]
    r"""The page number from which to start (0-based)"""
    limit: NotRequired[int]
    r"""The maximum number of items to return"""
    search_fields: NotRequired[List[IncidentProperties]]
    r"""String names of fields to search. Correspond by index to search field values"""
    search_field_values: NotRequired[List[str]]
    r"""Values of fields to search. Correspond by index to search fields. Unless field name contains \"list\", an individual search field value cannot be a list"""
    order_by: NotRequired[Nullable[IncidentProperties]]
    r"""The field whose value should be used to order the results"""
    order_by_direction: NotRequired[Nullable[OrderByDirection]]
    r"""The direction in which to order the results"""
    fields: NotRequired[Nullable[List[IncidentProperties]]]
    r"""The fields to include in the response"""
    start_datetime: NotRequired[Nullable[str]]
    r"""The start datetime for filtering results"""
    end_datetime: NotRequired[Nullable[str]]
    r"""The end datetime for filtering results"""


class IncidentListRequest(BaseModel):
    page: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The page number from which to start (0-based)"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 25
    r"""The maximum number of items to return"""

    search_fields: Annotated[
        Optional[List[IncidentProperties]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""String names of fields to search. Correspond by index to search field values"""

    search_field_values: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Values of fields to search. Correspond by index to search fields. Unless field name contains \"list\", an individual search field value cannot be a list"""

    order_by: Annotated[
        OptionalNullable[IncidentProperties],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The field whose value should be used to order the results"""

    order_by_direction: Annotated[
        OptionalNullable[OrderByDirection],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The direction in which to order the results"""

    fields: Annotated[
        OptionalNullable[List[IncidentProperties]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The fields to include in the response"""

    start_datetime: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The start datetime for filtering results"""

    end_datetime: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The end datetime for filtering results"""

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
