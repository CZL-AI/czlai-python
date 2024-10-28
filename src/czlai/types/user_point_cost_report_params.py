# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserPointCostReportParams"]


class UserPointCostReportParams(TypedDict, total=False):
    item_key: str

    medical_record_id: int
    """病历 id"""
