# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MedicalRecordOngoingRecordParams"]


class MedicalRecordOngoingRecordParams(TypedDict, total=False):
    module_type: Required[int]
    """模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别"""

    pet_profile_id: Required[int]
    """宠物档案 id"""
