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
from ...types.users import contact_create_params
from ..._base_client import make_request_options

__all__ = ["ContactResource", "AsyncContactResource"]


class ContactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return ContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return ContactResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_name: str | NotGiven = NOT_GIVEN,
        contact_name: str | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        合作交流信息保存

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/contact",
            body=maybe_transform(
                {
                    "company_name": company_name,
                    "contact_name": contact_name,
                    "mobile": mobile,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncContactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncContactResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_name: str | NotGiven = NOT_GIVEN,
        contact_name: str | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        合作交流信息保存

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/contact",
            body=await async_maybe_transform(
                {
                    "company_name": company_name,
                    "contact_name": contact_name,
                    "mobile": mobile,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ContactResourceWithRawResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_raw_response_wrapper(
            contact.create,
        )


class AsyncContactResourceWithRawResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_raw_response_wrapper(
            contact.create,
        )


class ContactResourceWithStreamingResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_streamed_response_wrapper(
            contact.create,
        )


class AsyncContactResourceWithStreamingResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_streamed_response_wrapper(
            contact.create,
        )
