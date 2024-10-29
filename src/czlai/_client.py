# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CzlaiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Czlai",
    "AsyncCzlai",
    "Client",
    "AsyncClient",
]


class Czlai(SyncAPIClient):
    aidoc: resources.AidocResource
    aidoc_exotic: resources.AidocExoticResource
    session_records: resources.SessionRecordsResource
    medical_records: resources.MedicalRecordsResource
    ai_checkup: resources.AICheckupResource
    ai_conv: resources.AIConvResource
    users: resources.UsersResource
    upload: resources.UploadResource
    upload_image: resources.UploadImageResource
    upload_image_oss: resources.UploadImageOssResource
    pet_profiles: resources.PetProfilesResource
    ai_memes: resources.AIMemesResource
    medication_analysis: resources.MedicationAnalysisResource
    aipic: resources.AipicResource
    aipics: resources.AipicsResource
    aipic_exotics: resources.AipicExoticsResource
    ai_trials: resources.AITrialsResource
    ai_trial: resources.AITrialResource
    policies: resources.PoliciesResource
    magnum_keys: resources.MagnumKeysResource
    buriedpoints: resources.BuriedpointsResource
    whitelist: resources.WhitelistResource
    pets: resources.PetsResource
    user_module_usages: resources.UserModuleUsagesResource
    logins: resources.LoginsResource
    user_points: resources.UserPointsResource
    point_prices: resources.PointPricesResource
    point_details: resources.PointDetailsResource
    point_tasks: resources.PointTasksResource
    check_points: resources.CheckPointsResource
    user_advices: resources.UserAdvicesResource
    evaluation: resources.EvaluationResource
    with_raw_response: CzlaiWithRawResponse
    with_streaming_response: CzlaiWithStreamedResponse

    # client options
    bearer_token: str
    username: str
    password: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous czlai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `BEARER_TOKEN`
        - `username` from `BASIC_AUTH_USERNAME`
        - `password` from `BASIC_AUTH_PASSWORD`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise CzlaiError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        # FIXME: This is not used
        if username is None:
            username = os.environ.get("BASIC_AUTH_USERNAME")
            self.username = username if username else ""
        # if username is None:
        #     raise CzlaiError(
        #         "The username client option must be set either by passing username to the client or by setting the BASIC_AUTH_USERNAME environment variable"
        #     )
        # self.username = username

        if password is None:
            password = os.environ.get("BASIC_AUTH_PASSWORD")
            self.password = password if password else ""
        # if password is None:
        #     raise CzlaiError(
        #         "The password client option must be set either by passing password to the client or by setting the BASIC_AUTH_PASSWORD environment variable"
        #     )
        # self.password = password

        if base_url is None:
            base_url = os.environ.get("CZLAI_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1.0/ai-b"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.aidoc = resources.AidocResource(self)
        self.aidoc_exotic = resources.AidocExoticResource(self)
        self.session_records = resources.SessionRecordsResource(self)
        self.medical_records = resources.MedicalRecordsResource(self)
        self.ai_checkup = resources.AICheckupResource(self)
        self.ai_conv = resources.AIConvResource(self)
        self.users = resources.UsersResource(self)
        self.upload = resources.UploadResource(self)
        self.upload_image = resources.UploadImageResource(self)
        self.upload_image_oss = resources.UploadImageOssResource(self)
        self.pet_profiles = resources.PetProfilesResource(self)
        self.ai_memes = resources.AIMemesResource(self)
        self.medication_analysis = resources.MedicationAnalysisResource(self)
        self.aipic = resources.AipicResource(self)
        self.aipics = resources.AipicsResource(self)
        self.aipic_exotics = resources.AipicExoticsResource(self)
        self.ai_trials = resources.AITrialsResource(self)
        self.ai_trial = resources.AITrialResource(self)
        self.policies = resources.PoliciesResource(self)
        self.magnum_keys = resources.MagnumKeysResource(self)
        self.buriedpoints = resources.BuriedpointsResource(self)
        self.whitelist = resources.WhitelistResource(self)
        self.pets = resources.PetsResource(self)
        self.user_module_usages = resources.UserModuleUsagesResource(self)
        self.logins = resources.LoginsResource(self)
        self.user_points = resources.UserPointsResource(self)
        self.point_prices = resources.PointPricesResource(self)
        self.point_details = resources.PointDetailsResource(self)
        self.point_tasks = resources.PointTasksResource(self)
        self.check_points = resources.CheckPointsResource(self)
        self.user_advices = resources.UserAdvicesResource(self)
        self.evaluation = resources.EvaluationResource(self)
        self.with_raw_response = CzlaiWithRawResponse(self)
        self.with_streaming_response = CzlaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._jwt:
            return self._jwt
        if self._basic_auth:
            return self._basic_auth
        return {}

    @property
    def _jwt(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCzlai(AsyncAPIClient):
    aidoc: resources.AsyncAidocResource
    aidoc_exotic: resources.AsyncAidocExoticResource
    session_records: resources.AsyncSessionRecordsResource
    medical_records: resources.AsyncMedicalRecordsResource
    ai_checkup: resources.AsyncAICheckupResource
    ai_conv: resources.AsyncAIConvResource
    users: resources.AsyncUsersResource
    upload: resources.AsyncUploadResource
    upload_image: resources.AsyncUploadImageResource
    upload_image_oss: resources.AsyncUploadImageOssResource
    pet_profiles: resources.AsyncPetProfilesResource
    ai_memes: resources.AsyncAIMemesResource
    medication_analysis: resources.AsyncMedicationAnalysisResource
    aipic: resources.AsyncAipicResource
    aipics: resources.AsyncAipicsResource
    aipic_exotics: resources.AsyncAipicExoticsResource
    ai_trials: resources.AsyncAITrialsResource
    ai_trial: resources.AsyncAITrialResource
    policies: resources.AsyncPoliciesResource
    magnum_keys: resources.AsyncMagnumKeysResource
    buriedpoints: resources.AsyncBuriedpointsResource
    whitelist: resources.AsyncWhitelistResource
    pets: resources.AsyncPetsResource
    user_module_usages: resources.AsyncUserModuleUsagesResource
    logins: resources.AsyncLoginsResource
    user_points: resources.AsyncUserPointsResource
    point_prices: resources.AsyncPointPricesResource
    point_details: resources.AsyncPointDetailsResource
    point_tasks: resources.AsyncPointTasksResource
    check_points: resources.AsyncCheckPointsResource
    user_advices: resources.AsyncUserAdvicesResource
    evaluation: resources.AsyncEvaluationResource
    with_raw_response: AsyncCzlaiWithRawResponse
    with_streaming_response: AsyncCzlaiWithStreamedResponse

    # client options
    bearer_token: str
    username: str
    password: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async czlai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `BEARER_TOKEN`
        - `username` from `BASIC_AUTH_USERNAME`
        - `password` from `BASIC_AUTH_PASSWORD`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise CzlaiError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if username is None:
            username = os.environ.get("BASIC_AUTH_USERNAME")
        if username is None:
            raise CzlaiError(
                "The username client option must be set either by passing username to the client or by setting the BASIC_AUTH_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("BASIC_AUTH_PASSWORD")
        if password is None:
            raise CzlaiError(
                "The password client option must be set either by passing password to the client or by setting the BASIC_AUTH_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("CZLAI_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1.0/ai-b"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.aidoc = resources.AsyncAidocResource(self)
        self.aidoc_exotic = resources.AsyncAidocExoticResource(self)
        self.session_records = resources.AsyncSessionRecordsResource(self)
        self.medical_records = resources.AsyncMedicalRecordsResource(self)
        self.ai_checkup = resources.AsyncAICheckupResource(self)
        self.ai_conv = resources.AsyncAIConvResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.upload = resources.AsyncUploadResource(self)
        self.upload_image = resources.AsyncUploadImageResource(self)
        self.upload_image_oss = resources.AsyncUploadImageOssResource(self)
        self.pet_profiles = resources.AsyncPetProfilesResource(self)
        self.ai_memes = resources.AsyncAIMemesResource(self)
        self.medication_analysis = resources.AsyncMedicationAnalysisResource(self)
        self.aipic = resources.AsyncAipicResource(self)
        self.aipics = resources.AsyncAipicsResource(self)
        self.aipic_exotics = resources.AsyncAipicExoticsResource(self)
        self.ai_trials = resources.AsyncAITrialsResource(self)
        self.ai_trial = resources.AsyncAITrialResource(self)
        self.policies = resources.AsyncPoliciesResource(self)
        self.magnum_keys = resources.AsyncMagnumKeysResource(self)
        self.buriedpoints = resources.AsyncBuriedpointsResource(self)
        self.whitelist = resources.AsyncWhitelistResource(self)
        self.pets = resources.AsyncPetsResource(self)
        self.user_module_usages = resources.AsyncUserModuleUsagesResource(self)
        self.logins = resources.AsyncLoginsResource(self)
        self.user_points = resources.AsyncUserPointsResource(self)
        self.point_prices = resources.AsyncPointPricesResource(self)
        self.point_details = resources.AsyncPointDetailsResource(self)
        self.point_tasks = resources.AsyncPointTasksResource(self)
        self.check_points = resources.AsyncCheckPointsResource(self)
        self.user_advices = resources.AsyncUserAdvicesResource(self)
        self.evaluation = resources.AsyncEvaluationResource(self)
        self.with_raw_response = AsyncCzlaiWithRawResponse(self)
        self.with_streaming_response = AsyncCzlaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._jwt:
            return self._jwt
        if self._basic_auth:
            return self._basic_auth
        return {}

    @property
    def _jwt(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CzlaiWithRawResponse:
    def __init__(self, client: Czlai) -> None:
        self.aidoc = resources.AidocResourceWithRawResponse(client.aidoc)
        self.aidoc_exotic = resources.AidocExoticResourceWithRawResponse(client.aidoc_exotic)
        self.session_records = resources.SessionRecordsResourceWithRawResponse(client.session_records)
        self.medical_records = resources.MedicalRecordsResourceWithRawResponse(client.medical_records)
        self.ai_checkup = resources.AICheckupResourceWithRawResponse(client.ai_checkup)
        self.ai_conv = resources.AIConvResourceWithRawResponse(client.ai_conv)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.upload = resources.UploadResourceWithRawResponse(client.upload)
        self.upload_image = resources.UploadImageResourceWithRawResponse(client.upload_image)
        self.upload_image_oss = resources.UploadImageOssResourceWithRawResponse(client.upload_image_oss)
        self.pet_profiles = resources.PetProfilesResourceWithRawResponse(client.pet_profiles)
        self.ai_memes = resources.AIMemesResourceWithRawResponse(client.ai_memes)
        self.medication_analysis = resources.MedicationAnalysisResourceWithRawResponse(client.medication_analysis)
        self.aipic = resources.AipicResourceWithRawResponse(client.aipic)
        self.aipics = resources.AipicsResourceWithRawResponse(client.aipics)
        self.aipic_exotics = resources.AipicExoticsResourceWithRawResponse(client.aipic_exotics)
        self.ai_trials = resources.AITrialsResourceWithRawResponse(client.ai_trials)
        self.ai_trial = resources.AITrialResourceWithRawResponse(client.ai_trial)
        self.policies = resources.PoliciesResourceWithRawResponse(client.policies)
        self.magnum_keys = resources.MagnumKeysResourceWithRawResponse(client.magnum_keys)
        self.buriedpoints = resources.BuriedpointsResourceWithRawResponse(client.buriedpoints)
        self.whitelist = resources.WhitelistResourceWithRawResponse(client.whitelist)
        self.pets = resources.PetsResourceWithRawResponse(client.pets)
        self.user_module_usages = resources.UserModuleUsagesResourceWithRawResponse(client.user_module_usages)
        self.logins = resources.LoginsResourceWithRawResponse(client.logins)
        self.user_points = resources.UserPointsResourceWithRawResponse(client.user_points)
        self.point_prices = resources.PointPricesResourceWithRawResponse(client.point_prices)
        self.point_details = resources.PointDetailsResourceWithRawResponse(client.point_details)
        self.point_tasks = resources.PointTasksResourceWithRawResponse(client.point_tasks)
        self.check_points = resources.CheckPointsResourceWithRawResponse(client.check_points)
        self.user_advices = resources.UserAdvicesResourceWithRawResponse(client.user_advices)
        self.evaluation = resources.EvaluationResourceWithRawResponse(client.evaluation)


class AsyncCzlaiWithRawResponse:
    def __init__(self, client: AsyncCzlai) -> None:
        self.aidoc = resources.AsyncAidocResourceWithRawResponse(client.aidoc)
        self.aidoc_exotic = resources.AsyncAidocExoticResourceWithRawResponse(client.aidoc_exotic)
        self.session_records = resources.AsyncSessionRecordsResourceWithRawResponse(client.session_records)
        self.medical_records = resources.AsyncMedicalRecordsResourceWithRawResponse(client.medical_records)
        self.ai_checkup = resources.AsyncAICheckupResourceWithRawResponse(client.ai_checkup)
        self.ai_conv = resources.AsyncAIConvResourceWithRawResponse(client.ai_conv)
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.upload = resources.AsyncUploadResourceWithRawResponse(client.upload)
        self.upload_image = resources.AsyncUploadImageResourceWithRawResponse(client.upload_image)
        self.upload_image_oss = resources.AsyncUploadImageOssResourceWithRawResponse(client.upload_image_oss)
        self.pet_profiles = resources.AsyncPetProfilesResourceWithRawResponse(client.pet_profiles)
        self.ai_memes = resources.AsyncAIMemesResourceWithRawResponse(client.ai_memes)
        self.medication_analysis = resources.AsyncMedicationAnalysisResourceWithRawResponse(client.medication_analysis)
        self.aipic = resources.AsyncAipicResourceWithRawResponse(client.aipic)
        self.aipics = resources.AsyncAipicsResourceWithRawResponse(client.aipics)
        self.aipic_exotics = resources.AsyncAipicExoticsResourceWithRawResponse(client.aipic_exotics)
        self.ai_trials = resources.AsyncAITrialsResourceWithRawResponse(client.ai_trials)
        self.ai_trial = resources.AsyncAITrialResourceWithRawResponse(client.ai_trial)
        self.policies = resources.AsyncPoliciesResourceWithRawResponse(client.policies)
        self.magnum_keys = resources.AsyncMagnumKeysResourceWithRawResponse(client.magnum_keys)
        self.buriedpoints = resources.AsyncBuriedpointsResourceWithRawResponse(client.buriedpoints)
        self.whitelist = resources.AsyncWhitelistResourceWithRawResponse(client.whitelist)
        self.pets = resources.AsyncPetsResourceWithRawResponse(client.pets)
        self.user_module_usages = resources.AsyncUserModuleUsagesResourceWithRawResponse(client.user_module_usages)
        self.logins = resources.AsyncLoginsResourceWithRawResponse(client.logins)
        self.user_points = resources.AsyncUserPointsResourceWithRawResponse(client.user_points)
        self.point_prices = resources.AsyncPointPricesResourceWithRawResponse(client.point_prices)
        self.point_details = resources.AsyncPointDetailsResourceWithRawResponse(client.point_details)
        self.point_tasks = resources.AsyncPointTasksResourceWithRawResponse(client.point_tasks)
        self.check_points = resources.AsyncCheckPointsResourceWithRawResponse(client.check_points)
        self.user_advices = resources.AsyncUserAdvicesResourceWithRawResponse(client.user_advices)
        self.evaluation = resources.AsyncEvaluationResourceWithRawResponse(client.evaluation)


class CzlaiWithStreamedResponse:
    def __init__(self, client: Czlai) -> None:
        self.aidoc = resources.AidocResourceWithStreamingResponse(client.aidoc)
        self.aidoc_exotic = resources.AidocExoticResourceWithStreamingResponse(client.aidoc_exotic)
        self.session_records = resources.SessionRecordsResourceWithStreamingResponse(client.session_records)
        self.medical_records = resources.MedicalRecordsResourceWithStreamingResponse(client.medical_records)
        self.ai_checkup = resources.AICheckupResourceWithStreamingResponse(client.ai_checkup)
        self.ai_conv = resources.AIConvResourceWithStreamingResponse(client.ai_conv)
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.upload = resources.UploadResourceWithStreamingResponse(client.upload)
        self.upload_image = resources.UploadImageResourceWithStreamingResponse(client.upload_image)
        self.upload_image_oss = resources.UploadImageOssResourceWithStreamingResponse(client.upload_image_oss)
        self.pet_profiles = resources.PetProfilesResourceWithStreamingResponse(client.pet_profiles)
        self.ai_memes = resources.AIMemesResourceWithStreamingResponse(client.ai_memes)
        self.medication_analysis = resources.MedicationAnalysisResourceWithStreamingResponse(client.medication_analysis)
        self.aipic = resources.AipicResourceWithStreamingResponse(client.aipic)
        self.aipics = resources.AipicsResourceWithStreamingResponse(client.aipics)
        self.aipic_exotics = resources.AipicExoticsResourceWithStreamingResponse(client.aipic_exotics)
        self.ai_trials = resources.AITrialsResourceWithStreamingResponse(client.ai_trials)
        self.ai_trial = resources.AITrialResourceWithStreamingResponse(client.ai_trial)
        self.policies = resources.PoliciesResourceWithStreamingResponse(client.policies)
        self.magnum_keys = resources.MagnumKeysResourceWithStreamingResponse(client.magnum_keys)
        self.buriedpoints = resources.BuriedpointsResourceWithStreamingResponse(client.buriedpoints)
        self.whitelist = resources.WhitelistResourceWithStreamingResponse(client.whitelist)
        self.pets = resources.PetsResourceWithStreamingResponse(client.pets)
        self.user_module_usages = resources.UserModuleUsagesResourceWithStreamingResponse(client.user_module_usages)
        self.logins = resources.LoginsResourceWithStreamingResponse(client.logins)
        self.user_points = resources.UserPointsResourceWithStreamingResponse(client.user_points)
        self.point_prices = resources.PointPricesResourceWithStreamingResponse(client.point_prices)
        self.point_details = resources.PointDetailsResourceWithStreamingResponse(client.point_details)
        self.point_tasks = resources.PointTasksResourceWithStreamingResponse(client.point_tasks)
        self.check_points = resources.CheckPointsResourceWithStreamingResponse(client.check_points)
        self.user_advices = resources.UserAdvicesResourceWithStreamingResponse(client.user_advices)
        self.evaluation = resources.EvaluationResourceWithStreamingResponse(client.evaluation)


class AsyncCzlaiWithStreamedResponse:
    def __init__(self, client: AsyncCzlai) -> None:
        self.aidoc = resources.AsyncAidocResourceWithStreamingResponse(client.aidoc)
        self.aidoc_exotic = resources.AsyncAidocExoticResourceWithStreamingResponse(client.aidoc_exotic)
        self.session_records = resources.AsyncSessionRecordsResourceWithStreamingResponse(client.session_records)
        self.medical_records = resources.AsyncMedicalRecordsResourceWithStreamingResponse(client.medical_records)
        self.ai_checkup = resources.AsyncAICheckupResourceWithStreamingResponse(client.ai_checkup)
        self.ai_conv = resources.AsyncAIConvResourceWithStreamingResponse(client.ai_conv)
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.upload = resources.AsyncUploadResourceWithStreamingResponse(client.upload)
        self.upload_image = resources.AsyncUploadImageResourceWithStreamingResponse(client.upload_image)
        self.upload_image_oss = resources.AsyncUploadImageOssResourceWithStreamingResponse(client.upload_image_oss)
        self.pet_profiles = resources.AsyncPetProfilesResourceWithStreamingResponse(client.pet_profiles)
        self.ai_memes = resources.AsyncAIMemesResourceWithStreamingResponse(client.ai_memes)
        self.medication_analysis = resources.AsyncMedicationAnalysisResourceWithStreamingResponse(
            client.medication_analysis
        )
        self.aipic = resources.AsyncAipicResourceWithStreamingResponse(client.aipic)
        self.aipics = resources.AsyncAipicsResourceWithStreamingResponse(client.aipics)
        self.aipic_exotics = resources.AsyncAipicExoticsResourceWithStreamingResponse(client.aipic_exotics)
        self.ai_trials = resources.AsyncAITrialsResourceWithStreamingResponse(client.ai_trials)
        self.ai_trial = resources.AsyncAITrialResourceWithStreamingResponse(client.ai_trial)
        self.policies = resources.AsyncPoliciesResourceWithStreamingResponse(client.policies)
        self.magnum_keys = resources.AsyncMagnumKeysResourceWithStreamingResponse(client.magnum_keys)
        self.buriedpoints = resources.AsyncBuriedpointsResourceWithStreamingResponse(client.buriedpoints)
        self.whitelist = resources.AsyncWhitelistResourceWithStreamingResponse(client.whitelist)
        self.pets = resources.AsyncPetsResourceWithStreamingResponse(client.pets)
        self.user_module_usages = resources.AsyncUserModuleUsagesResourceWithStreamingResponse(
            client.user_module_usages
        )
        self.logins = resources.AsyncLoginsResourceWithStreamingResponse(client.logins)
        self.user_points = resources.AsyncUserPointsResourceWithStreamingResponse(client.user_points)
        self.point_prices = resources.AsyncPointPricesResourceWithStreamingResponse(client.point_prices)
        self.point_details = resources.AsyncPointDetailsResourceWithStreamingResponse(client.point_details)
        self.point_tasks = resources.AsyncPointTasksResourceWithStreamingResponse(client.point_tasks)
        self.check_points = resources.AsyncCheckPointsResourceWithStreamingResponse(client.check_points)
        self.user_advices = resources.AsyncUserAdvicesResourceWithStreamingResponse(client.user_advices)
        self.evaluation = resources.AsyncEvaluationResourceWithStreamingResponse(client.evaluation)


Client = Czlai

AsyncClient = AsyncCzlai
