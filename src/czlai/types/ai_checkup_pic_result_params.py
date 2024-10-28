# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AICheckupPicResultParams"]


class AICheckupPicResultParams(TypedDict, total=False):
    img_url: Required[str]
    """图片 url"""

    pet_profile_id: Required[int]
    """宠物档案 id"""

    session_id: Required[str]
    """会话 id"""
