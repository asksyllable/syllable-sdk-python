"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List
from typing_extensions import Annotated, TypedDict


class OutboundBatchRemoveRequestTypedDict(TypedDict):
    batch_id: str
    request_body: List[str]


class OutboundBatchRemoveRequest(BaseModel):
    batch_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        List[str], FieldMetadata(request=RequestMetadata(media_type="application/json"))
    ]
