# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserPointRetrieveResponse", "Data"]


class Data(BaseModel):
    bonus_point: Optional[str] = None
    """赠送的积分余额"""

    purchase_point: Optional[str] = None
    """购买的积分余额"""

    total_point: Optional[str] = None
    """总积分余额"""


class UserPointRetrieveResponse(BaseModel):
    data: Optional[Data] = None
