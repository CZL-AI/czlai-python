# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    aipic_exotic_report_params,
    aipic_exotic_options_params,
    aipic_exotic_summary_params,
    aipic_exotic_question_params,
    aipic_exotic_validate_params,
    aipic_exotic_pic_result_params,
    aipic_exotic_report_task_params,
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

__all__ = ["AipicExoticsResource", "AsyncAipicExoticsResource"]


class AipicExoticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AipicExoticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AipicExoticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AipicExoticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AipicExoticsResourceWithStreamingResponse(self)

    def options(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题选项

        Args:
          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic-exotic/options",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_exotic_options_params.AipicExoticOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
          img_belong: 图片归属(1:宠物品种分析、2:宠物表情分析)

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
            "/aipic-exotic/pic-result",
            body=maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_exotic_pic_result_params.AipicExoticPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def question(
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
        获取问题(流式)

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
            "/aipic-exotic/question",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_exotic_question_params.AipicExoticQuestionParams,
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
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
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

          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析、3:牙齿分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic-exotic/report",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_exotic_report_params.AipicExoticReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report_task(
        self,
        *,
        session_id: str,
        img_url: str | NotGiven = NOT_GIVEN,
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

          img_url: 图片 url

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic-exotic/report-task",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                aipic_exotic_report_task_params.AipicExoticReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def summary(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取小结(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic-exotic/summary",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_exotic_summary_params.AipicExoticSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def validate(
        self,
        *,
        answer: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        验证答案是否有效

        Args:
          answer: 用户回答

          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic-exotic/validate",
            body=maybe_transform(
                {
                    "answer": answer,
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_exotic_validate_params.AipicExoticValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAipicExoticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAipicExoticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAipicExoticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAipicExoticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAipicExoticsResourceWithStreamingResponse(self)

    async def options(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题选项

        Args:
          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic-exotic/options",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_exotic_options_params.AipicExoticOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
          img_belong: 图片归属(1:宠物品种分析、2:宠物表情分析)

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
            "/aipic-exotic/pic-result",
            body=await async_maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_exotic_pic_result_params.AipicExoticPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def question(
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
        获取问题(流式)

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
            "/aipic-exotic/question",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_exotic_question_params.AipicExoticQuestionParams,
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
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
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

          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析、3:牙齿分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic-exotic/report",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_exotic_report_params.AipicExoticReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report_task(
        self,
        *,
        session_id: str,
        img_url: str | NotGiven = NOT_GIVEN,
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

          img_url: 图片 url

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic-exotic/report-task",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                aipic_exotic_report_task_params.AipicExoticReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def summary(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取小结(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic-exotic/summary",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_exotic_summary_params.AipicExoticSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def validate(
        self,
        *,
        answer: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        验证答案是否有效

        Args:
          answer: 用户回答

          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic-exotic/validate",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_exotic_validate_params.AipicExoticValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AipicExoticsResourceWithRawResponse:
    def __init__(self, aipic_exotics: AipicExoticsResource) -> None:
        self._aipic_exotics = aipic_exotics

        self.options = to_raw_response_wrapper(
            aipic_exotics.options,
        )
        self.pic_result = to_raw_response_wrapper(
            aipic_exotics.pic_result,
        )
        self.question = to_raw_response_wrapper(
            aipic_exotics.question,
        )
        self.report = to_raw_response_wrapper(
            aipic_exotics.report,
        )
        self.report_task = to_raw_response_wrapper(
            aipic_exotics.report_task,
        )
        self.summary = to_raw_response_wrapper(
            aipic_exotics.summary,
        )
        self.validate = to_raw_response_wrapper(
            aipic_exotics.validate,
        )


class AsyncAipicExoticsResourceWithRawResponse:
    def __init__(self, aipic_exotics: AsyncAipicExoticsResource) -> None:
        self._aipic_exotics = aipic_exotics

        self.options = async_to_raw_response_wrapper(
            aipic_exotics.options,
        )
        self.pic_result = async_to_raw_response_wrapper(
            aipic_exotics.pic_result,
        )
        self.question = async_to_raw_response_wrapper(
            aipic_exotics.question,
        )
        self.report = async_to_raw_response_wrapper(
            aipic_exotics.report,
        )
        self.report_task = async_to_raw_response_wrapper(
            aipic_exotics.report_task,
        )
        self.summary = async_to_raw_response_wrapper(
            aipic_exotics.summary,
        )
        self.validate = async_to_raw_response_wrapper(
            aipic_exotics.validate,
        )


class AipicExoticsResourceWithStreamingResponse:
    def __init__(self, aipic_exotics: AipicExoticsResource) -> None:
        self._aipic_exotics = aipic_exotics

        self.options = to_streamed_response_wrapper(
            aipic_exotics.options,
        )
        self.pic_result = to_streamed_response_wrapper(
            aipic_exotics.pic_result,
        )
        self.question = to_streamed_response_wrapper(
            aipic_exotics.question,
        )
        self.report = to_streamed_response_wrapper(
            aipic_exotics.report,
        )
        self.report_task = to_streamed_response_wrapper(
            aipic_exotics.report_task,
        )
        self.summary = to_streamed_response_wrapper(
            aipic_exotics.summary,
        )
        self.validate = to_streamed_response_wrapper(
            aipic_exotics.validate,
        )


class AsyncAipicExoticsResourceWithStreamingResponse:
    def __init__(self, aipic_exotics: AsyncAipicExoticsResource) -> None:
        self._aipic_exotics = aipic_exotics

        self.options = async_to_streamed_response_wrapper(
            aipic_exotics.options,
        )
        self.pic_result = async_to_streamed_response_wrapper(
            aipic_exotics.pic_result,
        )
        self.question = async_to_streamed_response_wrapper(
            aipic_exotics.question,
        )
        self.report = async_to_streamed_response_wrapper(
            aipic_exotics.report,
        )
        self.report_task = async_to_streamed_response_wrapper(
            aipic_exotics.report_task,
        )
        self.summary = async_to_streamed_response_wrapper(
            aipic_exotics.summary,
        )
        self.validate = async_to_streamed_response_wrapper(
            aipic_exotics.validate,
        )
