# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["IndustryResource", "AsyncIndustryResource"]


class IndustryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return IndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return IndustryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """行业列表"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/industry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncIndustryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncIndustryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """行业列表"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/industry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class IndustryResourceWithRawResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

        self.retrieve = to_raw_response_wrapper(
            industry.retrieve,
        )


class AsyncIndustryResourceWithRawResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

        self.retrieve = async_to_raw_response_wrapper(
            industry.retrieve,
        )


class IndustryResourceWithStreamingResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

        self.retrieve = to_streamed_response_wrapper(
            industry.retrieve,
        )


class AsyncIndustryResourceWithStreamingResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

        self.retrieve = async_to_streamed_response_wrapper(
            industry.retrieve,
        )
