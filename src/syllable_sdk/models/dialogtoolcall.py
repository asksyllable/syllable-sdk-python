"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from syllable_sdk.types import BaseModel
from typing import Any
from typing_extensions import TypedDict


class DialogToolCallTypedDict(TypedDict):
    tool_call_id: str
    r"""Tool call ID"""
    tool_name: str
    r"""Tool name"""
    tool_arguments: Any
    r"""Tool arguments"""
    timestamp: datetime
    r"""Tool call timestamp"""


class DialogToolCall(BaseModel):
    tool_call_id: str
    r"""Tool call ID"""

    tool_name: str
    r"""Tool name"""

    tool_arguments: Any
    r"""Tool arguments"""

    timestamp: datetime
    r"""Tool call timestamp"""
