"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agentresponse import AgentResponse, AgentResponseTypedDict
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


class ListResponseAgentResponseTypedDict(TypedDict):
    items: List[AgentResponseTypedDict]
    r"""List of items returned from the query"""
    page: int
    r"""The page number of the results (0-based)"""
    page_size: int
    r"""The number of items returned per page"""
    total_pages: NotRequired[Nullable[int]]
    r"""The total number of pages of results given the indicated page size"""
    total_count: NotRequired[Nullable[int]]
    r"""The total number of items returned from the query"""


class ListResponseAgentResponse(BaseModel):
    items: List[AgentResponse]
    r"""List of items returned from the query"""

    page: int
    r"""The page number of the results (0-based)"""

    page_size: int
    r"""The number of items returned per page"""

    total_pages: OptionalNullable[int] = UNSET
    r"""The total number of pages of results given the indicated page size"""

    total_count: OptionalNullable[int] = UNSET
    r"""The total number of items returned from the query"""

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
