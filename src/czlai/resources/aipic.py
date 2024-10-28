# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    aipic_report_params,
    aipic_options_params,
    aipic_question_params,
    aipic_validate_params,
    aipic_pic_result_params,
    aipic_report_task_params,
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

__all__ = ["AipicResource", "AsyncAipicResource"]


class AipicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AipicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AipicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AipicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AipicResourceWithStreamingResponse(self)

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
            "/aipic/options",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_options_params.AipicOptionsParams,
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
          img_belong: 图片归属(1:宠物体态分析、2:宠物表情分析)

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
            "/aipic/pic-result",
            body=maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_pic_result_params.AipicPicResultParams,
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
            "/aipic/question",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_question_params.AipicQuestionParams,
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
            "/aipic/report",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_report_params.AipicReportParams,
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
            "/aipic/report-task",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                aipic_report_task_params.AipicReportTaskParams,
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
            "/aipic/validate",
            body=maybe_transform(
                {
                    "answer": answer,
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_validate_params.AipicValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAipicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAipicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAipicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAipicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAipicResourceWithStreamingResponse(self)

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
            "/aipic/options",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_options_params.AipicOptionsParams,
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
          img_belong: 图片归属(1:宠物体态分析、2:宠物表情分析)

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
            "/aipic/pic-result",
            body=await async_maybe_transform(
                {
                    "img_belong": img_belong,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_pic_result_params.AipicPicResultParams,
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
            "/aipic/question",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aipic_question_params.AipicQuestionParams,
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
            "/aipic/report",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_report_params.AipicReportParams,
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
            "/aipic/report-task",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                aipic_report_task_params.AipicReportTaskParams,
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
            "/aipic/validate",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aipic_validate_params.AipicValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AipicResourceWithRawResponse:
    def __init__(self, aipic: AipicResource) -> None:
        self._aipic = aipic

        self.options = to_raw_response_wrapper(
            aipic.options,
        )
        self.pic_result = to_raw_response_wrapper(
            aipic.pic_result,
        )
        self.question = to_raw_response_wrapper(
            aipic.question,
        )
        self.report = to_raw_response_wrapper(
            aipic.report,
        )
        self.report_task = to_raw_response_wrapper(
            aipic.report_task,
        )
        self.validate = to_raw_response_wrapper(
            aipic.validate,
        )


class AsyncAipicResourceWithRawResponse:
    def __init__(self, aipic: AsyncAipicResource) -> None:
        self._aipic = aipic

        self.options = async_to_raw_response_wrapper(
            aipic.options,
        )
        self.pic_result = async_to_raw_response_wrapper(
            aipic.pic_result,
        )
        self.question = async_to_raw_response_wrapper(
            aipic.question,
        )
        self.report = async_to_raw_response_wrapper(
            aipic.report,
        )
        self.report_task = async_to_raw_response_wrapper(
            aipic.report_task,
        )
        self.validate = async_to_raw_response_wrapper(
            aipic.validate,
        )


class AipicResourceWithStreamingResponse:
    def __init__(self, aipic: AipicResource) -> None:
        self._aipic = aipic

        self.options = to_streamed_response_wrapper(
            aipic.options,
        )
        self.pic_result = to_streamed_response_wrapper(
            aipic.pic_result,
        )
        self.question = to_streamed_response_wrapper(
            aipic.question,
        )
        self.report = to_streamed_response_wrapper(
            aipic.report,
        )
        self.report_task = to_streamed_response_wrapper(
            aipic.report_task,
        )
        self.validate = to_streamed_response_wrapper(
            aipic.validate,
        )


class AsyncAipicResourceWithStreamingResponse:
    def __init__(self, aipic: AsyncAipicResource) -> None:
        self._aipic = aipic

        self.options = async_to_streamed_response_wrapper(
            aipic.options,
        )
        self.pic_result = async_to_streamed_response_wrapper(
            aipic.pic_result,
        )
        self.question = async_to_streamed_response_wrapper(
            aipic.question,
        )
        self.report = async_to_streamed_response_wrapper(
            aipic.report,
        )
        self.report_task = async_to_streamed_response_wrapper(
            aipic.report_task,
        )
        self.validate = async_to_streamed_response_wrapper(
            aipic.validate,
        )
