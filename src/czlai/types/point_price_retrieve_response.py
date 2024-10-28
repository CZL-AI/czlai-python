# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PointPriceRetrieveResponse", "Data"]


class Data(BaseModel):
    is_module_item: Optional[int] = None
    """是否为模块项目"""

    item_key: Optional[str] = None
    """积分类型"""

    item_name: Optional[str] = None
    """项目名"""

    price: Optional[str] = None
    """项目 key 名"""

    related_module: Optional[str] = None
    """关联模块"""


class PointPriceRetrieveResponse(BaseModel):
    data: Optional[Data] = None
