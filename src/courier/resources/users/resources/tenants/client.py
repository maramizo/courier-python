# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .types.add_user_to_single_tenants_params_profile import AddUserToSingleTenantsParamsProfile
from .types.list_tenants_for_user_response import ListTenantsForUserResponse
from .types.user_tenant_association import UserTenantAssociation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_multple(self, user_id: str, *, tenants: typing.List[UserTenantAssociation]) -> None:
        """
        This endpoint is used to add a user to
        multiple tenants in one call.
        A custom profile can also be supplied for each tenant.
        This profile will be merged with the user's main
        profile when sending to the user with that tenant.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - tenants: typing.List[UserTenantAssociation].
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants"),
            json=jsonable_encoder({"tenants": tenants}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add(self, user_id: str, tenant_id: str, *, profile: AddUserToSingleTenantsParamsProfile) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters:
            - user_id: str. Id of the user to be added to the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be added to.

            - profile: AddUserToSingleTenantsParamsProfile.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants/{tenant_id}"),
            json=jsonable_encoder({"profile": profile}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(self, user_id: str, tenant_id: str) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be removed from.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants/{tenant_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self, user_id: str, *, limit: typing.Optional[int] = None, starting_after: typing.Optional[int] = None
    ) -> ListTenantsForUserResponse:
        """
        Returns a paginated list of user tenant associations.

        Parameters:
            - user_id: str. Id of the user to retrieve all associated tenants for.

            - limit: typing.Optional[int]. The number of accounts to return
                                           (defaults to 20, maximum value of 100)
            - starting_after: typing.Optional[int]. Value of next_page from previous response
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants"),
            params=remove_none_from_dict({"limit": limit, "starting_after": starting_after}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListTenantsForUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_multple(self, user_id: str, *, tenants: typing.List[UserTenantAssociation]) -> None:
        """
        This endpoint is used to add a user to
        multiple tenants in one call.
        A custom profile can also be supplied for each tenant.
        This profile will be merged with the user's main
        profile when sending to the user with that tenant.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - tenants: typing.List[UserTenantAssociation].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants"),
            json=jsonable_encoder({"tenants": tenants}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add(self, user_id: str, tenant_id: str, *, profile: AddUserToSingleTenantsParamsProfile) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters:
            - user_id: str. Id of the user to be added to the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be added to.

            - profile: AddUserToSingleTenantsParamsProfile.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants/{tenant_id}"),
            json=jsonable_encoder({"profile": profile}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(self, user_id: str, tenant_id: str) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be removed from.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants/{tenant_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self, user_id: str, *, limit: typing.Optional[int] = None, starting_after: typing.Optional[int] = None
    ) -> ListTenantsForUserResponse:
        """
        Returns a paginated list of user tenant associations.

        Parameters:
            - user_id: str. Id of the user to retrieve all associated tenants for.

            - limit: typing.Optional[int]. The number of accounts to return
                                           (defaults to 20, maximum value of 100)
            - starting_after: typing.Optional[int]. Value of next_page from previous response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}/tenants"),
            params=remove_none_from_dict({"limit": limit, "starting_after": starting_after}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListTenantsForUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
