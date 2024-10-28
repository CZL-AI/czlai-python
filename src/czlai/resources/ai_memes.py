# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ai_meme_create_params, ai_meme_generate_params, ai_meme_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.ai_meme_create_response import AIMemeCreateResponse
from ..types.ai_meme_generate_response import AIMemeGenerateResponse
from ..types.ai_meme_retrieve_response import AIMemeRetrieveResponse

__all__ = ["AIMemesResource", "AsyncAIMemesResource"]


class AIMemesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIMemesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AIMemesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIMemesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AIMemesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image_url: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeCreateResponse:
        """
        获取表情包数据

        Args:
          image_url: 图片地址

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai-meme",
            body=maybe_transform(
                {
                    "image_url": image_url,
                    "session_id": session_id,
                },
                ai_meme_create_params.AIMemeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIMemeCreateResponse,
        )

    def retrieve(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeRetrieveResponse:
        """
        获取用户历史表情包数据列表

        Args:
          limit: 每页数量

          page: 页数

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai-meme",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    ai_meme_retrieve_params.AIMemeRetrieveParams,
                ),
            ),
            cast_to=AIMemeRetrieveResponse,
        )

    def generate(
        self,
        *,
        context_index: int | NotGiven = NOT_GIVEN,
        meme_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeGenerateResponse:
        """
        获取 AI 表情包

        Args:
          context_index: 文案序号

          meme_id: 表情包 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai-meme/generate",
            body=maybe_transform(
                {
                    "context_index": context_index,
                    "meme_id": meme_id,
                },
                ai_meme_generate_params.AIMemeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIMemeGenerateResponse,
        )


class AsyncAIMemesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIMemesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIMemesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIMemesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAIMemesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image_url: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeCreateResponse:
        """
        获取表情包数据

        Args:
          image_url: 图片地址

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai-meme",
            body=await async_maybe_transform(
                {
                    "image_url": image_url,
                    "session_id": session_id,
                },
                ai_meme_create_params.AIMemeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIMemeCreateResponse,
        )

    async def retrieve(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeRetrieveResponse:
        """
        获取用户历史表情包数据列表

        Args:
          limit: 每页数量

          page: 页数

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai-meme",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    ai_meme_retrieve_params.AIMemeRetrieveParams,
                ),
            ),
            cast_to=AIMemeRetrieveResponse,
        )

    async def generate(
        self,
        *,
        context_index: int | NotGiven = NOT_GIVEN,
        meme_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIMemeGenerateResponse:
        """
        获取 AI 表情包

        Args:
          context_index: 文案序号

          meme_id: 表情包 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai-meme/generate",
            body=await async_maybe_transform(
                {
                    "context_index": context_index,
                    "meme_id": meme_id,
                },
                ai_meme_generate_params.AIMemeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIMemeGenerateResponse,
        )


class AIMemesResourceWithRawResponse:
    def __init__(self, ai_memes: AIMemesResource) -> None:
        self._ai_memes = ai_memes

        self.create = to_raw_response_wrapper(
            ai_memes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ai_memes.retrieve,
        )
        self.generate = to_raw_response_wrapper(
            ai_memes.generate,
        )


class AsyncAIMemesResourceWithRawResponse:
    def __init__(self, ai_memes: AsyncAIMemesResource) -> None:
        self._ai_memes = ai_memes

        self.create = async_to_raw_response_wrapper(
            ai_memes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ai_memes.retrieve,
        )
        self.generate = async_to_raw_response_wrapper(
            ai_memes.generate,
        )


class AIMemesResourceWithStreamingResponse:
    def __init__(self, ai_memes: AIMemesResource) -> None:
        self._ai_memes = ai_memes

        self.create = to_streamed_response_wrapper(
            ai_memes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ai_memes.retrieve,
        )
        self.generate = to_streamed_response_wrapper(
            ai_memes.generate,
        )


class AsyncAIMemesResourceWithStreamingResponse:
    def __init__(self, ai_memes: AsyncAIMemesResource) -> None:
        self._ai_memes = ai_memes

        self.create = async_to_streamed_response_wrapper(
            ai_memes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ai_memes.retrieve,
        )
        self.generate = async_to_streamed_response_wrapper(
            ai_memes.generate,
        )
