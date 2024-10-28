# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PointDetailRetrieveParams"]


class PointDetailRetrieveParams(TypedDict, total=False):
    is_add: Literal[0, 1, 2]
    """0-支出 1-收入 2-全部"""

    limit: int
    """每页数量"""

    page: int
    """页数"""
