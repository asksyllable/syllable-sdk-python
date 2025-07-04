"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from syllable_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from typing import Any, Optional
from typing_extensions import NotRequired, TypedDict


class TestMessageResponseTypedDict(TypedDict):
    r"""Response from an agent in a test chat."""

    __test__ = False  # pyright: ignore[reportGeneralTypeIssues]

    test_id: str
    r"""Channel-manager-side ID of the session (see Session.channel_manager_sid)"""
    agent_id: str
    r"""ID of the agent with which the chat is taking place"""
    response: Nullable[Any]
    r"""The response from the agent"""
    text: NotRequired[str]
    r"""The text of the message that elicited the response"""
    response_text: NotRequired[str]
    r"""The text of the response"""


class TestMessageResponse(BaseModel):
    r"""Response from an agent in a test chat."""

    __test__ = False

    test_id: str
    r"""Channel-manager-side ID of the session (see Session.channel_manager_sid)"""

    agent_id: str
    r"""ID of the agent with which the chat is taking place"""

    response: Nullable[Any]
    r"""The response from the agent"""

    text: Optional[str] = None
    r"""The text of the message that elicited the response"""

    response_text: Optional[str] = None
    r"""The text of the response"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["text", "response_text"]
        nullable_fields = ["response"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
