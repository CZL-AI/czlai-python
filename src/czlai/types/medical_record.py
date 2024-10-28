# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MedicalRecord"]


class MedicalRecord(BaseModel):
    id: Optional[int] = None
    """主键 ID"""

    created_at: Optional[datetime] = None
    """创建时间"""

    module_type: Optional[int] = None
    """模块 1-智能问诊 2-健康检测"""

    report: Optional[str] = None
    """报告"""

    session_id: Optional[str] = None
    """对应的 session_id"""

    summary: Optional[str] = None
    """小结"""

    user_uuid: Optional[str] = None
    """用户 uuid"""
