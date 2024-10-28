# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import point_task_bonus_params, point_task_confirm_params
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
from ..types.point_task_list_response import PointTaskListResponse

__all__ = ["PointTasksResource", "AsyncPointTasksResource"]


class PointTasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PointTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PointTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PointTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PointTasksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointTaskListResponse:
        """获取积分任务列表"""
        return self._get(
            "/point-task",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PointTaskListResponse,
        )

    def bonus(
        self,
        *,
        task_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        领取奖励

        Args:
          task_id: 任务 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/point-task/bonus",
            body=maybe_transform({"task_id": task_id}, point_task_bonus_params.PointTaskBonusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def confirm(
        self,
        *,
        task_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        确认积分任务

        Args:
          task_id: 任务 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/point-task/confirm",
            body=maybe_transform({"task_id": task_id}, point_task_confirm_params.PointTaskConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPointTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPointTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPointTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPointTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPointTasksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PointTaskListResponse:
        """获取积分任务列表"""
        return await self._get(
            "/point-task",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PointTaskListResponse,
        )

    async def bonus(
        self,
        *,
        task_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        领取奖励

        Args:
          task_id: 任务 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/point-task/bonus",
            body=await async_maybe_transform({"task_id": task_id}, point_task_bonus_params.PointTaskBonusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def confirm(
        self,
        *,
        task_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        确认积分任务

        Args:
          task_id: 任务 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/point-task/confirm",
            body=await async_maybe_transform({"task_id": task_id}, point_task_confirm_params.PointTaskConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PointTasksResourceWithRawResponse:
    def __init__(self, point_tasks: PointTasksResource) -> None:
        self._point_tasks = point_tasks

        self.list = to_raw_response_wrapper(
            point_tasks.list,
        )
        self.bonus = to_raw_response_wrapper(
            point_tasks.bonus,
        )
        self.confirm = to_raw_response_wrapper(
            point_tasks.confirm,
        )


class AsyncPointTasksResourceWithRawResponse:
    def __init__(self, point_tasks: AsyncPointTasksResource) -> None:
        self._point_tasks = point_tasks

        self.list = async_to_raw_response_wrapper(
            point_tasks.list,
        )
        self.bonus = async_to_raw_response_wrapper(
            point_tasks.bonus,
        )
        self.confirm = async_to_raw_response_wrapper(
            point_tasks.confirm,
        )


class PointTasksResourceWithStreamingResponse:
    def __init__(self, point_tasks: PointTasksResource) -> None:
        self._point_tasks = point_tasks

        self.list = to_streamed_response_wrapper(
            point_tasks.list,
        )
        self.bonus = to_streamed_response_wrapper(
            point_tasks.bonus,
        )
        self.confirm = to_streamed_response_wrapper(
            point_tasks.confirm,
        )


class AsyncPointTasksResourceWithStreamingResponse:
    def __init__(self, point_tasks: AsyncPointTasksResource) -> None:
        self._point_tasks = point_tasks

        self.list = async_to_streamed_response_wrapper(
            point_tasks.list,
        )
        self.bonus = async_to_streamed_response_wrapper(
            point_tasks.bonus,
        )
        self.confirm = async_to_streamed_response_wrapper(
            point_tasks.confirm,
        )
