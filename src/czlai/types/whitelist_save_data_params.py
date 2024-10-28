# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["WhitelistSaveDataParams"]


class WhitelistSaveDataParams(TypedDict, total=False):
    save_data: List[str]
    """保存数据"""
