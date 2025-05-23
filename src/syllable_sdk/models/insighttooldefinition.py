"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing import Any
from typing_extensions import TypedDict


class InsightToolDefinitionTypedDict(TypedDict):
    r"""Model for an insight tool definition. This is a template that can be used by multiple insight
    tool configurations, each providing their own parameter values.
    """

    id: int
    r"""Unique ID for insight tool definition"""
    name: str
    r"""Human-readable name of insight tool definition"""
    type: str
    r"""Type of insight tool definition"""
    description: str
    r"""Text description of insight tool definition"""
    tool_parameters: Any
    r"""Parameters for tools that use this definition and their associated types"""
    tool_result_set: Any
    r"""Result key/types for insight tool definition"""


class InsightToolDefinition(BaseModel):
    r"""Model for an insight tool definition. This is a template that can be used by multiple insight
    tool configurations, each providing their own parameter values.
    """

    id: int
    r"""Unique ID for insight tool definition"""

    name: str
    r"""Human-readable name of insight tool definition"""

    type: str
    r"""Type of insight tool definition"""

    description: str
    r"""Text description of insight tool definition"""

    tool_parameters: Any
    r"""Parameters for tools that use this definition and their associated types"""

    tool_result_set: Any
    r"""Result key/types for insight tool definition"""
