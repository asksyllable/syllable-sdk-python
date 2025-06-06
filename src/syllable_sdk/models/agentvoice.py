"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agentlanguage import AgentLanguage, AgentLanguageTypedDict
from .agentvoicedisplayname import AgentVoiceDisplayName
from .agentvoicegender import AgentVoiceGender
from .agentvoicemodel import AgentVoiceModel
from .agentvoicevarname import AgentVoiceVarName
from .ttsprovider import TtsProvider
from syllable_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AgentVoiceTypedDict(TypedDict):
    r"""Voice option for an agent."""

    provider: TtsProvider
    r"""TTS provider for an agent voice."""
    display_name: AgentVoiceDisplayName
    r"""Display names of voices that Syllable supports."""
    var_name: AgentVoiceVarName
    r"""The variable name of an agent voice (used when processing messages)."""
    gender: AgentVoiceGender
    r"""Gender for an agent voice."""
    model: AgentVoiceModel
    r"""Model for an agent voice."""
    supported_languages: List[AgentLanguageTypedDict]
    r"""Languages supported by the voice"""
    deprecated: bool
    r"""Whether the voice is deprecated and should not be used"""


class AgentVoice(BaseModel):
    r"""Voice option for an agent."""

    provider: TtsProvider
    r"""TTS provider for an agent voice."""

    display_name: AgentVoiceDisplayName
    r"""Display names of voices that Syllable supports."""

    var_name: AgentVoiceVarName
    r"""The variable name of an agent voice (used when processing messages)."""

    gender: AgentVoiceGender
    r"""Gender for an agent voice."""

    model: AgentVoiceModel
    r"""Model for an agent voice."""

    supported_languages: List[AgentLanguage]
    r"""Languages supported by the voice"""

    deprecated: bool
    r"""Whether the voice is deprecated and should not be used"""
