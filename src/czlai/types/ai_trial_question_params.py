# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AITrialQuestionParams"]


class AITrialQuestionParams(TypedDict, total=False):
    service_type: int
    """1-猫狗 2-异宠"""

    session_id: str
    """会话 id"""
