"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .insighttoolinput import InsightToolInput, InsightToolInputTypedDict
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class InsightsToolUpdateRequestTypedDict(TypedDict):
    tool_id: int
    insight_tool_input: InsightToolInputTypedDict


class InsightsToolUpdateRequest(BaseModel):
    tool_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    insight_tool_input: Annotated[
        InsightToolInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
