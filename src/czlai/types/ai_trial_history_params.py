# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AITrialHistoryParams"]


class AITrialHistoryParams(TypedDict, total=False):
    content: Required[str]
    """内容"""

    role: Required[str]
    """角色, 取值为其中之一 ==>[user, ai]"""

    session_id: Required[str]
    """会话 id"""

    content_type: int
    """1-文字 2-图文"""

    module_type: int
    """1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别"""

    stage: int
    """1-用户主诉 2-用户回答 3-AI 提问 4-AI 病情小结 5-AI 病例报告 6-AI 输出 7-用户补充"""
