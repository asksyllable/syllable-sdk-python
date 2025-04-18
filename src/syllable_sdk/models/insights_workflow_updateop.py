"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .insightworkflowinput import InsightWorkflowInput, InsightWorkflowInputTypedDict
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class InsightsWorkflowUpdateRequestTypedDict(TypedDict):
    workflow_id: int
    insight_workflow_input: InsightWorkflowInputTypedDict


class InsightsWorkflowUpdateRequest(BaseModel):
    workflow_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    insight_workflow_input: Annotated[
        InsightWorkflowInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
