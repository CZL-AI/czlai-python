# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import upload_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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

__all__ = ["UploadResource", "AsyncUploadResource"]


class UploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UploadResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image: FileTypes,
        is_to_cloud: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        允许用户上传一张图片

        Args:
          image: 要上传的图片文件

          is_to_cloud: 是否上传到图床

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"image": image})
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/upload",
            body=maybe_transform(body, upload_create_params.UploadCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"is_to_cloud": is_to_cloud}, upload_create_params.UploadCreateParams),
            ),
            cast_to=NoneType,
        )


class AsyncUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUploadResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image: FileTypes,
        is_to_cloud: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        允许用户上传一张图片

        Args:
          image: 要上传的图片文件

          is_to_cloud: 是否上传到图床

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"image": image})
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/upload",
            body=await async_maybe_transform(body, upload_create_params.UploadCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"is_to_cloud": is_to_cloud}, upload_create_params.UploadCreateParams
                ),
            ),
            cast_to=NoneType,
        )


class UploadResourceWithRawResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_raw_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithRawResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_raw_response_wrapper(
            upload.create,
        )


class UploadResourceWithStreamingResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_streamed_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithStreamingResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_streamed_response_wrapper(
            upload.create,
        )
