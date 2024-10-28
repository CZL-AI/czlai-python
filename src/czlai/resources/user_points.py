# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import user_point_cost_report_params
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
from ..types.user_point_retrieve_response import UserPointRetrieveResponse

__all__ = ["UserPointsResource", "AsyncUserPointsResource"]


class UserPointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UserPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UserPointsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPointRetrieveResponse:
        """获取用户积分"""
        return self._get(
            "/user-point",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPointRetrieveResponse,
        )

    def cost_report(
        self,
        *,
        item_key: str | NotGiven = NOT_GIVEN,
        medical_record_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        积分消耗报表

        Args:
          medical_record_id: 病历 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/user-point/cost-report",
            body=maybe_transform(
                {
                    "item_key": item_key,
                    "medical_record_id": medical_record_id,
                },
                user_point_cost_report_params.UserPointCostReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUserPointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUserPointsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPointRetrieveResponse:
        """获取用户积分"""
        return await self._get(
            "/user-point",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPointRetrieveResponse,
        )

    async def cost_report(
        self,
        *,
        item_key: str | NotGiven = NOT_GIVEN,
        medical_record_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        积分消耗报表

        Args:
          medical_record_id: 病历 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/user-point/cost-report",
            body=await async_maybe_transform(
                {
                    "item_key": item_key,
                    "medical_record_id": medical_record_id,
                },
                user_point_cost_report_params.UserPointCostReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UserPointsResourceWithRawResponse:
    def __init__(self, user_points: UserPointsResource) -> None:
        self._user_points = user_points

        self.retrieve = to_raw_response_wrapper(
            user_points.retrieve,
        )
        self.cost_report = to_raw_response_wrapper(
            user_points.cost_report,
        )


class AsyncUserPointsResourceWithRawResponse:
    def __init__(self, user_points: AsyncUserPointsResource) -> None:
        self._user_points = user_points

        self.retrieve = async_to_raw_response_wrapper(
            user_points.retrieve,
        )
        self.cost_report = async_to_raw_response_wrapper(
            user_points.cost_report,
        )


class UserPointsResourceWithStreamingResponse:
    def __init__(self, user_points: UserPointsResource) -> None:
        self._user_points = user_points

        self.retrieve = to_streamed_response_wrapper(
            user_points.retrieve,
        )
        self.cost_report = to_streamed_response_wrapper(
            user_points.cost_report,
        )


class AsyncUserPointsResourceWithStreamingResponse:
    def __init__(self, user_points: AsyncUserPointsResource) -> None:
        self._user_points = user_points

        self.retrieve = async_to_streamed_response_wrapper(
            user_points.retrieve,
        )
        self.cost_report = async_to_streamed_response_wrapper(
            user_points.cost_report,
        )
