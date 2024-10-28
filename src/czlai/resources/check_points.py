# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import check_point_create_params
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

__all__ = ["CheckPointsResource", "AsyncCheckPointsResource"]


class CheckPointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return CheckPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return CheckPointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        page_path: str | NotGiven = NOT_GIVEN,
        related_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        埋点

        Args:
          action: 埋点动作

          code: 微信 code

          page_path: 页面路径

          related_id: 关联 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/check-point",
            body=maybe_transform(
                {
                    "action": action,
                    "code": code,
                    "page_path": page_path,
                    "related_id": related_id,
                },
                check_point_create_params.CheckPointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCheckPointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncCheckPointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        page_path: str | NotGiven = NOT_GIVEN,
        related_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        埋点

        Args:
          action: 埋点动作

          code: 微信 code

          page_path: 页面路径

          related_id: 关联 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/check-point",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "code": code,
                    "page_path": page_path,
                    "related_id": related_id,
                },
                check_point_create_params.CheckPointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CheckPointsResourceWithRawResponse:
    def __init__(self, check_points: CheckPointsResource) -> None:
        self._check_points = check_points

        self.create = to_raw_response_wrapper(
            check_points.create,
        )


class AsyncCheckPointsResourceWithRawResponse:
    def __init__(self, check_points: AsyncCheckPointsResource) -> None:
        self._check_points = check_points

        self.create = async_to_raw_response_wrapper(
            check_points.create,
        )


class CheckPointsResourceWithStreamingResponse:
    def __init__(self, check_points: CheckPointsResource) -> None:
        self._check_points = check_points

        self.create = to_streamed_response_wrapper(
            check_points.create,
        )


class AsyncCheckPointsResourceWithStreamingResponse:
    def __init__(self, check_points: AsyncCheckPointsResource) -> None:
        self._check_points = check_points

        self.create = async_to_streamed_response_wrapper(
            check_points.create,
        )
