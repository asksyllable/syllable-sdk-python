"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .batchstatus import BatchStatus
from datetime import datetime
from pydantic import model_serializer
from syllable_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CommunicationBatchTypedDict(TypedDict):
    batch_id: str
    r"""Unique ID for conversation batch"""
    campaign_id: int
    r"""Unique ID for campaign"""
    last_updated_by: str
    r"""Email of user who last updated campaign"""
    expires_on: NotRequired[Nullable[datetime]]
    r"""Timestamp of batch expiration"""
    paused: NotRequired[Nullable[bool]]
    r"""Whether the batch is on HOLD. When on HOLD, no outreach will be made."""
    status: NotRequired[BatchStatus]
    r"""Status of a communication batch."""
    upload_filename: NotRequired[Nullable[str]]
    r"""Name of file used to create batch"""
    created_at: NotRequired[datetime]
    r"""Timestamp of batch creation"""
    deleted_at: NotRequired[Nullable[datetime]]
    r"""Timestamp of batch deletion"""
    deleted_reason: NotRequired[Nullable[str]]
    r"""Reason for batch deletion"""
    last_worked_on: NotRequired[Nullable[datetime]]
    r"""Timestamp of last batch activity"""
    error_message: NotRequired[Nullable[str]]
    r"""Error message if batch upload failed"""


class CommunicationBatch(BaseModel):
    batch_id: str
    r"""Unique ID for conversation batch"""

    campaign_id: int
    r"""Unique ID for campaign"""

    last_updated_by: str
    r"""Email of user who last updated campaign"""

    expires_on: OptionalNullable[datetime] = UNSET
    r"""Timestamp of batch expiration"""

    paused: OptionalNullable[bool] = UNSET
    r"""Whether the batch is on HOLD. When on HOLD, no outreach will be made."""

    status: Optional[BatchStatus] = None
    r"""Status of a communication batch."""

    upload_filename: OptionalNullable[str] = UNSET
    r"""Name of file used to create batch"""

    created_at: Optional[datetime] = None
    r"""Timestamp of batch creation"""

    deleted_at: OptionalNullable[datetime] = UNSET
    r"""Timestamp of batch deletion"""

    deleted_reason: OptionalNullable[str] = UNSET
    r"""Reason for batch deletion"""

    last_worked_on: OptionalNullable[datetime] = UNSET
    r"""Timestamp of last batch activity"""

    error_message: OptionalNullable[str] = UNSET
    r"""Error message if batch upload failed"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "expires_on",
            "paused",
            "status",
            "upload_filename",
            "created_at",
            "deleted_at",
            "deleted_reason",
            "last_worked_on",
            "error_message",
        ]
        nullable_fields = [
            "expires_on",
            "paused",
            "upload_filename",
            "deleted_at",
            "deleted_reason",
            "last_worked_on",
            "error_message",
        ]
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
