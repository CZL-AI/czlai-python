# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AICheckupQuestionResultParams"]


class AICheckupQuestionResultParams(TypedDict, total=False):
    index: Required[int]
    """宠物档案 id"""

    pet_profile_id: Required[int]
    """宠物档案 id"""

    question_id: Required[str]
    """回答 id"""

    round: Required[str]
    """题目轮次"""

    session_id: Required[str]
    """会话 id"""
