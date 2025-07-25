"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .toolauthtype import ToolAuthType
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import Any
from typing_extensions import NotRequired, TypedDict


class ServiceUpdateRequestTypedDict(TypedDict):
    r"""Request model to update an existing service."""

    name: str
    r"""The name of the service"""
    description: str
    r"""The description of the service"""
    id: int
    r"""The internal ID of the service"""
    auth_type: NotRequired[Nullable[ToolAuthType]]
    r"""The type of authentication to use for the service's tools"""
    auth_values: NotRequired[Nullable[Any]]
    r"""The values to use for the authentication, as a dict. Should contain \"username\" and \"password\" keys if auth type is basic, \"token\" key if auth type is bearer, or arbitrary header keys if auth type is custom_headers. On an update, leave a value for a given key null and the value in the database will not be updated. (If a key is omitted entirely, any existing value for that key will be removed.)"""
    last_updated_comments: NotRequired[Nullable[str]]
    r"""Free text providing comment about what was updated"""


class ServiceUpdateRequest(BaseModel):
    r"""Request model to update an existing service."""

    name: str
    r"""The name of the service"""

    description: str
    r"""The description of the service"""

    id: int
    r"""The internal ID of the service"""

    auth_type: OptionalNullable[ToolAuthType] = UNSET
    r"""The type of authentication to use for the service's tools"""

    auth_values: OptionalNullable[Any] = UNSET
    r"""The values to use for the authentication, as a dict. Should contain \"username\" and \"password\" keys if auth type is basic, \"token\" key if auth type is bearer, or arbitrary header keys if auth type is custom_headers. On an update, leave a value for a given key null and the value in the database will not be updated. (If a key is omitted entirely, any existing value for that key will be removed.)"""

    last_updated_comments: OptionalNullable[str] = UNSET
    r"""Free text providing comment about what was updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["auth_type", "auth_values", "last_updated_comments"]
        nullable_fields = ["auth_type", "auth_values", "last_updated_comments"]
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
