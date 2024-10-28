# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.pets import pet_info_retrieve_params
from ..._base_client import make_request_options

__all__ = ["PetInfoResource", "AsyncPetInfoResource"]


class PetInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PetInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PetInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PetInfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        pets_type: Literal["dog", "cat"],
        is_sort: Literal[0, 1] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        宠物数据

        Args:
          pets_type: dog cat

          is_sort: 0-分组 1-不分组

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/pets/pet-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "pets_type": pets_type,
                        "is_sort": is_sort,
                    },
                    pet_info_retrieve_params.PetInfoRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncPetInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPetInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPetInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPetInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        pets_type: Literal["dog", "cat"],
        is_sort: Literal[0, 1] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        宠物数据

        Args:
          pets_type: dog cat

          is_sort: 0-分组 1-不分组

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/pets/pet-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "pets_type": pets_type,
                        "is_sort": is_sort,
                    },
                    pet_info_retrieve_params.PetInfoRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class PetInfoResourceWithRawResponse:
    def __init__(self, pet_info: PetInfoResource) -> None:
        self._pet_info = pet_info

        self.retrieve = to_raw_response_wrapper(
            pet_info.retrieve,
        )


class AsyncPetInfoResourceWithRawResponse:
    def __init__(self, pet_info: AsyncPetInfoResource) -> None:
        self._pet_info = pet_info

        self.retrieve = async_to_raw_response_wrapper(
            pet_info.retrieve,
        )


class PetInfoResourceWithStreamingResponse:
    def __init__(self, pet_info: PetInfoResource) -> None:
        self._pet_info = pet_info

        self.retrieve = to_streamed_response_wrapper(
            pet_info.retrieve,
        )


class AsyncPetInfoResourceWithStreamingResponse:
    def __init__(self, pet_info: AsyncPetInfoResource) -> None:
        self._pet_info = pet_info

        self.retrieve = async_to_streamed_response_wrapper(
            pet_info.retrieve,
        )
