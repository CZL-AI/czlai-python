# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AIMemeGenerateParams"]


class AIMemeGenerateParams(TypedDict, total=False):
    context_index: int
    """文案序号"""

    meme_id: int
    """表情包 id"""
