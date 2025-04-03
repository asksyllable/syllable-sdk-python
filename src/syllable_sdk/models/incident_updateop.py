"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .serviceincidentrequest import (
    ServiceIncidentRequest,
    ServiceIncidentRequestTypedDict,
)
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class IncidentUpdateRequestTypedDict(TypedDict):
    incident_id: int
    service_incident_request: ServiceIncidentRequestTypedDict


class IncidentUpdateRequest(BaseModel):
    incident_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    service_incident_request: Annotated[
        ServiceIncidentRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
