# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    pet_profile_create_params,
    pet_profile_delete_params,
    pet_profile_update_params,
    pet_profile_ex_info_params,
    pet_profile_variety_params,
    pet_profile_retrieve_params,
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
from ..types.pet_profile_list_response import PetProfileListResponse
from ..types.pet_profile_delete_response import PetProfileDeleteResponse
from ..types.pet_profile_retrieve_response import PetProfileRetrieveResponse

__all__ = ["PetProfilesResource", "AsyncPetProfilesResource"]


class PetProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PetProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return PetProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return PetProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allergy_history: Optional[str] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        birthday: str | NotGiven = NOT_GIVEN,
        disease_history: Optional[str] | NotGiven = NOT_GIVEN,
        family_history: Optional[str] | NotGiven = NOT_GIVEN,
        gender: int | NotGiven = NOT_GIVEN,
        is_neutered: Optional[int] | NotGiven = NOT_GIVEN,
        is_vaccination: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pet_type: int | NotGiven = NOT_GIVEN,
        pet_variety: Optional[str] | NotGiven = NOT_GIVEN,
        vaccination_date: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        创建宠物档案

        Args:
          allergy_history: 过敏史

          avatar: 头像

          birthday: 生日

          disease_history: 疾病史

          family_history: 家族史

          gender: 性别 1-公 2-母

          is_neutered: 是否已绝育 0-否 1-是

          is_vaccination: 是否已接种疫苗 0-否 1-是

          name: 宠物名字

          pet_type: 宠物类型

          pet_variety: 宠物品种

          vaccination_date: 疫苗时间

          weight: 重量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/pet-profile",
            body=maybe_transform(
                {
                    "allergy_history": allergy_history,
                    "avatar": avatar,
                    "birthday": birthday,
                    "disease_history": disease_history,
                    "family_history": family_history,
                    "gender": gender,
                    "is_neutered": is_neutered,
                    "is_vaccination": is_vaccination,
                    "name": name,
                    "pet_type": pet_type,
                    "pet_variety": pet_variety,
                    "vaccination_date": vaccination_date,
                    "weight": weight,
                },
                pet_profile_create_params.PetProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileRetrieveResponse:
        """
        获取宠物档案

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pet-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_retrieve_params.PetProfileRetrieveParams
                ),
            ),
            cast_to=PetProfileRetrieveResponse,
        )

    def update(
        self,
        *,
        pet_profile_id: int,
        allergy_history: Optional[str] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        birthday: str | NotGiven = NOT_GIVEN,
        disease_history: Optional[str] | NotGiven = NOT_GIVEN,
        family_history: Optional[str] | NotGiven = NOT_GIVEN,
        gender: int | NotGiven = NOT_GIVEN,
        is_neutered: Optional[int] | NotGiven = NOT_GIVEN,
        is_vaccination: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pet_type: int | NotGiven = NOT_GIVEN,
        pet_variety: Optional[str] | NotGiven = NOT_GIVEN,
        vaccination_date: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        更新宠物档案

        Args:
          allergy_history: 过敏史

          avatar: 头像

          birthday: 生日

          disease_history: 疾病史

          family_history: 家族史

          gender: 性别 1-公 2-母

          is_neutered: 是否已绝育 0-否 1-是

          is_vaccination: 是否已接种疫苗 0-否 1-是

          name: 宠物名字

          pet_type: 宠物类型

          pet_variety: 宠物品种

          vaccination_date: 疫苗时间

          weight: 重量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/pet-profile",
            body=maybe_transform(
                {
                    "allergy_history": allergy_history,
                    "avatar": avatar,
                    "birthday": birthday,
                    "disease_history": disease_history,
                    "family_history": family_history,
                    "gender": gender,
                    "is_neutered": is_neutered,
                    "is_vaccination": is_vaccination,
                    "name": name,
                    "pet_type": pet_type,
                    "pet_variety": pet_variety,
                    "vaccination_date": vaccination_date,
                    "weight": weight,
                },
                pet_profile_update_params.PetProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_update_params.PetProfileUpdateParams
                ),
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileListResponse:
        """获取宠物档案列表"""
        return self._get(
            "/pet-profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PetProfileListResponse,
        )

    def delete(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileDeleteResponse:
        """
        删除宠物档案

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/pet-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_delete_params.PetProfileDeleteParams
                ),
            ),
            cast_to=PetProfileDeleteResponse,
        )

    def ex_info(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取宠物档案扩展信息

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/pet-profile/ex-info",
            body=maybe_transform({"pet_profile_id": pet_profile_id}, pet_profile_ex_info_params.PetProfileExInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def variety(
        self,
        *,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取宠物品种

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/pet-profile/variety",
            body=maybe_transform({"user_input": user_input}, pet_profile_variety_params.PetProfileVarietyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncPetProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPetProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPetProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncPetProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allergy_history: Optional[str] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        birthday: str | NotGiven = NOT_GIVEN,
        disease_history: Optional[str] | NotGiven = NOT_GIVEN,
        family_history: Optional[str] | NotGiven = NOT_GIVEN,
        gender: int | NotGiven = NOT_GIVEN,
        is_neutered: Optional[int] | NotGiven = NOT_GIVEN,
        is_vaccination: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pet_type: int | NotGiven = NOT_GIVEN,
        pet_variety: Optional[str] | NotGiven = NOT_GIVEN,
        vaccination_date: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        创建宠物档案

        Args:
          allergy_history: 过敏史

          avatar: 头像

          birthday: 生日

          disease_history: 疾病史

          family_history: 家族史

          gender: 性别 1-公 2-母

          is_neutered: 是否已绝育 0-否 1-是

          is_vaccination: 是否已接种疫苗 0-否 1-是

          name: 宠物名字

          pet_type: 宠物类型

          pet_variety: 宠物品种

          vaccination_date: 疫苗时间

          weight: 重量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/pet-profile",
            body=await async_maybe_transform(
                {
                    "allergy_history": allergy_history,
                    "avatar": avatar,
                    "birthday": birthday,
                    "disease_history": disease_history,
                    "family_history": family_history,
                    "gender": gender,
                    "is_neutered": is_neutered,
                    "is_vaccination": is_vaccination,
                    "name": name,
                    "pet_type": pet_type,
                    "pet_variety": pet_variety,
                    "vaccination_date": vaccination_date,
                    "weight": weight,
                },
                pet_profile_create_params.PetProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileRetrieveResponse:
        """
        获取宠物档案

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pet-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_retrieve_params.PetProfileRetrieveParams
                ),
            ),
            cast_to=PetProfileRetrieveResponse,
        )

    async def update(
        self,
        *,
        pet_profile_id: int,
        allergy_history: Optional[str] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        birthday: str | NotGiven = NOT_GIVEN,
        disease_history: Optional[str] | NotGiven = NOT_GIVEN,
        family_history: Optional[str] | NotGiven = NOT_GIVEN,
        gender: int | NotGiven = NOT_GIVEN,
        is_neutered: Optional[int] | NotGiven = NOT_GIVEN,
        is_vaccination: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pet_type: int | NotGiven = NOT_GIVEN,
        pet_variety: Optional[str] | NotGiven = NOT_GIVEN,
        vaccination_date: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        更新宠物档案

        Args:
          allergy_history: 过敏史

          avatar: 头像

          birthday: 生日

          disease_history: 疾病史

          family_history: 家族史

          gender: 性别 1-公 2-母

          is_neutered: 是否已绝育 0-否 1-是

          is_vaccination: 是否已接种疫苗 0-否 1-是

          name: 宠物名字

          pet_type: 宠物类型

          pet_variety: 宠物品种

          vaccination_date: 疫苗时间

          weight: 重量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/pet-profile",
            body=await async_maybe_transform(
                {
                    "allergy_history": allergy_history,
                    "avatar": avatar,
                    "birthday": birthday,
                    "disease_history": disease_history,
                    "family_history": family_history,
                    "gender": gender,
                    "is_neutered": is_neutered,
                    "is_vaccination": is_vaccination,
                    "name": name,
                    "pet_type": pet_type,
                    "pet_variety": pet_variety,
                    "vaccination_date": vaccination_date,
                    "weight": weight,
                },
                pet_profile_update_params.PetProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_update_params.PetProfileUpdateParams
                ),
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileListResponse:
        """获取宠物档案列表"""
        return await self._get(
            "/pet-profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PetProfileListResponse,
        )

    async def delete(
        self,
        *,
        pet_profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetProfileDeleteResponse:
        """
        删除宠物档案

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/pet-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pet_profile_id": pet_profile_id}, pet_profile_delete_params.PetProfileDeleteParams
                ),
            ),
            cast_to=PetProfileDeleteResponse,
        )

    async def ex_info(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取宠物档案扩展信息

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/pet-profile/ex-info",
            body=await async_maybe_transform(
                {"pet_profile_id": pet_profile_id}, pet_profile_ex_info_params.PetProfileExInfoParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def variety(
        self,
        *,
        user_input: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取宠物品种

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/pet-profile/variety",
            body=await async_maybe_transform(
                {"user_input": user_input}, pet_profile_variety_params.PetProfileVarietyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class PetProfilesResourceWithRawResponse:
    def __init__(self, pet_profiles: PetProfilesResource) -> None:
        self._pet_profiles = pet_profiles

        self.create = to_raw_response_wrapper(
            pet_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pet_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pet_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            pet_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            pet_profiles.delete,
        )
        self.ex_info = to_raw_response_wrapper(
            pet_profiles.ex_info,
        )
        self.variety = to_raw_response_wrapper(
            pet_profiles.variety,
        )


class AsyncPetProfilesResourceWithRawResponse:
    def __init__(self, pet_profiles: AsyncPetProfilesResource) -> None:
        self._pet_profiles = pet_profiles

        self.create = async_to_raw_response_wrapper(
            pet_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pet_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pet_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            pet_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pet_profiles.delete,
        )
        self.ex_info = async_to_raw_response_wrapper(
            pet_profiles.ex_info,
        )
        self.variety = async_to_raw_response_wrapper(
            pet_profiles.variety,
        )


class PetProfilesResourceWithStreamingResponse:
    def __init__(self, pet_profiles: PetProfilesResource) -> None:
        self._pet_profiles = pet_profiles

        self.create = to_streamed_response_wrapper(
            pet_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pet_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pet_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            pet_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            pet_profiles.delete,
        )
        self.ex_info = to_streamed_response_wrapper(
            pet_profiles.ex_info,
        )
        self.variety = to_streamed_response_wrapper(
            pet_profiles.variety,
        )


class AsyncPetProfilesResourceWithStreamingResponse:
    def __init__(self, pet_profiles: AsyncPetProfilesResource) -> None:
        self._pet_profiles = pet_profiles

        self.create = async_to_streamed_response_wrapper(
            pet_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pet_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pet_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pet_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pet_profiles.delete,
        )
        self.ex_info = async_to_streamed_response_wrapper(
            pet_profiles.ex_info,
        )
        self.variety = async_to_streamed_response_wrapper(
            pet_profiles.variety,
        )
