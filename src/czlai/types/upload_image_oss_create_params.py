# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["UploadImageOssCreateParams"]


class UploadImageOssCreateParams(TypedDict, total=False):
    upload_type: Required[Literal[1, 2, 3, 4]]
    """图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他"""

    image: Required[FileTypes]
    """要上传的图片文件"""

    upload_to_local: int
    """是否上传到本地服务器"""
