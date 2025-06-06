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


class IncidentCreateRequestTypedDict(TypedDict):
    r"""Request model to create a service incident."""

    description: str
    r"""Description of the service incident"""
    start_datetime: datetime
    r"""Start time of the incident"""
    resolution_datetime: datetime
    r"""Resolution time of the incident"""
    impact_category: str
    r"""Category of the impact"""
    sessions_impacted: int
    r"""Number of sessions impacted"""
    markdown: str
    r"""Detailed markdown description of the incident"""
    organization_id: NotRequired[Nullable[int]]
    r"""The ID of the organization"""
    sub_organization_id: NotRequired[Nullable[int]]
    r"""The ID of the sub-organization"""
    sub_organization: NotRequired[Nullable[str]]
    r"""The name of the sub-organization"""


class IncidentCreateRequest(BaseModel):
    r"""Request model to create a service incident."""

    description: str
    r"""Description of the service incident"""

    start_datetime: datetime
    r"""Start time of the incident"""

    resolution_datetime: datetime
    r"""Resolution time of the incident"""

    impact_category: str
    r"""Category of the impact"""

    sessions_impacted: int
    r"""Number of sessions impacted"""

    markdown: str
    r"""Detailed markdown description of the incident"""

    organization_id: OptionalNullable[int] = UNSET
    r"""The ID of the organization"""

    sub_organization_id: OptionalNullable[int] = UNSET
    r"""The ID of the sub-organization"""

    sub_organization: OptionalNullable[str] = UNSET
    r"""The name of the sub-organization"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "sub_organization_id", "sub_organization"]
        nullable_fields = ["organization_id", "sub_organization_id", "sub_organization"]
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
