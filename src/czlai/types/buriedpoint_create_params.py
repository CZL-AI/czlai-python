# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BuriedpointCreateParams"]


class BuriedpointCreateParams(TypedDict, total=False):
    point: Required[str]
    """参数"""

    code: str
    """微信 code"""
