# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    magnum_key_get_key_params,
    magnum_key_voice_choice_params,
    magnum_key_picture_choice_params,
    magnum_key_voice_question_params,
    magnum_key_picture_question_params,
)
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

__all__ = ["MagnumKeysResource", "AsyncMagnumKeysResource"]


class MagnumKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MagnumKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return MagnumKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagnumKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return MagnumKeysResourceWithStreamingResponse(self)

    def get_key(
        self,
        *,
        context: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取 key_usage_id

        Args:
          context: 文本

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/magnumkey/get-key",
            body=maybe_transform({"context": context}, magnum_key_get_key_params.MagnumKeyGetKeyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def picture_choice(
        self,
        *,
        img_url: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片选项

        Args:
          img_url: 图片 url

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/magnumkey/picture-choice",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_picture_choice_params.MagnumKeyPictureChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def picture_question(
        self,
        *,
        img_url: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片问题

        Args:
          img_url: 图片 url

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/magnumkey/picture-question",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_picture_question_params.MagnumKeyPictureQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def voice_choice(
        self,
        *,
        message: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取声音选项

        Args:
          message: 获取声音选项

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/magnumkey/voice-choice",
            body=maybe_transform(
                {
                    "message": message,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_voice_choice_params.MagnumKeyVoiceChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def voice_question(
        self,
        *,
        message: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取声音问题

        Args:
          message: 语音文本

          key_usage_id: 会话 id

          pet_id: 宠物 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/magnumkey/voice-question",
            body=maybe_transform(
                {
                    "message": message,
                    "key_usage_id": key_usage_id,
                    "pet_id": pet_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_voice_question_params.MagnumKeyVoiceQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMagnumKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMagnumKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMagnumKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagnumKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncMagnumKeysResourceWithStreamingResponse(self)

    async def get_key(
        self,
        *,
        context: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取 key_usage_id

        Args:
          context: 文本

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/magnumkey/get-key",
            body=await async_maybe_transform({"context": context}, magnum_key_get_key_params.MagnumKeyGetKeyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def picture_choice(
        self,
        *,
        img_url: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片选项

        Args:
          img_url: 图片 url

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/magnumkey/picture-choice",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_picture_choice_params.MagnumKeyPictureChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def picture_question(
        self,
        *,
        img_url: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片问题

        Args:
          img_url: 图片 url

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/magnumkey/picture-question",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_picture_question_params.MagnumKeyPictureQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def voice_choice(
        self,
        *,
        message: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取声音选项

        Args:
          message: 获取声音选项

          key_usage_id: 会话 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/magnumkey/voice-choice",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "key_usage_id": key_usage_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_voice_choice_params.MagnumKeyVoiceChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def voice_question(
        self,
        *,
        message: str,
        key_usage_id: Optional[str] | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取声音问题

        Args:
          message: 语音文本

          key_usage_id: 会话 id

          pet_id: 宠物 id

          user_uuid: 用户 uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/magnumkey/voice-question",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "key_usage_id": key_usage_id,
                    "pet_id": pet_id,
                    "user_uuid": user_uuid,
                },
                magnum_key_voice_question_params.MagnumKeyVoiceQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MagnumKeysResourceWithRawResponse:
    def __init__(self, magnum_keys: MagnumKeysResource) -> None:
        self._magnum_keys = magnum_keys

        self.get_key = to_raw_response_wrapper(
            magnum_keys.get_key,
        )
        self.picture_choice = to_raw_response_wrapper(
            magnum_keys.picture_choice,
        )
        self.picture_question = to_raw_response_wrapper(
            magnum_keys.picture_question,
        )
        self.voice_choice = to_raw_response_wrapper(
            magnum_keys.voice_choice,
        )
        self.voice_question = to_raw_response_wrapper(
            magnum_keys.voice_question,
        )


class AsyncMagnumKeysResourceWithRawResponse:
    def __init__(self, magnum_keys: AsyncMagnumKeysResource) -> None:
        self._magnum_keys = magnum_keys

        self.get_key = async_to_raw_response_wrapper(
            magnum_keys.get_key,
        )
        self.picture_choice = async_to_raw_response_wrapper(
            magnum_keys.picture_choice,
        )
        self.picture_question = async_to_raw_response_wrapper(
            magnum_keys.picture_question,
        )
        self.voice_choice = async_to_raw_response_wrapper(
            magnum_keys.voice_choice,
        )
        self.voice_question = async_to_raw_response_wrapper(
            magnum_keys.voice_question,
        )


class MagnumKeysResourceWithStreamingResponse:
    def __init__(self, magnum_keys: MagnumKeysResource) -> None:
        self._magnum_keys = magnum_keys

        self.get_key = to_streamed_response_wrapper(
            magnum_keys.get_key,
        )
        self.picture_choice = to_streamed_response_wrapper(
            magnum_keys.picture_choice,
        )
        self.picture_question = to_streamed_response_wrapper(
            magnum_keys.picture_question,
        )
        self.voice_choice = to_streamed_response_wrapper(
            magnum_keys.voice_choice,
        )
        self.voice_question = to_streamed_response_wrapper(
            magnum_keys.voice_question,
        )


class AsyncMagnumKeysResourceWithStreamingResponse:
    def __init__(self, magnum_keys: AsyncMagnumKeysResource) -> None:
        self._magnum_keys = magnum_keys

        self.get_key = async_to_streamed_response_wrapper(
            magnum_keys.get_key,
        )
        self.picture_choice = async_to_streamed_response_wrapper(
            magnum_keys.picture_choice,
        )
        self.picture_question = async_to_streamed_response_wrapper(
            magnum_keys.picture_question,
        )
        self.voice_choice = async_to_streamed_response_wrapper(
            magnum_keys.voice_choice,
        )
        self.voice_question = async_to_streamed_response_wrapper(
            magnum_keys.voice_question,
        )
