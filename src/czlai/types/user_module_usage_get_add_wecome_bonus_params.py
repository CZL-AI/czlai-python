# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserModuleUsageGetAddWecomeBonusParams"]


class UserModuleUsageGetAddWecomeBonusParams(TypedDict, total=False):
    module_type: int
    """1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别"""
