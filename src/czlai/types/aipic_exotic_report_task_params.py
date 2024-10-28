# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AipicExoticReportTaskParams"]


class AipicExoticReportTaskParams(TypedDict, total=False):
    session_id: Required[str]
    """会话 id"""

    img_url: str
    """图片 url"""

    report_type: int
    """报告类型"""
