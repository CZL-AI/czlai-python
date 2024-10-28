# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AIMemeRetrieveParams"]


class AIMemeRetrieveParams(TypedDict, total=False):
    limit: int
    """每页数量"""

    page: int
    """页数"""
