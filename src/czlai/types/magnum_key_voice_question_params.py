# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MagnumKeyVoiceQuestionParams"]


class MagnumKeyVoiceQuestionParams(TypedDict, total=False):
    message: Required[str]
    """语音文本"""

    key_usage_id: Optional[str]
    """会话 id"""

    pet_id: int
    """宠物 id"""

    user_uuid: Optional[str]
    """用户 uuid"""
