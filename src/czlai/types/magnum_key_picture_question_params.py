# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MagnumKeyPictureQuestionParams"]


class MagnumKeyPictureQuestionParams(TypedDict, total=False):
    img_url: Required[str]
    """图片 url"""

    key_usage_id: Optional[str]
    """会话 id"""

    user_uuid: Optional[str]
    """用户 uuid"""
