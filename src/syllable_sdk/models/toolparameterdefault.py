"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .toolparametertransform import (
    ToolParameterTransform,
    ToolParameterTransformTypedDict,
)
from syllable_sdk.types import BaseModel
from typing_extensions import TypedDict


class ToolParameterDefaultTypedDict(TypedDict):
    r"""The default value for a parameter of a tool call."""

    transform: ToolParameterTransformTypedDict
    r"""A transform to be applied to the value of a tool parameter.

    Either `value` or `format` must be set:
    - `value` is any arbitrary value: string, list or dictionary.
    - `format` is a string composed of other parameters or context variables.
    """


class ToolParameterDefault(BaseModel):
    r"""The default value for a parameter of a tool call."""

    transform: ToolParameterTransform
    r"""A transform to be applied to the value of a tool parameter.

    Either `value` or `format` must be set:
    - `value` is any arbitrary value: string, list or dictionary.
    - `format` is a string composed of other parameters or context variables.
    """
