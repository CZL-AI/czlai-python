# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AICheckupQuestionParams"]


class AICheckupQuestionParams(TypedDict, total=False):
    pet_profile_id: Required[int]
    """宠物档案 id"""

    session_id: Required[str]
    """会话 id"""
