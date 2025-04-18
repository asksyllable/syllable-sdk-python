"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class StaticToolParameterType(str, Enum):
    r"""The expected type for a static tool parameter."""

    STRING = "string"
    INT = "int"
    BOOLEAN = "boolean"
    DATA_SOURCE_LIST = "data_source_list"
