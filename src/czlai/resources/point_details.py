# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import point_detail_retrieve_params
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
from ..types.point_detail_retrieve_response import PointDetailRetrieveResponse

__all__ = ["PointDetailsResource", "AsyncPointDetailsResource"]


class PointDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PointDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PointDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PointDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PointDetailsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        is_add: Literal[0, 1, 2] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointDetailRetrieveResponse:
        """
        获取积分明细

        Args:
          is_add: 0-支出 1-收入 2-全部

          limit: 每页数量

          page: 页数

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/point-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_add": is_add,
                        "limit": limit,
                        "page": page,
                    },
                    point_detail_retrieve_params.PointDetailRetrieveParams,
                ),
            ),
            cast_to=PointDetailRetrieveResponse,
        )


class AsyncPointDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPointDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPointDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPointDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPointDetailsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        is_add: Literal[0, 1, 2] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointDetailRetrieveResponse:
        """
        获取积分明细

        Args:
          is_add: 0-支出 1-收入 2-全部

          limit: 每页数量

          page: 页数

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/point-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_add": is_add,
                        "limit": limit,
                        "page": page,
                    },
                    point_detail_retrieve_params.PointDetailRetrieveParams,
                ),
            ),
            cast_to=PointDetailRetrieveResponse,
        )


class PointDetailsResourceWithRawResponse:
    def __init__(self, point_details: PointDetailsResource) -> None:
        self._point_details = point_details

        self.retrieve = to_raw_response_wrapper(
            point_details.retrieve,
        )


class AsyncPointDetailsResourceWithRawResponse:
    def __init__(self, point_details: AsyncPointDetailsResource) -> None:
        self._point_details = point_details

        self.retrieve = async_to_raw_response_wrapper(
            point_details.retrieve,
        )


class PointDetailsResourceWithStreamingResponse:
    def __init__(self, point_details: PointDetailsResource) -> None:
        self._point_details = point_details

        self.retrieve = to_streamed_response_wrapper(
            point_details.retrieve,
        )


class AsyncPointDetailsResourceWithStreamingResponse:
    def __init__(self, point_details: AsyncPointDetailsResource) -> None:
        self._point_details = point_details

        self.retrieve = async_to_streamed_response_wrapper(
            point_details.retrieve,
        )
