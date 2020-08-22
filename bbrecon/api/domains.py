from typing import Any, Dict, List, Optional, Union, cast

import httpx
from datetime import datetime

from ..client import Client
from ..errors import ApiResponseError
from ..models.domains import Domains


def get_domains(
    *,
    client: Client,
    programs: Optional[List[str]] = None,
    page: Optional[int] = None,
    created_since: Optional[datetime] = None,
) -> Union[Domains]:
    url = "{}/v0b/domains".format(client.base_url)

    params: Dict[str, Any] = {}
    if programs is not None:
        params["programs"] = programs
    if page is not None:
        params["page"] = page
    if created_since is not None:
        params["createdSince"] = created_since.strftime("%Y-%m-%dT%H:%M:%SZ")

    response = httpx.get(url=url, headers=client.get_headers(), params=params)

    if response.status_code == 200:
        return Domains.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())
