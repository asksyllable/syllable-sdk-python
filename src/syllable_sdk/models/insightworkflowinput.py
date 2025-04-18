"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class InsightWorkflowInputConditionsTypedDict(TypedDict):
    r"""Conditions for insight workflow to trigger on a given call recording."""


class InsightWorkflowInputConditions(BaseModel):
    r"""Conditions for insight workflow to trigger on a given call recording."""


class InsightWorkflowInputTypedDict(TypedDict):
    r"""Request model to create/update an insight workflow."""

    name: str
    r"""Human-readable name of insight workflow"""
    description: str
    r"""Text description of insight workflow"""
    insight_tool_ids: List[int]
    r"""List of IDs of insight tools used in the workflow"""
    conditions: InsightWorkflowInputConditionsTypedDict
    r"""Conditions for insight workflow to trigger on a given call recording."""
    status: str
    r"""Status of the insight workflow"""


class InsightWorkflowInput(BaseModel):
    r"""Request model to create/update an insight workflow."""

    name: str
    r"""Human-readable name of insight workflow"""

    description: str
    r"""Text description of insight workflow"""

    insight_tool_ids: List[int]
    r"""List of IDs of insight tools used in the workflow"""

    conditions: InsightWorkflowInputConditions
    r"""Conditions for insight workflow to trigger on a given call recording."""

    status: str
    r"""Status of the insight workflow"""
