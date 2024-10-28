# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoginSMSParams"]


class LoginSMSParams(TypedDict, total=False):
    code: Required[str]

    phone: Required[str]

    login_from: int
    """1-微信小程序 2-安卓 APP 3-IOS APP"""
