"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channeltargetupdaterequest import (
    ChannelTargetUpdateRequest,
    ChannelTargetUpdateRequestTypedDict,
)
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class ChannelTargetsUpdateRequestTypedDict(TypedDict):
    channel_id: int
    target_id: int
    channel_target_update_request: ChannelTargetUpdateRequestTypedDict


class ChannelTargetsUpdateRequest(BaseModel):
    channel_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    target_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    channel_target_update_request: Annotated[
        ChannelTargetUpdateRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
