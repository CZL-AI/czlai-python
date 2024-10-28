# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import user_info_retrieve_params
from ..._base_client import make_request_options

__all__ = ["UserInfoResource", "AsyncUserInfoResource"]


class UserInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UserInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UserInfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取用户信息

        Args:
          uuid: 用户 UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/user-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"uuid": uuid}, user_info_retrieve_params.UserInfoRetrieveParams),
            ),
            cast_to=NoneType,
        )


class AsyncUserInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUserInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取用户信息

        Args:
          uuid: 用户 UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/user-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"uuid": uuid}, user_info_retrieve_params.UserInfoRetrieveParams),
            ),
            cast_to=NoneType,
        )


class UserInfoResourceWithRawResponse:
    def __init__(self, user_info: UserInfoResource) -> None:
        self._user_info = user_info

        self.retrieve = to_raw_response_wrapper(
            user_info.retrieve,
        )


class AsyncUserInfoResourceWithRawResponse:
    def __init__(self, user_info: AsyncUserInfoResource) -> None:
        self._user_info = user_info

        self.retrieve = async_to_raw_response_wrapper(
            user_info.retrieve,
        )


class UserInfoResourceWithStreamingResponse:
    def __init__(self, user_info: UserInfoResource) -> None:
        self._user_info = user_info

        self.retrieve = to_streamed_response_wrapper(
            user_info.retrieve,
        )


class AsyncUserInfoResourceWithStreamingResponse:
    def __init__(self, user_info: AsyncUserInfoResource) -> None:
        self._user_info = user_info

        self.retrieve = async_to_streamed_response_wrapper(
            user_info.retrieve,
        )
