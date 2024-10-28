# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    image: Required[FileTypes]
    """要上传的图片文件"""

    is_to_cloud: int
    """是否上传到图床"""
