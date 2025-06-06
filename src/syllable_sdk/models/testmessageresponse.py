"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from syllable_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ResponseTypedDict(TypedDict):
    r"""The response from the agent"""


class Response(BaseModel):
    r"""The response from the agent"""


class TestMessageResponseTypedDict(TypedDict):
    r"""Response from an agent in a test chat."""

    __test__ = False  # pyright: ignore[reportGeneralTypeIssues]

    test_id: str
    r"""Channel-manager-side ID of the session (see Session.channel_manager_sid)"""
    agent_id: str
    r"""ID of the agent with which the chat is taking place"""
    text: NotRequired[str]
    r"""The text of the message that elicited the response"""
    response: NotRequired[ResponseTypedDict]
    r"""The response from the agent"""
    response_text: NotRequired[str]
    r"""The text of the response"""


class TestMessageResponse(BaseModel):
    r"""Response from an agent in a test chat."""

    __test__ = False

    test_id: str
    r"""Channel-manager-side ID of the session (see Session.channel_manager_sid)"""

    agent_id: str
    r"""ID of the agent with which the chat is taking place"""

    text: Optional[str] = None
    r"""The text of the message that elicited the response"""

    response: Optional[Response] = None
    r"""The response from the agent"""

    response_text: Optional[str] = None
    r"""The text of the response"""
