# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AITrialReportParams"]


class AITrialReportParams(TypedDict, total=False):
    service_type: Required[int]
    """1-猫狗 2-异宠"""

    session_id: Required[str]
    """会话 id"""
