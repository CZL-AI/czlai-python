# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    ai_trial_answer_params,
    ai_trial_report_params,
    ai_trial_history_params,
    ai_trial_summary_params,
    ai_trial_relation_params,
    ai_trial_session_start_params,
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

__all__ = ["AITrialResource", "AsyncAITrialResource"]


class AITrialResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AITrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AITrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AITrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AITrialResourceWithStreamingResponse(self)

    def answer(
        self,
        *,
        service_type: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        AI 聊天

        Args:
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/ai-trial/answer",
            body=maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_trial_answer_params.AITrialAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def history(
        self,
        *,
        content: str,
        role: str,
        session_id: str,
        content_type: int | NotGiven = NOT_GIVEN,
        module_type: int | NotGiven = NOT_GIVEN,
        stage: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        保存聊天记录

        Args:
          content: 内容

          role: 角色, 取值为其中之一 ==>[user, ai]

          session_id: 会话 id

          content_type: 1-文字 2-图文

          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          stage: 1-用户主诉 2-用户回答 3-AI 提问 4-AI 病情小结 5-AI 病例报告 6-AI 输出 7-用户补充

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/history",
            body=maybe_transform(
                {
                    "content": content,
                    "role": role,
                    "session_id": session_id,
                    "content_type": content_type,
                    "module_type": module_type,
                    "stage": stage,
                },
                ai_trial_history_params.AITrialHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def relation(
        self,
        *,
        service_type: Literal[1, 2] | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问答联想

        Args:
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/relation",
            body=maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_relation_params.AITrialRelationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report(
        self,
        *,
        service_type: int,
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
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/report",
            body=maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_report_params.AITrialReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def session_start(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        service_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        流程开始

        Args:
          content: 用户主诉

          service_type: 1-猫狗 2-异宠

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/session-start",
            body=maybe_transform(
                {
                    "content": content,
                    "service_type": service_type,
                },
                ai_trial_session_start_params.AITrialSessionStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def summary(
        self,
        *,
        service_type: int | NotGiven = NOT_GIVEN,
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
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/summary",
            body=maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_summary_params.AITrialSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAITrialResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAITrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAITrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAITrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAITrialResourceWithStreamingResponse(self)

    async def answer(
        self,
        *,
        service_type: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        AI 聊天

        Args:
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/answer",
            body=await async_maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_trial_answer_params.AITrialAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def history(
        self,
        *,
        content: str,
        role: str,
        session_id: str,
        content_type: int | NotGiven = NOT_GIVEN,
        module_type: int | NotGiven = NOT_GIVEN,
        stage: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        保存聊天记录

        Args:
          content: 内容

          role: 角色, 取值为其中之一 ==>[user, ai]

          session_id: 会话 id

          content_type: 1-文字 2-图文

          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          stage: 1-用户主诉 2-用户回答 3-AI 提问 4-AI 病情小结 5-AI 病例报告 6-AI 输出 7-用户补充

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/history",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "role": role,
                    "session_id": session_id,
                    "content_type": content_type,
                    "module_type": module_type,
                    "stage": stage,
                },
                ai_trial_history_params.AITrialHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def relation(
        self,
        *,
        service_type: Literal[1, 2] | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取问答联想

        Args:
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/relation",
            body=await async_maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_relation_params.AITrialRelationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report(
        self,
        *,
        service_type: int,
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
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/report",
            body=await async_maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_report_params.AITrialReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def session_start(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        service_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        流程开始

        Args:
          content: 用户主诉

          service_type: 1-猫狗 2-异宠

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/session-start",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "service_type": service_type,
                },
                ai_trial_session_start_params.AITrialSessionStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def summary(
        self,
        *,
        service_type: int | NotGiven = NOT_GIVEN,
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
          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/summary",
            body=await async_maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_summary_params.AITrialSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AITrialResourceWithRawResponse:
    def __init__(self, ai_trial: AITrialResource) -> None:
        self._ai_trial = ai_trial

        self.answer = to_raw_response_wrapper(
            ai_trial.answer,
        )
        self.history = to_raw_response_wrapper(
            ai_trial.history,
        )
        self.relation = to_raw_response_wrapper(
            ai_trial.relation,
        )
        self.report = to_raw_response_wrapper(
            ai_trial.report,
        )
        self.session_start = to_raw_response_wrapper(
            ai_trial.session_start,
        )
        self.summary = to_raw_response_wrapper(
            ai_trial.summary,
        )


class AsyncAITrialResourceWithRawResponse:
    def __init__(self, ai_trial: AsyncAITrialResource) -> None:
        self._ai_trial = ai_trial

        self.answer = async_to_raw_response_wrapper(
            ai_trial.answer,
        )
        self.history = async_to_raw_response_wrapper(
            ai_trial.history,
        )
        self.relation = async_to_raw_response_wrapper(
            ai_trial.relation,
        )
        self.report = async_to_raw_response_wrapper(
            ai_trial.report,
        )
        self.session_start = async_to_raw_response_wrapper(
            ai_trial.session_start,
        )
        self.summary = async_to_raw_response_wrapper(
            ai_trial.summary,
        )


class AITrialResourceWithStreamingResponse:
    def __init__(self, ai_trial: AITrialResource) -> None:
        self._ai_trial = ai_trial

        self.answer = to_streamed_response_wrapper(
            ai_trial.answer,
        )
        self.history = to_streamed_response_wrapper(
            ai_trial.history,
        )
        self.relation = to_streamed_response_wrapper(
            ai_trial.relation,
        )
        self.report = to_streamed_response_wrapper(
            ai_trial.report,
        )
        self.session_start = to_streamed_response_wrapper(
            ai_trial.session_start,
        )
        self.summary = to_streamed_response_wrapper(
            ai_trial.summary,
        )


class AsyncAITrialResourceWithStreamingResponse:
    def __init__(self, ai_trial: AsyncAITrialResource) -> None:
        self._ai_trial = ai_trial

        self.answer = async_to_streamed_response_wrapper(
            ai_trial.answer,
        )
        self.history = async_to_streamed_response_wrapper(
            ai_trial.history,
        )
        self.relation = async_to_streamed_response_wrapper(
            ai_trial.relation,
        )
        self.report = async_to_streamed_response_wrapper(
            ai_trial.report,
        )
        self.session_start = async_to_streamed_response_wrapper(
            ai_trial.session_start,
        )
        self.summary = async_to_streamed_response_wrapper(
            ai_trial.summary,
        )
