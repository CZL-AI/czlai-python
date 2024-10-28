# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    ai_checkup_report_params,
    ai_checkup_summary_params,
    ai_checkup_is_first_params,
    ai_checkup_question_params,
    ai_checkup_pic_result_params,
    ai_checkup_report_task_params,
    ai_checkup_update_profile_params,
    ai_checkup_question_result_params,
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
from ..types.ai_checkup_is_first_response import AICheckupIsFirstResponse
from ..types.ai_checkup_session_start_response import AICheckupSessionStartResponse
from ..types.ai_checkup_update_profile_response import AICheckupUpdateProfileResponse

__all__ = ["AICheckupResource", "AsyncAICheckupResource"]


class AICheckupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AICheckupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AICheckupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICheckupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AICheckupResourceWithStreamingResponse(self)

    def is_first(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupIsFirstResponse:
        """
        检查是否为当月首检

        Args:
          pet_profile_id: 宠物档案 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai-checkup/is-first",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pet_profile_id": pet_profile_id}, ai_checkup_is_first_params.AICheckupIsFirstParams
                ),
            ),
            cast_to=AICheckupIsFirstResponse,
        )

    def pic_result(
        self,
        *,
        img_url: str,
        pet_profile_id: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果

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
            "/ai-checkup/pic-result",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_pic_result_params.AICheckupPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def question(
        self,
        *,
        pet_profile_id: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题

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
            "/ai-checkup/question",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_question_params.AICheckupQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def question_result(
        self,
        *,
        index: int,
        pet_profile_id: int,
        question_id: str,
        round: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题

        Args:
          index: 宠物档案 id

          pet_profile_id: 宠物档案 id

          question_id: 回答 id

          round: 题目轮次

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-checkup/question-result",
            body=maybe_transform(
                {
                    "index": index,
                    "pet_profile_id": pet_profile_id,
                    "question_id": question_id,
                    "round": round,
                    "session_id": session_id,
                },
                ai_checkup_question_result_params.AICheckupQuestionResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report(
        self,
        *,
        pet_profile_id: int,
        session_id: str,
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
            "/ai-checkup/report",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_report_params.AICheckupReportParams,
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
            "/ai-checkup/report-task",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                ai_checkup_report_task_params.AICheckupReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def session_start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupSessionStartResponse:
        """开始一个新的会话"""
        return self._get(
            "/ai-checkup/session-start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICheckupSessionStartResponse,
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
    ) -> str:
        """
        生成总结

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
            "/ai-checkup/summary",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_summary_params.AICheckupSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update_profile(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        update_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupUpdateProfileResponse:
        """
        更新宠物档案的体检参数

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          update_type: 更新类型, 可选 1,2,3

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai-checkup/update-profile",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "update_type": update_type,
                },
                ai_checkup_update_profile_params.AICheckupUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICheckupUpdateProfileResponse,
        )


class AsyncAICheckupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAICheckupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICheckupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICheckupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAICheckupResourceWithStreamingResponse(self)

    async def is_first(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupIsFirstResponse:
        """
        检查是否为当月首检

        Args:
          pet_profile_id: 宠物档案 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai-checkup/is-first",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pet_profile_id": pet_profile_id}, ai_checkup_is_first_params.AICheckupIsFirstParams
                ),
            ),
            cast_to=AICheckupIsFirstResponse,
        )

    async def pic_result(
        self,
        *,
        img_url: str,
        pet_profile_id: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果

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
            "/ai-checkup/pic-result",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_pic_result_params.AICheckupPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def question(
        self,
        *,
        pet_profile_id: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题

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
            "/ai-checkup/question",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_question_params.AICheckupQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def question_result(
        self,
        *,
        index: int,
        pet_profile_id: int,
        question_id: str,
        round: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问题

        Args:
          index: 宠物档案 id

          pet_profile_id: 宠物档案 id

          question_id: 回答 id

          round: 题目轮次

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-checkup/question-result",
            body=await async_maybe_transform(
                {
                    "index": index,
                    "pet_profile_id": pet_profile_id,
                    "question_id": question_id,
                    "round": round,
                    "session_id": session_id,
                },
                ai_checkup_question_result_params.AICheckupQuestionResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report(
        self,
        *,
        pet_profile_id: int,
        session_id: str,
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
            "/ai-checkup/report",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_report_params.AICheckupReportParams,
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
            "/ai-checkup/report-task",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "img_url": img_url,
                    "report_type": report_type,
                },
                ai_checkup_report_task_params.AICheckupReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def session_start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupSessionStartResponse:
        """开始一个新的会话"""
        return await self._get(
            "/ai-checkup/session-start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICheckupSessionStartResponse,
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
    ) -> str:
        """
        生成总结

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
            "/ai-checkup/summary",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                ai_checkup_summary_params.AICheckupSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update_profile(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        update_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICheckupUpdateProfileResponse:
        """
        更新宠物档案的体检参数

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          update_type: 更新类型, 可选 1,2,3

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai-checkup/update-profile",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "update_type": update_type,
                },
                ai_checkup_update_profile_params.AICheckupUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICheckupUpdateProfileResponse,
        )


class AICheckupResourceWithRawResponse:
    def __init__(self, ai_checkup: AICheckupResource) -> None:
        self._ai_checkup = ai_checkup

        self.is_first = to_raw_response_wrapper(
            ai_checkup.is_first,
        )
        self.pic_result = to_raw_response_wrapper(
            ai_checkup.pic_result,
        )
        self.question = to_raw_response_wrapper(
            ai_checkup.question,
        )
        self.question_result = to_raw_response_wrapper(
            ai_checkup.question_result,
        )
        self.report = to_raw_response_wrapper(
            ai_checkup.report,
        )
        self.report_task = to_raw_response_wrapper(
            ai_checkup.report_task,
        )
        self.session_start = to_raw_response_wrapper(
            ai_checkup.session_start,
        )
        self.summary = to_raw_response_wrapper(
            ai_checkup.summary,
        )
        self.update_profile = to_raw_response_wrapper(
            ai_checkup.update_profile,
        )


class AsyncAICheckupResourceWithRawResponse:
    def __init__(self, ai_checkup: AsyncAICheckupResource) -> None:
        self._ai_checkup = ai_checkup

        self.is_first = async_to_raw_response_wrapper(
            ai_checkup.is_first,
        )
        self.pic_result = async_to_raw_response_wrapper(
            ai_checkup.pic_result,
        )
        self.question = async_to_raw_response_wrapper(
            ai_checkup.question,
        )
        self.question_result = async_to_raw_response_wrapper(
            ai_checkup.question_result,
        )
        self.report = async_to_raw_response_wrapper(
            ai_checkup.report,
        )
        self.report_task = async_to_raw_response_wrapper(
            ai_checkup.report_task,
        )
        self.session_start = async_to_raw_response_wrapper(
            ai_checkup.session_start,
        )
        self.summary = async_to_raw_response_wrapper(
            ai_checkup.summary,
        )
        self.update_profile = async_to_raw_response_wrapper(
            ai_checkup.update_profile,
        )


class AICheckupResourceWithStreamingResponse:
    def __init__(self, ai_checkup: AICheckupResource) -> None:
        self._ai_checkup = ai_checkup

        self.is_first = to_streamed_response_wrapper(
            ai_checkup.is_first,
        )
        self.pic_result = to_streamed_response_wrapper(
            ai_checkup.pic_result,
        )
        self.question = to_streamed_response_wrapper(
            ai_checkup.question,
        )
        self.question_result = to_streamed_response_wrapper(
            ai_checkup.question_result,
        )
        self.report = to_streamed_response_wrapper(
            ai_checkup.report,
        )
        self.report_task = to_streamed_response_wrapper(
            ai_checkup.report_task,
        )
        self.session_start = to_streamed_response_wrapper(
            ai_checkup.session_start,
        )
        self.summary = to_streamed_response_wrapper(
            ai_checkup.summary,
        )
        self.update_profile = to_streamed_response_wrapper(
            ai_checkup.update_profile,
        )


class AsyncAICheckupResourceWithStreamingResponse:
    def __init__(self, ai_checkup: AsyncAICheckupResource) -> None:
        self._ai_checkup = ai_checkup

        self.is_first = async_to_streamed_response_wrapper(
            ai_checkup.is_first,
        )
        self.pic_result = async_to_streamed_response_wrapper(
            ai_checkup.pic_result,
        )
        self.question = async_to_streamed_response_wrapper(
            ai_checkup.question,
        )
        self.question_result = async_to_streamed_response_wrapper(
            ai_checkup.question_result,
        )
        self.report = async_to_streamed_response_wrapper(
            ai_checkup.report,
        )
        self.report_task = async_to_streamed_response_wrapper(
            ai_checkup.report_task,
        )
        self.session_start = async_to_streamed_response_wrapper(
            ai_checkup.session_start,
        )
        self.summary = async_to_streamed_response_wrapper(
            ai_checkup.summary,
        )
        self.update_profile = async_to_streamed_response_wrapper(
            ai_checkup.update_profile,
        )
