"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class SessionSummaryGetByIDRequestTypedDict(TypedDict):
    session_id: str


class SessionSummaryGetByIDRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
