# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.point_price_retrieve_response import PointPriceRetrieveResponse

__all__ = ["PointPricesResource", "AsyncPointPricesResource"]


class PointPricesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PointPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PointPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PointPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PointPricesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointPriceRetrieveResponse:
        """获取积分价格"""
        return self._get(
            "/point-price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PointPriceRetrieveResponse,
        )


class AsyncPointPricesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPointPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPointPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPointPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPointPricesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointPriceRetrieveResponse:
        """获取积分价格"""
        return await self._get(
            "/point-price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PointPriceRetrieveResponse,
        )


class PointPricesResourceWithRawResponse:
    def __init__(self, point_prices: PointPricesResource) -> None:
        self._point_prices = point_prices

        self.retrieve = to_raw_response_wrapper(
            point_prices.retrieve,
        )


class AsyncPointPricesResourceWithRawResponse:
    def __init__(self, point_prices: AsyncPointPricesResource) -> None:
        self._point_prices = point_prices

        self.retrieve = async_to_raw_response_wrapper(
            point_prices.retrieve,
        )


class PointPricesResourceWithStreamingResponse:
    def __init__(self, point_prices: PointPricesResource) -> None:
        self._point_prices = point_prices

        self.retrieve = to_streamed_response_wrapper(
            point_prices.retrieve,
        )


class AsyncPointPricesResourceWithStreamingResponse:
    def __init__(self, point_prices: AsyncPointPricesResource) -> None:
        self._point_prices = point_prices

        self.retrieve = async_to_streamed_response_wrapper(
            point_prices.retrieve,
        )
