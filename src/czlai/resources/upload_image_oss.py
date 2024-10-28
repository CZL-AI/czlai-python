# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import upload_image_oss_create_params
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

__all__ = ["UploadImageOssResource", "AsyncUploadImageOssResource"]


class UploadImageOssResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadImageOssResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return UploadImageOssResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadImageOssResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return UploadImageOssResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        upload_type: Literal[1, 2, 3, 4],
        image: FileTypes,
        upload_to_local: int | NotGiven = NOT_GIVEN,
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
          upload_type: 图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他

          image: 要上传的图片文件

          upload_to_local: 是否上传到本地服务器

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
            "/upload-image-oss",
            body=maybe_transform(body, upload_image_oss_create_params.UploadImageOssCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "upload_type": upload_type,
                        "upload_to_local": upload_to_local,
                    },
                    upload_image_oss_create_params.UploadImageOssCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncUploadImageOssResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadImageOssResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadImageOssResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadImageOssResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncUploadImageOssResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        upload_type: Literal[1, 2, 3, 4],
        image: FileTypes,
        upload_to_local: int | NotGiven = NOT_GIVEN,
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
          upload_type: 图片上传类型 1-头像 2-图片识别模块 3-表情包 4-其他

          image: 要上传的图片文件

          upload_to_local: 是否上传到本地服务器

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
            "/upload-image-oss",
            body=await async_maybe_transform(body, upload_image_oss_create_params.UploadImageOssCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "upload_type": upload_type,
                        "upload_to_local": upload_to_local,
                    },
                    upload_image_oss_create_params.UploadImageOssCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class UploadImageOssResourceWithRawResponse:
    def __init__(self, upload_image_oss: UploadImageOssResource) -> None:
        self._upload_image_oss = upload_image_oss

        self.create = to_raw_response_wrapper(
            upload_image_oss.create,
        )


class AsyncUploadImageOssResourceWithRawResponse:
    def __init__(self, upload_image_oss: AsyncUploadImageOssResource) -> None:
        self._upload_image_oss = upload_image_oss

        self.create = async_to_raw_response_wrapper(
            upload_image_oss.create,
        )


class UploadImageOssResourceWithStreamingResponse:
    def __init__(self, upload_image_oss: UploadImageOssResource) -> None:
        self._upload_image_oss = upload_image_oss

        self.create = to_streamed_response_wrapper(
            upload_image_oss.create,
        )


class AsyncUploadImageOssResourceWithStreamingResponse:
    def __init__(self, upload_image_oss: AsyncUploadImageOssResource) -> None:
        self._upload_image_oss = upload_image_oss

        self.create = async_to_streamed_response_wrapper(
            upload_image_oss.create,
        )
