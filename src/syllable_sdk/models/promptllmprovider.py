"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PromptLlmProvider(str, Enum):
    r"""LLM API provider."""

    AZURE_OPENAI = "azure_openai"
    OPENAI = "openai"
