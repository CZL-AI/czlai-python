# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AipicSummaryParams"]


class AipicSummaryParams(TypedDict, total=False):
    img_url: str
    """图片 url"""

    pet_profile_id: int
    """宠物档案 id"""

    session_id: str
    """会话 id"""

    sub_module_type: int
    """图片归属(1:宠物体态分析、2:宠物表情分析)"""
