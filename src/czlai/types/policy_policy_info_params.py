# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PolicyPolicyInfoParams"]


class PolicyPolicyInfoParams(TypedDict, total=False):
    keys: str
    """密钥"""

    policy_type: int
    """1-用户协议 2-免责条款 3-隐私政策"""
