"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class LanguageGroupProperties(str, Enum):
    r"""Names of language group fields supported for filtering/sorting on list endpoint."""

    NAME = "name"
    DESCRIPTION = "description"
    SKIP_CURRENT_LANGUAGE_IN_MESSAGE = "skip_current_language_in_message"
    UPDATED_AT = "updated_at"
    LAST_UPDATED_BY = "last_updated_by"
