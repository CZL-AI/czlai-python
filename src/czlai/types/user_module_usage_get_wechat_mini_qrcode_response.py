# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserModuleUsageGetWechatMiniQrcodeResponse", "Data"]


class Data(BaseModel):
    code_url: Optional[str] = None


class UserModuleUsageGetWechatMiniQrcodeResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
