"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing_extensions import TypedDict


class ToolPromptInfoTypedDict(TypedDict):
    r"""Information about a prompt linked to a tool."""

    id: int
    r"""The ID of the prompt"""
    name: str
    r"""The name of the prompt"""


class ToolPromptInfo(BaseModel):
    r"""Information about a prompt linked to a tool."""

    id: int
    r"""The ID of the prompt"""

    name: str
    r"""The name of the prompt"""
