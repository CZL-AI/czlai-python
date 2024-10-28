# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import whitelist_save_data_params, whitelist_filtering_data_params
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

__all__ = ["WhitelistResource", "AsyncWhitelistResource"]


class WhitelistResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhitelistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return WhitelistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhitelistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return WhitelistResourceWithStreamingResponse(self)

    def filtering_data(
        self,
        *,
        filtering_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        白名单数据过滤

        Args:
          filtering_data: 过滤数据

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/whitelist/filtering_data",
            body=maybe_transform(
                {"filtering_data": filtering_data}, whitelist_filtering_data_params.WhitelistFilteringDataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def save_data(
        self,
        *,
        save_data: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        白名单数据保存

        Args:
          save_data: 保存数据

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/whitelist/save_data",
            body=maybe_transform({"save_data": save_data}, whitelist_save_data_params.WhitelistSaveDataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWhitelistResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhitelistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhitelistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhitelistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncWhitelistResourceWithStreamingResponse(self)

    async def filtering_data(
        self,
        *,
        filtering_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        白名单数据过滤

        Args:
          filtering_data: 过滤数据

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/whitelist/filtering_data",
            body=await async_maybe_transform(
                {"filtering_data": filtering_data}, whitelist_filtering_data_params.WhitelistFilteringDataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def save_data(
        self,
        *,
        save_data: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        白名单数据保存

        Args:
          save_data: 保存数据

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/whitelist/save_data",
            body=await async_maybe_transform(
                {"save_data": save_data}, whitelist_save_data_params.WhitelistSaveDataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WhitelistResourceWithRawResponse:
    def __init__(self, whitelist: WhitelistResource) -> None:
        self._whitelist = whitelist

        self.filtering_data = to_raw_response_wrapper(
            whitelist.filtering_data,
        )
        self.save_data = to_raw_response_wrapper(
            whitelist.save_data,
        )


class AsyncWhitelistResourceWithRawResponse:
    def __init__(self, whitelist: AsyncWhitelistResource) -> None:
        self._whitelist = whitelist

        self.filtering_data = async_to_raw_response_wrapper(
            whitelist.filtering_data,
        )
        self.save_data = async_to_raw_response_wrapper(
            whitelist.save_data,
        )


class WhitelistResourceWithStreamingResponse:
    def __init__(self, whitelist: WhitelistResource) -> None:
        self._whitelist = whitelist

        self.filtering_data = to_streamed_response_wrapper(
            whitelist.filtering_data,
        )
        self.save_data = to_streamed_response_wrapper(
            whitelist.save_data,
        )


class AsyncWhitelistResourceWithStreamingResponse:
    def __init__(self, whitelist: AsyncWhitelistResource) -> None:
        self._whitelist = whitelist

        self.filtering_data = async_to_streamed_response_wrapper(
            whitelist.filtering_data,
        )
        self.save_data = async_to_streamed_response_wrapper(
            whitelist.save_data,
        )
