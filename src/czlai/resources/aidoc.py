# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    aidoc_report_params,
    aidoc_pic_result_params,
    aidoc_report_task_params,
    aidoc_if_need_image_params,
    aidoc_if_continue_ask_params,
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

__all__ = ["AidocResource", "AsyncAidocResource"]


class AidocResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AidocResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AidocResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AidocResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AidocResourceWithStreamingResponse(self)

    def if_continue_ask(
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
    ) -> str:
        """
        判断是否需要继续提问

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/aidoc/if-continue-ask",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_if_continue_ask_params.AidocIfContinueAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def if_need_image(
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
    ) -> object:
        """
        判断是否需要传图

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/aidoc/if-need-image",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_if_need_image_params.AidocIfNeedImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def pic_result(
        self,
        *,
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
            "/aidoc/pic-result",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_pic_result_params.AidocPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发布获取诊断报告任务

        Args:
          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc/report",
            body=maybe_transform({"session_id": session_id}, aidoc_report_params.AidocReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report_task(
        self,
        *,
        session_id: str,
        report_type: int | NotGiven = NOT_GIVEN,
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
          session_id: 会话 id

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc/report-task",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "report_type": report_type,
                },
                aidoc_report_task_params.AidocReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAidocResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAidocResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAidocResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAidocResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAidocResourceWithStreamingResponse(self)

    async def if_continue_ask(
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
    ) -> str:
        """
        判断是否需要继续提问

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/aidoc/if-continue-ask",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_if_continue_ask_params.AidocIfContinueAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def if_need_image(
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
    ) -> object:
        """
        判断是否需要传图

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/aidoc/if-need-image",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_if_need_image_params.AidocIfNeedImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def pic_result(
        self,
        *,
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
            "/aidoc/pic-result",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_pic_result_params.AidocPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发布获取诊断报告任务

        Args:
          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc/report",
            body=await async_maybe_transform({"session_id": session_id}, aidoc_report_params.AidocReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report_task(
        self,
        *,
        session_id: str,
        report_type: int | NotGiven = NOT_GIVEN,
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
          session_id: 会话 id

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc/report-task",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "report_type": report_type,
                },
                aidoc_report_task_params.AidocReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AidocResourceWithRawResponse:
    def __init__(self, aidoc: AidocResource) -> None:
        self._aidoc = aidoc

        self.if_continue_ask = to_raw_response_wrapper(
            aidoc.if_continue_ask,
        )
        self.if_need_image = to_raw_response_wrapper(
            aidoc.if_need_image,
        )
        self.pic_result = to_raw_response_wrapper(
            aidoc.pic_result,
        )
        self.report = to_raw_response_wrapper(
            aidoc.report,
        )
        self.report_task = to_raw_response_wrapper(
            aidoc.report_task,
        )


class AsyncAidocResourceWithRawResponse:
    def __init__(self, aidoc: AsyncAidocResource) -> None:
        self._aidoc = aidoc

        self.if_continue_ask = async_to_raw_response_wrapper(
            aidoc.if_continue_ask,
        )
        self.if_need_image = async_to_raw_response_wrapper(
            aidoc.if_need_image,
        )
        self.pic_result = async_to_raw_response_wrapper(
            aidoc.pic_result,
        )
        self.report = async_to_raw_response_wrapper(
            aidoc.report,
        )
        self.report_task = async_to_raw_response_wrapper(
            aidoc.report_task,
        )


class AidocResourceWithStreamingResponse:
    def __init__(self, aidoc: AidocResource) -> None:
        self._aidoc = aidoc

        self.if_continue_ask = to_streamed_response_wrapper(
            aidoc.if_continue_ask,
        )
        self.if_need_image = to_streamed_response_wrapper(
            aidoc.if_need_image,
        )
        self.pic_result = to_streamed_response_wrapper(
            aidoc.pic_result,
        )
        self.report = to_streamed_response_wrapper(
            aidoc.report,
        )
        self.report_task = to_streamed_response_wrapper(
            aidoc.report_task,
        )


class AsyncAidocResourceWithStreamingResponse:
    def __init__(self, aidoc: AsyncAidocResource) -> None:
        self._aidoc = aidoc

        self.if_continue_ask = async_to_streamed_response_wrapper(
            aidoc.if_continue_ask,
        )
        self.if_need_image = async_to_streamed_response_wrapper(
            aidoc.if_need_image,
        )
        self.pic_result = async_to_streamed_response_wrapper(
            aidoc.pic_result,
        )
        self.report = async_to_streamed_response_wrapper(
            aidoc.report,
        )
        self.report_task = async_to_streamed_response_wrapper(
            aidoc.report_task,
        )
