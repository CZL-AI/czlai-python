# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AITrialOptionsParams"]


class AITrialOptionsParams(TypedDict, total=False):
    question: str
    """问题"""

    service_type: int
    """1-猫狗 2-异宠"""

    session_id: str
    """会话 id"""
