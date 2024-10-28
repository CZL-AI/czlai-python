# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ai_conv_answer_params, ai_conv_relation_params, ai_conv_validate_params
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

__all__ = ["AIConvResource", "AsyncAIConvResource"]


class AIConvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIConvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AIConvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIConvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AIConvResourceWithStreamingResponse(self)

    def answer(
        self,
        *,
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
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/ai-conv/answer",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_answer_params.AIConvAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def relation(
        self,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取联想

        Args:
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-conv/relation",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_relation_params.AIConvRelationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def validate(
        self,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        AI 聊天校验

        Args:
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai-conv/validate",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_validate_params.AIConvValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAIConvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIConvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIConvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIConvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAIConvResourceWithStreamingResponse(self)

    async def answer(
        self,
        *,
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
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/ai-conv/answer",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_answer_params.AIConvAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def relation(
        self,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取联想

        Args:
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-conv/relation",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_relation_params.AIConvRelationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def validate(
        self,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        AI 聊天校验

        Args:
          session_id: 会话 id

          user_input: 用户输入

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai-conv/validate",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "user_input": user_input,
                },
                ai_conv_validate_params.AIConvValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AIConvResourceWithRawResponse:
    def __init__(self, ai_conv: AIConvResource) -> None:
        self._ai_conv = ai_conv

        self.answer = to_raw_response_wrapper(
            ai_conv.answer,
        )
        self.relation = to_raw_response_wrapper(
            ai_conv.relation,
        )
        self.validate = to_raw_response_wrapper(
            ai_conv.validate,
        )


class AsyncAIConvResourceWithRawResponse:
    def __init__(self, ai_conv: AsyncAIConvResource) -> None:
        self._ai_conv = ai_conv

        self.answer = async_to_raw_response_wrapper(
            ai_conv.answer,
        )
        self.relation = async_to_raw_response_wrapper(
            ai_conv.relation,
        )
        self.validate = async_to_raw_response_wrapper(
            ai_conv.validate,
        )


class AIConvResourceWithStreamingResponse:
    def __init__(self, ai_conv: AIConvResource) -> None:
        self._ai_conv = ai_conv

        self.answer = to_streamed_response_wrapper(
            ai_conv.answer,
        )
        self.relation = to_streamed_response_wrapper(
            ai_conv.relation,
        )
        self.validate = to_streamed_response_wrapper(
            ai_conv.validate,
        )


class AsyncAIConvResourceWithStreamingResponse:
    def __init__(self, ai_conv: AsyncAIConvResource) -> None:
        self._ai_conv = ai_conv

        self.answer = async_to_streamed_response_wrapper(
            ai_conv.answer,
        )
        self.relation = async_to_streamed_response_wrapper(
            ai_conv.relation,
        )
        self.validate = async_to_streamed_response_wrapper(
            ai_conv.validate,
        )
