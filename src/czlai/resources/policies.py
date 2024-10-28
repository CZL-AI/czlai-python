# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import policy_policy_info_params
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

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def policy_info(
        self,
        *,
        keys: str | NotGiven = NOT_GIVEN,
        policy_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        政策类型

        Args:
          keys: 密钥

          policy_type: 1-用户协议 2-免责条款 3-隐私政策

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/policy/policy_info",
            body=maybe_transform(
                {
                    "keys": keys,
                    "policy_type": policy_type,
                },
                policy_policy_info_params.PolicyPolicyInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def policy_info(
        self,
        *,
        keys: str | NotGiven = NOT_GIVEN,
        policy_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        政策类型

        Args:
          keys: 密钥

          policy_type: 1-用户协议 2-免责条款 3-隐私政策

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/policy/policy_info",
            body=await async_maybe_transform(
                {
                    "keys": keys,
                    "policy_type": policy_type,
                },
                policy_policy_info_params.PolicyPolicyInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.policy_info = to_raw_response_wrapper(
            policies.policy_info,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.policy_info = async_to_raw_response_wrapper(
            policies.policy_info,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.policy_info = to_streamed_response_wrapper(
            policies.policy_info,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.policy_info = async_to_streamed_response_wrapper(
            policies.policy_info,
        )
