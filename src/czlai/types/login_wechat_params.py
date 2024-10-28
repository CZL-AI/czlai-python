# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LoginWechatParams"]


class LoginWechatParams(TypedDict, total=False):
    wechat_code: Required[str]
    """会话 id"""

    encrypted_data: Annotated[str, PropertyInfo(alias="encryptedData")]
    """加密数据"""

    iv: str
    """加密初始向量"""

    module_type: int
    """模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图片识别"""

    phone_number: str
    """手机号"""

    spread_id: int
    """推广人 sid"""
