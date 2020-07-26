from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.http_validation_error import HTTPValidationError
from ..models.programs import Programs
from ..models.program import Program


def get_programs(
    *,
    client: Client,
    name: Optional[str] = "",
    types: Optional[List[str]] = [],
    platforms: Optional[List[str]] = [],
    exclude_platforms: Optional[List[str]] = [],
    rewards: Optional[List[str]] = [],
    page: Optional[int] = 0,
) -> Union[
    Programs, HTTPValidationError,
]:

    """ Retrieve a list of indexed bug bounty programs, using filters to
narrow your search if needed.

Returns up to 50 programs per page.
 """
    url = "{}/v0b/programs".format(client.base_url)

    if types is None:
        json_types = None
    else:
        json_types = types

    if platforms is None:
        json_platforms = None
    else:
        json_platforms = platforms

    if exclude_platforms is None:
        json_exclude_platforms = None
    else:
        json_exclude_platforms = exclude_platforms

    if rewards is None:
        json_rewards = None
    else:
        json_rewards = rewards

    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if types is not None:
        params["types"] = json_types
    if platforms is not None:
        params["platforms"] = json_platforms
    if exclude_platforms is not None:
        params["excludePlatforms"] = json_exclude_platforms
    if rewards is not None:
        params["rewards"] = json_rewards
    if page is not None:
        params["page"] = page

    response = httpx.get(url=url, headers=client.get_headers(), params=params,)

    if response.status_code == 200:
        return Programs.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 422:
        return HTTPValidationError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


def get_program(
    *, client: Client, slug: str,
) -> Union[
    Program, HTTPValidationError,
]:

    """ Retrieve a specific bug bounty program by its `slug`. """
    url = "{}/v0b/programs/{slug}".format(client.base_url, slug=slug)

    response = httpx.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return Program.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 422:
        return HTTPValidationError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)
