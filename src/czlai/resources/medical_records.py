# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import (
    medical_record_update_params,
    medical_record_retrieve_params,
    medical_record_create_list_params,
    medical_record_ongoing_record_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.medical_record_retrieve_response import MedicalRecordRetrieveResponse
from ..types.medical_record_create_list_response import MedicalRecordCreateListResponse

__all__ = ["MedicalRecordsResource", "AsyncMedicalRecordsResource"]


class MedicalRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MedicalRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return MedicalRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MedicalRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return MedicalRecordsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        report_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MedicalRecordRetrieveResponse:
        """
        获取单个病例报告

        Args:
          report_id: 报告 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/medical-record",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"report_id": report_id}, medical_record_retrieve_params.MedicalRecordRetrieveParams
                ),
            ),
            cast_to=MedicalRecordRetrieveResponse,
        )

    def update(
        self,
        *,
        is_read: int | NotGiven = NOT_GIVEN,
        report_id: int | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage: str | NotGiven = NOT_GIVEN,
        status: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        修改状态和记录对话进行阶段

        Args:
          report_id: 医疗报告 ID

          stage: 阶段存档

          status: 1-进行中 2-已完成 3-手动结束 4-自动结束

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/medical-record",
            body=maybe_transform(
                {
                    "is_read": is_read,
                    "report_id": report_id,
                    "report_time": report_time,
                    "stage": stage,
                    "status": status,
                },
                medical_record_update_params.MedicalRecordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        module_type: Iterable[int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pet_profile_id: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MedicalRecordCreateListResponse:
        """
        获取医疗报告列表

        Args:
          limit: 每页数量

          page: 页码

          pet_profile_id: 宠物档案 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/medical-record-list",
            body=maybe_transform(
                {
                    "limit": limit,
                    "module_type": module_type,
                    "page": page,
                    "pet_profile_id": pet_profile_id,
                },
                medical_record_create_list_params.MedicalRecordCreateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MedicalRecordCreateListResponse,
        )

    def ongoing_record(
        self,
        *,
        module_type: int,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取进行中的医疗报告

        Args:
          module_type: 模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          pet_profile_id: 宠物档案 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/medical-record/ongoing-record",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "module_type": module_type,
                        "pet_profile_id": pet_profile_id,
                    },
                    medical_record_ongoing_record_params.MedicalRecordOngoingRecordParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncMedicalRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMedicalRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMedicalRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMedicalRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncMedicalRecordsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        report_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MedicalRecordRetrieveResponse:
        """
        获取单个病例报告

        Args:
          report_id: 报告 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/medical-record",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"report_id": report_id}, medical_record_retrieve_params.MedicalRecordRetrieveParams
                ),
            ),
            cast_to=MedicalRecordRetrieveResponse,
        )

    async def update(
        self,
        *,
        is_read: int | NotGiven = NOT_GIVEN,
        report_id: int | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage: str | NotGiven = NOT_GIVEN,
        status: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        修改状态和记录对话进行阶段

        Args:
          report_id: 医疗报告 ID

          stage: 阶段存档

          status: 1-进行中 2-已完成 3-手动结束 4-自动结束

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/medical-record",
            body=await async_maybe_transform(
                {
                    "is_read": is_read,
                    "report_id": report_id,
                    "report_time": report_time,
                    "stage": stage,
                    "status": status,
                },
                medical_record_update_params.MedicalRecordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        module_type: Iterable[int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pet_profile_id: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MedicalRecordCreateListResponse:
        """
        获取医疗报告列表

        Args:
          limit: 每页数量

          page: 页码

          pet_profile_id: 宠物档案 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/medical-record-list",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "module_type": module_type,
                    "page": page,
                    "pet_profile_id": pet_profile_id,
                },
                medical_record_create_list_params.MedicalRecordCreateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MedicalRecordCreateListResponse,
        )

    async def ongoing_record(
        self,
        *,
        module_type: int,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取进行中的医疗报告

        Args:
          module_type: 模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          pet_profile_id: 宠物档案 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/medical-record/ongoing-record",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "module_type": module_type,
                        "pet_profile_id": pet_profile_id,
                    },
                    medical_record_ongoing_record_params.MedicalRecordOngoingRecordParams,
                ),
            ),
            cast_to=NoneType,
        )


class MedicalRecordsResourceWithRawResponse:
    def __init__(self, medical_records: MedicalRecordsResource) -> None:
        self._medical_records = medical_records

        self.retrieve = to_raw_response_wrapper(
            medical_records.retrieve,
        )
        self.update = to_raw_response_wrapper(
            medical_records.update,
        )
        self.create_list = to_raw_response_wrapper(
            medical_records.create_list,
        )
        self.ongoing_record = to_raw_response_wrapper(
            medical_records.ongoing_record,
        )


class AsyncMedicalRecordsResourceWithRawResponse:
    def __init__(self, medical_records: AsyncMedicalRecordsResource) -> None:
        self._medical_records = medical_records

        self.retrieve = async_to_raw_response_wrapper(
            medical_records.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            medical_records.update,
        )
        self.create_list = async_to_raw_response_wrapper(
            medical_records.create_list,
        )
        self.ongoing_record = async_to_raw_response_wrapper(
            medical_records.ongoing_record,
        )


class MedicalRecordsResourceWithStreamingResponse:
    def __init__(self, medical_records: MedicalRecordsResource) -> None:
        self._medical_records = medical_records

        self.retrieve = to_streamed_response_wrapper(
            medical_records.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            medical_records.update,
        )
        self.create_list = to_streamed_response_wrapper(
            medical_records.create_list,
        )
        self.ongoing_record = to_streamed_response_wrapper(
            medical_records.ongoing_record,
        )


class AsyncMedicalRecordsResourceWithStreamingResponse:
    def __init__(self, medical_records: AsyncMedicalRecordsResource) -> None:
        self._medical_records = medical_records

        self.retrieve = async_to_streamed_response_wrapper(
            medical_records.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            medical_records.update,
        )
        self.create_list = async_to_streamed_response_wrapper(
            medical_records.create_list,
        )
        self.ongoing_record = async_to_streamed_response_wrapper(
            medical_records.ongoing_record,
        )
