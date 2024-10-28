# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["UserAdviceCreateParams"]


class UserAdviceCreateParams(TypedDict, total=False):
    advice_type: Required[str]
    """反馈类型"""

    description: Required[str]
    """反馈内容"""

    image_list: Required[List[str]]
