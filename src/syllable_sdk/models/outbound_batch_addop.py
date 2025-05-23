"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .communicationrequest import CommunicationRequest, CommunicationRequestTypedDict
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class OutboundBatchAddRequestTypedDict(TypedDict):
    batch_id: str
    communication_request: CommunicationRequestTypedDict


class OutboundBatchAddRequest(BaseModel):
    batch_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    communication_request: Annotated[
        CommunicationRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
