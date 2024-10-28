# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AIMemeCreateParams"]


class AIMemeCreateParams(TypedDict, total=False):
    image_url: str
    """图片地址"""

    session_id: str
    """会话 id"""
