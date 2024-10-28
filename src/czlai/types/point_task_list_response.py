# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PointTaskListResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """id"""

    achieve_count: Optional[int] = None
    """可完成次数"""

    bonus_point: Optional[str] = None
    """积分奖励"""

    condition_count: Optional[int] = None
    """完成条件次数"""

    description: Optional[str] = None
    """任务说明"""

    icon: Optional[str] = None
    """任务图标"""

    is_open: Optional[int] = None
    """0-未开启 1-开启"""

    related_module: Optional[str] = None
    """关联模块"""

    status: Optional[int] = None
    """1-未完成 2-未领取"""

    task_action: Optional[str] = None
    """任务动作"""

    task_name: Optional[str] = None
    """任务名称"""

    to_page: Optional[str] = None
    """跳转页面"""


class PointTaskListResponse(BaseModel):
    data: Optional[List[Data]] = None

    message: Optional[str] = None
    """message"""

    success: Optional[bool] = None
    """success"""
