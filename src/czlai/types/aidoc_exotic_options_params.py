# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AidocExoticOptionsParams"]


class AidocExoticOptionsParams(TypedDict, total=False):
    pet_profile_id: int
    """宠物档案 id"""

    question: str
    """问题"""

    session_id: str
    """会话 id"""
