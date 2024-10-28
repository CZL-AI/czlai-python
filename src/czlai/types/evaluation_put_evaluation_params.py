# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvaluationPutEvaluationParams"]


class EvaluationPutEvaluationParams(TypedDict, total=False):
    content: Required[str]
    """文本内容"""

    evaluation: Required[int]
    """评价 id"""

    session_id: Required[str]
    """会话 id"""
