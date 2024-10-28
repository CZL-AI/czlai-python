# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    medication_analysis_report_params,
    medication_analysis_summary_params,
    medication_analysis_pic_result_params,
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

__all__ = ["MedicationAnalysisResource", "AsyncMedicationAnalysisResource"]


class MedicationAnalysisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MedicationAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return MedicationAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MedicationAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return MedicationAnalysisResourceWithStreamingResponse(self)

    def pic_result(
        self,
        *,
        img_belong: int | NotGiven = NOT_GIVEN,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果(流式)

        Args:
          img_belong: 图片归属(1:宠物体态分析、2:宠物表情分析、3:牙齿分析)

          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/medication_analysis/pic-result",
            body=maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_pic_result_params.MedicationAnalysisPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取诊断报告

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/medication_analysis/report",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_report_params.MedicationAnalysisReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def summary(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取病情小结(流式)

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/medication_analysis/summary",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_summary_params.MedicationAnalysisSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMedicationAnalysisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMedicationAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMedicationAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMedicationAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncMedicationAnalysisResourceWithStreamingResponse(self)

    async def pic_result(
        self,
        *,
        img_belong: int | NotGiven = NOT_GIVEN,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果(流式)

        Args:
          img_belong: 图片归属(1:宠物体态分析、2:宠物表情分析、3:牙齿分析)

          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/medication_analysis/pic-result",
            body=await async_maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_pic_result_params.MedicationAnalysisPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取诊断报告

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/medication_analysis/report",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_report_params.MedicationAnalysisReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def summary(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取病情小结(流式)

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/medication_analysis/summary",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                medication_analysis_summary_params.MedicationAnalysisSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MedicationAnalysisResourceWithRawResponse:
    def __init__(self, medication_analysis: MedicationAnalysisResource) -> None:
        self._medication_analysis = medication_analysis

        self.pic_result = to_raw_response_wrapper(
            medication_analysis.pic_result,
        )
        self.report = to_raw_response_wrapper(
            medication_analysis.report,
        )
        self.summary = to_raw_response_wrapper(
            medication_analysis.summary,
        )


class AsyncMedicationAnalysisResourceWithRawResponse:
    def __init__(self, medication_analysis: AsyncMedicationAnalysisResource) -> None:
        self._medication_analysis = medication_analysis

        self.pic_result = async_to_raw_response_wrapper(
            medication_analysis.pic_result,
        )
        self.report = async_to_raw_response_wrapper(
            medication_analysis.report,
        )
        self.summary = async_to_raw_response_wrapper(
            medication_analysis.summary,
        )


class MedicationAnalysisResourceWithStreamingResponse:
    def __init__(self, medication_analysis: MedicationAnalysisResource) -> None:
        self._medication_analysis = medication_analysis

        self.pic_result = to_streamed_response_wrapper(
            medication_analysis.pic_result,
        )
        self.report = to_streamed_response_wrapper(
            medication_analysis.report,
        )
        self.summary = to_streamed_response_wrapper(
            medication_analysis.summary,
        )


class AsyncMedicationAnalysisResourceWithStreamingResponse:
    def __init__(self, medication_analysis: AsyncMedicationAnalysisResource) -> None:
        self._medication_analysis = medication_analysis

        self.pic_result = async_to_streamed_response_wrapper(
            medication_analysis.pic_result,
        )
        self.report = async_to_streamed_response_wrapper(
            medication_analysis.report,
        )
        self.summary = async_to_streamed_response_wrapper(
            medication_analysis.summary,
        )
