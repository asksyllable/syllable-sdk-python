"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing_extensions import TypedDict


class ServiceCreateRequestTypedDict(TypedDict):
    r"""Request model to create a service."""

    name: str
    r"""The name of the service"""
    description: str
    r"""The description of the service"""


class ServiceCreateRequest(BaseModel):
    r"""Request model to create a service."""

    name: str
    r"""The name of the service"""

    description: str
    r"""The description of the service"""
