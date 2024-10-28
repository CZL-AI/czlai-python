# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pet_info import (
    PetInfoResource,
    AsyncPetInfoResource,
    PetInfoResourceWithRawResponse,
    AsyncPetInfoResourceWithRawResponse,
    PetInfoResourceWithStreamingResponse,
    AsyncPetInfoResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PetsResource", "AsyncPetsResource"]


class PetsResource(SyncAPIResource):
    @cached_property
    def pet_info(self) -> PetInfoResource:
        return PetInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> PetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PetsResourceWithStreamingResponse(self)


class AsyncPetsResource(AsyncAPIResource):
    @cached_property
    def pet_info(self) -> AsyncPetInfoResource:
        return AsyncPetInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPetsResourceWithStreamingResponse(self)


class PetsResourceWithRawResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

    @cached_property
    def pet_info(self) -> PetInfoResourceWithRawResponse:
        return PetInfoResourceWithRawResponse(self._pets.pet_info)


class AsyncPetsResourceWithRawResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

    @cached_property
    def pet_info(self) -> AsyncPetInfoResourceWithRawResponse:
        return AsyncPetInfoResourceWithRawResponse(self._pets.pet_info)


class PetsResourceWithStreamingResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

    @cached_property
    def pet_info(self) -> PetInfoResourceWithStreamingResponse:
        return PetInfoResourceWithStreamingResponse(self._pets.pet_info)


class AsyncPetsResourceWithStreamingResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

    @cached_property
    def pet_info(self) -> AsyncPetInfoResourceWithStreamingResponse:
        return AsyncPetInfoResourceWithStreamingResponse(self._pets.pet_info)
