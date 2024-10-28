# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AIConvValidateParams"]


class AIConvValidateParams(TypedDict, total=False):
    session_id: str
    """会话 id"""

    user_input: str
    """用户输入"""
