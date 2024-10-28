# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AidocExoticPicResultParams"]


class AidocExoticPicResultParams(TypedDict, total=False):
    img_url: str
    """图片 url"""

    pet_profile_id: int
    """宠物档案 id"""

    session_id: str
    """会话 id"""
