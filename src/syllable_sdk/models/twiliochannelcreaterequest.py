"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .twiliochannelconfigcreate import (
    TwilioChannelConfigCreate,
    TwilioChannelConfigCreateTypedDict,
)
from syllable_sdk.types import BaseModel
from typing_extensions import TypedDict


class TwilioChannelCreateRequestTypedDict(TypedDict):
    r"""Request model for creating a Twilio channel."""

    name: str
    r"""The channel name"""
    config: TwilioChannelConfigCreateTypedDict
    r"""Twilio channel config information."""


class TwilioChannelCreateRequest(BaseModel):
    r"""Request model for creating a Twilio channel."""

    name: str
    r"""The channel name"""

    config: TwilioChannelConfigCreate
    r"""Twilio channel config information."""
