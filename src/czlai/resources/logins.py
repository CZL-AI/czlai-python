# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import login_sms_params, login_wechat_params
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
from ..types.login_response import LoginResponse

__all__ = ["LoginsResource", "AsyncLoginsResource"]


class LoginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return LoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return LoginsResourceWithStreamingResponse(self)

    def sms(
        self,
        *,
        code: str,
        phone: str,
        login_from: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginResponse:
        """
        短信登录

        Args:
          login_from: 1-微信小程序 2-安卓 APP 3-IOS APP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sms-login",
            body=maybe_transform(
                {
                    "code": code,
                    "phone": phone,
                    "login_from": login_from,
                },
                login_sms_params.LoginSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginResponse,
        )

    def wechat(
        self,
        *,
        wechat_code: str,
        encrypted_data: str | NotGiven = NOT_GIVEN,
        iv: str | NotGiven = NOT_GIVEN,
        module_type: int | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        spread_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Logs in the user by WeChat

        Args:
          wechat_code: 会话 id

          encrypted_data: 加密数据

          iv: 加密初始向量

          module_type: 模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图片识别

          phone_number: 手机号

          spread_id: 推广人 sid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/wechat-login",
            body=maybe_transform(
                {
                    "wechat_code": wechat_code,
                    "encrypted_data": encrypted_data,
                    "iv": iv,
                    "module_type": module_type,
                    "phone_number": phone_number,
                    "spread_id": spread_id,
                },
                login_wechat_params.LoginWechatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLoginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncLoginsResourceWithStreamingResponse(self)

    async def sms(
        self,
        *,
        code: str,
        phone: str,
        login_from: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginResponse:
        """
        短信登录

        Args:
          login_from: 1-微信小程序 2-安卓 APP 3-IOS APP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sms-login",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "phone": phone,
                    "login_from": login_from,
                },
                login_sms_params.LoginSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginResponse,
        )

    async def wechat(
        self,
        *,
        wechat_code: str,
        encrypted_data: str | NotGiven = NOT_GIVEN,
        iv: str | NotGiven = NOT_GIVEN,
        module_type: int | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        spread_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Logs in the user by WeChat

        Args:
          wechat_code: 会话 id

          encrypted_data: 加密数据

          iv: 加密初始向量

          module_type: 模块类型 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图片识别

          phone_number: 手机号

          spread_id: 推广人 sid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/wechat-login",
            body=await async_maybe_transform(
                {
                    "wechat_code": wechat_code,
                    "encrypted_data": encrypted_data,
                    "iv": iv,
                    "module_type": module_type,
                    "phone_number": phone_number,
                    "spread_id": spread_id,
                },
                login_wechat_params.LoginWechatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LoginsResourceWithRawResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.sms = to_raw_response_wrapper(
            logins.sms,
        )
        self.wechat = to_raw_response_wrapper(
            logins.wechat,
        )


class AsyncLoginsResourceWithRawResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.sms = async_to_raw_response_wrapper(
            logins.sms,
        )
        self.wechat = async_to_raw_response_wrapper(
            logins.wechat,
        )


class LoginsResourceWithStreamingResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.sms = to_streamed_response_wrapper(
            logins.sms,
        )
        self.wechat = to_streamed_response_wrapper(
            logins.wechat,
        )


class AsyncLoginsResourceWithStreamingResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.sms = async_to_streamed_response_wrapper(
            logins.sms,
        )
        self.wechat = async_to_streamed_response_wrapper(
            logins.wechat,
        )
