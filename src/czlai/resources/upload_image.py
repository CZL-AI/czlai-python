# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import upload_image_create_params
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

__all__ = ["UploadImageResource", "AsyncUploadImageResource"]


class UploadImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UploadImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UploadImageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image: FileTypes,
        is_to_cloud: int | NotGiven = NOT_GIVEN,
        upload_type: Literal[1, 2, 3, 4] | NotGiven = NOT_GIVEN,
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

          upload_type: 图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他

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
            "/upload-image",
            body=maybe_transform(body, upload_image_create_params.UploadImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_to_cloud": is_to_cloud,
                        "upload_type": upload_type,
                    },
                    upload_image_create_params.UploadImageCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncUploadImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUploadImageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image: FileTypes,
        is_to_cloud: int | NotGiven = NOT_GIVEN,
        upload_type: Literal[1, 2, 3, 4] | NotGiven = NOT_GIVEN,
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

          upload_type: 图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他

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
            "/upload-image",
            body=await async_maybe_transform(body, upload_image_create_params.UploadImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_to_cloud": is_to_cloud,
                        "upload_type": upload_type,
                    },
                    upload_image_create_params.UploadImageCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class UploadImageResourceWithRawResponse:
    def __init__(self, upload_image: UploadImageResource) -> None:
        self._upload_image = upload_image

        self.create = to_raw_response_wrapper(
            upload_image.create,
        )


class AsyncUploadImageResourceWithRawResponse:
    def __init__(self, upload_image: AsyncUploadImageResource) -> None:
        self._upload_image = upload_image

        self.create = async_to_raw_response_wrapper(
            upload_image.create,
        )


class UploadImageResourceWithStreamingResponse:
    def __init__(self, upload_image: UploadImageResource) -> None:
        self._upload_image = upload_image

        self.create = to_streamed_response_wrapper(
            upload_image.create,
        )


class AsyncUploadImageResourceWithStreamingResponse:
    def __init__(self, upload_image: AsyncUploadImageResource) -> None:
        self._upload_image = upload_image

        self.create = async_to_streamed_response_wrapper(
            upload_image.create,
        )
