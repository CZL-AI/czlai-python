# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import aipic_summary_params
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

__all__ = ["AipicsResource", "AsyncAipicsResource"]


class AipicsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AipicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AipicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AipicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AipicsResourceWithStreamingResponse(self)

    def summary(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取小结(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aipic/summary",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_summary_params.AipicSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAipicsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAipicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAipicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAipicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAipicsResourceWithStreamingResponse(self)

    async def summary(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sub_module_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取小结(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          sub_module_type: 图片归属(1:宠物体态分析、2:宠物表情分析)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aipic/summary",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                    "sub_module_type": sub_module_type,
                },
                aipic_summary_params.AipicSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AipicsResourceWithRawResponse:
    def __init__(self, aipics: AipicsResource) -> None:
        self._aipics = aipics

        self.summary = to_raw_response_wrapper(
            aipics.summary,
        )


class AsyncAipicsResourceWithRawResponse:
    def __init__(self, aipics: AsyncAipicsResource) -> None:
        self._aipics = aipics

        self.summary = async_to_raw_response_wrapper(
            aipics.summary,
        )


class AipicsResourceWithStreamingResponse:
    def __init__(self, aipics: AipicsResource) -> None:
        self._aipics = aipics

        self.summary = to_streamed_response_wrapper(
            aipics.summary,
        )


class AsyncAipicsResourceWithStreamingResponse:
    def __init__(self, aipics: AsyncAipicsResource) -> None:
        self._aipics = aipics

        self.summary = async_to_streamed_response_wrapper(
            aipics.summary,
        )
