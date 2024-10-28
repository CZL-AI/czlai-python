# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ai_trial_options_params, ai_trial_question_params
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

__all__ = ["AITrialsResource", "AsyncAITrialsResource"]


class AITrialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AITrialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AITrialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AITrialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AITrialsResourceWithStreamingResponse(self)

    def options(
        self,
        *,
        question: str | NotGiven = NOT_GIVEN,
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
        获取问题选项

        Args:
          question: 问题

          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-trial/options",
            body=maybe_transform(
                {
                    "question": question,
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_options_params.AITrialOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def question(
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
        获取问题(流式)

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
            "/ai-trial/question",
            body=maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_question_params.AITrialQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAITrialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAITrialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAITrialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAITrialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAITrialsResourceWithStreamingResponse(self)

    async def options(
        self,
        *,
        question: str | NotGiven = NOT_GIVEN,
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
        获取问题选项

        Args:
          question: 问题

          service_type: 1-猫狗 2-异宠

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-trial/options",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_options_params.AITrialOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def question(
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
        获取问题(流式)

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
            "/ai-trial/question",
            body=await async_maybe_transform(
                {
                    "service_type": service_type,
                    "session_id": session_id,
                },
                ai_trial_question_params.AITrialQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AITrialsResourceWithRawResponse:
    def __init__(self, ai_trials: AITrialsResource) -> None:
        self._ai_trials = ai_trials

        self.options = to_raw_response_wrapper(
            ai_trials.options,
        )
        self.question = to_raw_response_wrapper(
            ai_trials.question,
        )


class AsyncAITrialsResourceWithRawResponse:
    def __init__(self, ai_trials: AsyncAITrialsResource) -> None:
        self._ai_trials = ai_trials

        self.options = async_to_raw_response_wrapper(
            ai_trials.options,
        )
        self.question = async_to_raw_response_wrapper(
            ai_trials.question,
        )


class AITrialsResourceWithStreamingResponse:
    def __init__(self, ai_trials: AITrialsResource) -> None:
        self._ai_trials = ai_trials

        self.options = to_streamed_response_wrapper(
            ai_trials.options,
        )
        self.question = to_streamed_response_wrapper(
            ai_trials.question,
        )


class AsyncAITrialsResourceWithStreamingResponse:
    def __init__(self, ai_trials: AsyncAITrialsResource) -> None:
        self._ai_trials = ai_trials

        self.options = async_to_streamed_response_wrapper(
            ai_trials.options,
        )
        self.question = async_to_streamed_response_wrapper(
            ai_trials.question,
        )
