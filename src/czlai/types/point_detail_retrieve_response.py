# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PointDetailRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """id"""

    description: Optional[str] = None
    """明细说明"""

    detail_type: Optional[int] = None
    """明细类型 1-购买增加积分 2-活动增加积分 3-模块核销积分"""

    is_add: Optional[Literal[0, 1]] = None
    """0-减少 1-增加"""

    is_purchase_point: Optional[int] = None
    """0-非购买积分 1-购买积分"""

    point_num: Optional[str] = None
    """积分数量"""

    session_id: Optional[str] = None
    """会话 id"""

    user_uuid: Optional[str] = None
    """用户 uuid"""


class PointDetailRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
