# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AICheckupUpdateProfileParams"]


class AICheckupUpdateProfileParams(TypedDict, total=False):
    pet_profile_id: int
    """宠物档案 id"""

    session_id: str
    """会话 id"""

    update_type: int
    """更新类型, 可选 1,2,3"""
