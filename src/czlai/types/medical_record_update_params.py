# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MedicalRecordUpdateParams"]


class MedicalRecordUpdateParams(TypedDict, total=False):
    is_read: int

    report_id: int
    """医疗报告 ID"""

    report_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    stage: str
    """阶段存档"""

    status: int
    """1-进行中 2-已完成 3-手动结束 4-自动结束"""
