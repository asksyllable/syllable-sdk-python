"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing_extensions import TypedDict


class InsightToolInputToolArgumentsTypedDict(TypedDict):
    r"""Arguments for calling the insight tool"""


class InsightToolInputToolArguments(BaseModel):
    r"""Arguments for calling the insight tool"""


class InsightToolInputTypedDict(TypedDict):
    r"""Request model to create/update an insight tool."""

    name: str
    r"""Human readable name of insight tool"""
    description: str
    r"""Text description of insight tool"""
    version: int
    r"""Version number of insight tool"""
    tool_arguments: InsightToolInputToolArgumentsTypedDict
    r"""Arguments for calling the insight tool"""
    insight_tool_definition_id: int
    r"""Internal ID for the definition used by the insight tool"""


class InsightToolInput(BaseModel):
    r"""Request model to create/update an insight tool."""

    name: str
    r"""Human readable name of insight tool"""

    description: str
    r"""Text description of insight tool"""

    version: int
    r"""Version number of insight tool"""

    tool_arguments: InsightToolInputToolArguments
    r"""Arguments for calling the insight tool"""

    insight_tool_definition_id: int
    r"""Internal ID for the definition used by the insight tool"""
