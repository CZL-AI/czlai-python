# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckPointCreateParams"]


class CheckPointCreateParams(TypedDict, total=False):
    action: str
    """埋点动作"""

    code: str
    """微信 code"""

    page_path: str
    """页面路径"""

    related_id: str
    """关联 id"""
