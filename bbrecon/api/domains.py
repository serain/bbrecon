from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.domains import Domains
from ..models.domain import Domain


def get_domains(
    *, client: Client, programs: Optional[List[str]] = None,
) -> Union[Domains]:
    url = "{}/v0b/programs".format(client.base_url)

    params: Dict[str, Any] = {}
    if programs is not None:
        params["programs"] = programs

    response = httpx.get(url=url, headers=client.get_headers(), params=params)

    if response.status_code == 200:
        return Domains.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())


def get_program(*, client: Client, slug: str) -> Union[Domain]:
    url = "{}/v0b/programs/{slug}".format(client.base_url, slug=slug)
    response = httpx.get(url=url, headers=client.get_headers())

    if response.status_code == 200:
        return Domain.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())
