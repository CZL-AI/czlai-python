# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .asr import (
    AsrResource,
    AsyncAsrResource,
    AsrResourceWithRawResponse,
    AsyncAsrResourceWithRawResponse,
    AsrResourceWithStreamingResponse,
    AsyncAsrResourceWithStreamingResponse,
)
from ...types import user_chat_v_params, user_send_sms_params
from .contact import (
    ContactResource,
    AsyncContactResource,
    ContactResourceWithRawResponse,
    AsyncContactResourceWithRawResponse,
    ContactResourceWithStreamingResponse,
    AsyncContactResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .industry import (
    IndustryResource,
    AsyncIndustryResource,
    IndustryResourceWithRawResponse,
    AsyncIndustryResourceWithRawResponse,
    IndustryResourceWithStreamingResponse,
    AsyncIndustryResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .user_info import (
    UserInfoResource,
    AsyncUserInfoResource,
    UserInfoResourceWithRawResponse,
    AsyncUserInfoResourceWithRawResponse,
    UserInfoResourceWithStreamingResponse,
    AsyncUserInfoResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def user_info(self) -> UserInfoResource:
        return UserInfoResource(self._client)

    @cached_property
    def contact(self) -> ContactResource:
        return ContactResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def asr(self) -> AsrResource:
        return AsrResource(self._client)

    @cached_property
    def industry(self) -> IndustryResource:
        return IndustryResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def chat_v(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        AI 图片聊天

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/chat-v",
            body=maybe_transform(
                {
                    "content": content,
                    "session_id": session_id,
                },
                user_chat_v_params.UserChatVParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Logs out the user"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_sms(
        self,
        *,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发验证短信

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/send-sms",
            body=maybe_transform({"phone": phone}, user_send_sms_params.UserSendSMSParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def user_info(self) -> AsyncUserInfoResource:
        return AsyncUserInfoResource(self._client)

    @cached_property
    def contact(self) -> AsyncContactResource:
        return AsyncContactResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def asr(self) -> AsyncAsrResource:
        return AsyncAsrResource(self._client)

    @cached_property
    def industry(self) -> AsyncIndustryResource:
        return AsyncIndustryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def chat_v(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        AI 图片聊天

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/chat-v",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "session_id": session_id,
                },
                user_chat_v_params.UserChatVParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Logs out the user"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_sms(
        self,
        *,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发验证短信

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/send-sms",
            body=await async_maybe_transform({"phone": phone}, user_send_sms_params.UserSendSMSParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.chat_v = to_raw_response_wrapper(
            users.chat_v,
        )
        self.logout = to_raw_response_wrapper(
            users.logout,
        )
        self.send_sms = to_raw_response_wrapper(
            users.send_sms,
        )

    @cached_property
    def user_info(self) -> UserInfoResourceWithRawResponse:
        return UserInfoResourceWithRawResponse(self._users.user_info)

    @cached_property
    def contact(self) -> ContactResourceWithRawResponse:
        return ContactResourceWithRawResponse(self._users.contact)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._users.summary)

    @cached_property
    def asr(self) -> AsrResourceWithRawResponse:
        return AsrResourceWithRawResponse(self._users.asr)

    @cached_property
    def industry(self) -> IndustryResourceWithRawResponse:
        return IndustryResourceWithRawResponse(self._users.industry)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.chat_v = async_to_raw_response_wrapper(
            users.chat_v,
        )
        self.logout = async_to_raw_response_wrapper(
            users.logout,
        )
        self.send_sms = async_to_raw_response_wrapper(
            users.send_sms,
        )

    @cached_property
    def user_info(self) -> AsyncUserInfoResourceWithRawResponse:
        return AsyncUserInfoResourceWithRawResponse(self._users.user_info)

    @cached_property
    def contact(self) -> AsyncContactResourceWithRawResponse:
        return AsyncContactResourceWithRawResponse(self._users.contact)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._users.summary)

    @cached_property
    def asr(self) -> AsyncAsrResourceWithRawResponse:
        return AsyncAsrResourceWithRawResponse(self._users.asr)

    @cached_property
    def industry(self) -> AsyncIndustryResourceWithRawResponse:
        return AsyncIndustryResourceWithRawResponse(self._users.industry)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.chat_v = to_streamed_response_wrapper(
            users.chat_v,
        )
        self.logout = to_streamed_response_wrapper(
            users.logout,
        )
        self.send_sms = to_streamed_response_wrapper(
            users.send_sms,
        )

    @cached_property
    def user_info(self) -> UserInfoResourceWithStreamingResponse:
        return UserInfoResourceWithStreamingResponse(self._users.user_info)

    @cached_property
    def contact(self) -> ContactResourceWithStreamingResponse:
        return ContactResourceWithStreamingResponse(self._users.contact)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._users.summary)

    @cached_property
    def asr(self) -> AsrResourceWithStreamingResponse:
        return AsrResourceWithStreamingResponse(self._users.asr)

    @cached_property
    def industry(self) -> IndustryResourceWithStreamingResponse:
        return IndustryResourceWithStreamingResponse(self._users.industry)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.chat_v = async_to_streamed_response_wrapper(
            users.chat_v,
        )
        self.logout = async_to_streamed_response_wrapper(
            users.logout,
        )
        self.send_sms = async_to_streamed_response_wrapper(
            users.send_sms,
        )

    @cached_property
    def user_info(self) -> AsyncUserInfoResourceWithStreamingResponse:
        return AsyncUserInfoResourceWithStreamingResponse(self._users.user_info)

    @cached_property
    def contact(self) -> AsyncContactResourceWithStreamingResponse:
        return AsyncContactResourceWithStreamingResponse(self._users.contact)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._users.summary)

    @cached_property
    def asr(self) -> AsyncAsrResourceWithStreamingResponse:
        return AsyncAsrResourceWithStreamingResponse(self._users.asr)

    @cached_property
    def industry(self) -> AsyncIndustryResourceWithStreamingResponse:
        return AsyncIndustryResourceWithStreamingResponse(self._users.industry)
