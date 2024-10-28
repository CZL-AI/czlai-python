# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MedicalRecordRetrieveParams"]


class MedicalRecordRetrieveParams(TypedDict, total=False):
    report_id: Required[int]
    """报告 ID"""
