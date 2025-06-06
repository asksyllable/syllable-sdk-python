"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class ConversationProperties(str, Enum):
    TIMESTAMP = "timestamp"
    AGENT_TYPE = "agent_type"
    AGENT_ID = "agent_id"
    AGENT_NAME = "agent_name"
    PROMPT_ID = "prompt_id"
    PROMPT_NAME = "prompt_name"
    LLM_PROVIDER = "llm_provider"
    LLM_MODEL = "llm_model"
    LLM_VERSION = "llm_version"
    IS_LEGACY = "is_legacy"
