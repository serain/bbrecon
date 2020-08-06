from typing import Any, Dict, List, Optional, Union, cast
from datetime import datetime

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.programs import Programs
from ..models.program import Program


def get_programs(
    *,
    client: Client,
    name: Optional[str] = None,
    types: Optional[List[str]] = None,
    platforms: Optional[List[str]] = None,
    exclude_platforms: Optional[List[str]] = None,
    rewards: Optional[List[str]] = None,
    page: Optional[int] = None,
    created_since: Optional[datetime] = None,
) -> Union[Programs]:
    url = "{}/v0b/programs/public".format(client.base_url)

    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if types is not None:
        params["types"] = types
    if platforms is not None:
        params["platforms"] = platforms
    if exclude_platforms is not None:
        params["excludePlatforms"] = exclude_platforms
    if rewards is not None:
        params["rewards"] = rewards
    if page is not None:
        params["page"] = page
    if created_since is not None:
        params["createdSince"] = created_since.strftime("%Y-%m-%dT%H:%M:%SZ")

    response = httpx.get(url=url, headers=client.get_headers(), params=params)

    if response.status_code == 200:
        return Programs.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())


def get_program(*, client: Client, slug: str) -> Union[Program]:
    url = "{}/v0b/programs/public/{slug}".format(client.base_url, slug=slug)
    response = httpx.get(url=url, headers=client.get_headers())

    if response.status_code == 200:
        return Program.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())
