# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AIMeme", "Context"]


class Context(BaseModel):
    caption_list: Optional[List[str]] = None

    is_cat_or_dog: Optional[int] = None
    """1 表示是猫或狗，2 表示非猫狗的动植物，0 表示不是动植物。"""

    is_legal: Optional[int] = None
    """1 表示是合法的，0 表示不合法。"""


class AIMeme(BaseModel):
    id: Optional[int] = None

    context: Optional[Context] = None

    created_at: Optional[str] = None

    meme_image: Optional[object] = None
    """表情包 url 列表"""

    origin_image: Optional[str] = None
    """原始图片列表"""

    updated_at: Optional[str] = None
