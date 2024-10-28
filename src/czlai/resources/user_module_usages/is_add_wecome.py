# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.user_module_usages.is_add_wecome_retrieve_response import IsAddWecomeRetrieveResponse

__all__ = ["IsAddWecomeResource", "AsyncIsAddWecomeResource"]


class IsAddWecomeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IsAddWecomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return IsAddWecomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IsAddWecomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return IsAddWecomeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IsAddWecomeRetrieveResponse:
        """是否领取过添加企微的奖励"""
        return self._get(
            "/user-module-usage/is-add-wecome",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsAddWecomeRetrieveResponse,
        )


class AsyncIsAddWecomeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIsAddWecomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIsAddWecomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIsAddWecomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncIsAddWecomeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IsAddWecomeRetrieveResponse:
        """是否领取过添加企微的奖励"""
        return await self._get(
            "/user-module-usage/is-add-wecome",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsAddWecomeRetrieveResponse,
        )


class IsAddWecomeResourceWithRawResponse:
    def __init__(self, is_add_wecome: IsAddWecomeResource) -> None:
        self._is_add_wecome = is_add_wecome

        self.retrieve = to_raw_response_wrapper(
            is_add_wecome.retrieve,
        )


class AsyncIsAddWecomeResourceWithRawResponse:
    def __init__(self, is_add_wecome: AsyncIsAddWecomeResource) -> None:
        self._is_add_wecome = is_add_wecome

        self.retrieve = async_to_raw_response_wrapper(
            is_add_wecome.retrieve,
        )


class IsAddWecomeResourceWithStreamingResponse:
    def __init__(self, is_add_wecome: IsAddWecomeResource) -> None:
        self._is_add_wecome = is_add_wecome

        self.retrieve = to_streamed_response_wrapper(
            is_add_wecome.retrieve,
        )


class AsyncIsAddWecomeResourceWithStreamingResponse:
    def __init__(self, is_add_wecome: AsyncIsAddWecomeResource) -> None:
        self._is_add_wecome = is_add_wecome

        self.retrieve = async_to_streamed_response_wrapper(
            is_add_wecome.retrieve,
        )
