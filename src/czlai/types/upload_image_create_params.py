# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["UploadImageCreateParams"]


class UploadImageCreateParams(TypedDict, total=False):
    image: Required[FileTypes]
    """要上传的图片文件"""

    is_to_cloud: int
    """是否上传到图床"""

    upload_type: Literal[1, 2, 3, 4]
    """图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他"""
