# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AITrialSessionStartParams"]


class AITrialSessionStartParams(TypedDict, total=False):
    content: str
    """用户主诉"""

    service_type: int
    """1-猫狗 2-异宠"""
