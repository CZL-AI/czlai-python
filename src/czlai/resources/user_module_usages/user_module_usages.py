# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import user_module_usage_get_add_wecome_bonus_params
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
from .is_add_wecome import (
    IsAddWecomeResource,
    AsyncIsAddWecomeResource,
    IsAddWecomeResourceWithRawResponse,
    AsyncIsAddWecomeResourceWithRawResponse,
    IsAddWecomeResourceWithStreamingResponse,
    AsyncIsAddWecomeResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.user_module_usage_get_add_wecome_bonus_response import UserModuleUsageGetAddWecomeBonusResponse
from ...types.user_module_usage_get_wechat_mini_qrcode_response import UserModuleUsageGetWechatMiniQrcodeResponse

__all__ = ["UserModuleUsagesResource", "AsyncUserModuleUsagesResource"]


class UserModuleUsagesResource(SyncAPIResource):
    @cached_property
    def is_add_wecome(self) -> IsAddWecomeResource:
        return IsAddWecomeResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserModuleUsagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UserModuleUsagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserModuleUsagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UserModuleUsagesResourceWithStreamingResponse(self)

    def checkin(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """签到"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/user-module-usage/checkin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_add_wecome_bonus(
        self,
        *,
        module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserModuleUsageGetAddWecomeBonusResponse:
        """
        领取添加企微的奖励

        Args:
          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user-module-usage/get-add-wecome-bonus",
            body=maybe_transform(
                {"module_type": module_type},
                user_module_usage_get_add_wecome_bonus_params.UserModuleUsageGetAddWecomeBonusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModuleUsageGetAddWecomeBonusResponse,
        )

    def get_wechat_mini_qrcode(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserModuleUsageGetWechatMiniQrcodeResponse:
        """获取微信小程序二维码"""
        return self._post(
            "/user-module-usage/get-wechat-mini-qrcode",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModuleUsageGetWechatMiniQrcodeResponse,
        )


class AsyncUserModuleUsagesResource(AsyncAPIResource):
    @cached_property
    def is_add_wecome(self) -> AsyncIsAddWecomeResource:
        return AsyncIsAddWecomeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserModuleUsagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserModuleUsagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserModuleUsagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUserModuleUsagesResourceWithStreamingResponse(self)

    async def checkin(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """签到"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/user-module-usage/checkin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_add_wecome_bonus(
        self,
        *,
        module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserModuleUsageGetAddWecomeBonusResponse:
        """
        领取添加企微的奖励

        Args:
          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user-module-usage/get-add-wecome-bonus",
            body=await async_maybe_transform(
                {"module_type": module_type},
                user_module_usage_get_add_wecome_bonus_params.UserModuleUsageGetAddWecomeBonusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModuleUsageGetAddWecomeBonusResponse,
        )

    async def get_wechat_mini_qrcode(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserModuleUsageGetWechatMiniQrcodeResponse:
        """获取微信小程序二维码"""
        return await self._post(
            "/user-module-usage/get-wechat-mini-qrcode",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModuleUsageGetWechatMiniQrcodeResponse,
        )


class UserModuleUsagesResourceWithRawResponse:
    def __init__(self, user_module_usages: UserModuleUsagesResource) -> None:
        self._user_module_usages = user_module_usages

        self.checkin = to_raw_response_wrapper(
            user_module_usages.checkin,
        )
        self.get_add_wecome_bonus = to_raw_response_wrapper(
            user_module_usages.get_add_wecome_bonus,
        )
        self.get_wechat_mini_qrcode = to_raw_response_wrapper(
            user_module_usages.get_wechat_mini_qrcode,
        )

    @cached_property
    def is_add_wecome(self) -> IsAddWecomeResourceWithRawResponse:
        return IsAddWecomeResourceWithRawResponse(self._user_module_usages.is_add_wecome)


class AsyncUserModuleUsagesResourceWithRawResponse:
    def __init__(self, user_module_usages: AsyncUserModuleUsagesResource) -> None:
        self._user_module_usages = user_module_usages

        self.checkin = async_to_raw_response_wrapper(
            user_module_usages.checkin,
        )
        self.get_add_wecome_bonus = async_to_raw_response_wrapper(
            user_module_usages.get_add_wecome_bonus,
        )
        self.get_wechat_mini_qrcode = async_to_raw_response_wrapper(
            user_module_usages.get_wechat_mini_qrcode,
        )

    @cached_property
    def is_add_wecome(self) -> AsyncIsAddWecomeResourceWithRawResponse:
        return AsyncIsAddWecomeResourceWithRawResponse(self._user_module_usages.is_add_wecome)


class UserModuleUsagesResourceWithStreamingResponse:
    def __init__(self, user_module_usages: UserModuleUsagesResource) -> None:
        self._user_module_usages = user_module_usages

        self.checkin = to_streamed_response_wrapper(
            user_module_usages.checkin,
        )
        self.get_add_wecome_bonus = to_streamed_response_wrapper(
            user_module_usages.get_add_wecome_bonus,
        )
        self.get_wechat_mini_qrcode = to_streamed_response_wrapper(
            user_module_usages.get_wechat_mini_qrcode,
        )

    @cached_property
    def is_add_wecome(self) -> IsAddWecomeResourceWithStreamingResponse:
        return IsAddWecomeResourceWithStreamingResponse(self._user_module_usages.is_add_wecome)


class AsyncUserModuleUsagesResourceWithStreamingResponse:
    def __init__(self, user_module_usages: AsyncUserModuleUsagesResource) -> None:
        self._user_module_usages = user_module_usages

        self.checkin = async_to_streamed_response_wrapper(
            user_module_usages.checkin,
        )
        self.get_add_wecome_bonus = async_to_streamed_response_wrapper(
            user_module_usages.get_add_wecome_bonus,
        )
        self.get_wechat_mini_qrcode = async_to_streamed_response_wrapper(
            user_module_usages.get_wechat_mini_qrcode,
        )

    @cached_property
    def is_add_wecome(self) -> AsyncIsAddWecomeResourceWithStreamingResponse:
        return AsyncIsAddWecomeResourceWithStreamingResponse(self._user_module_usages.is_add_wecome)
