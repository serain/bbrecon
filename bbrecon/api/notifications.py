from typing import Any, Dict, Optional, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.notifications import Notifications
from ..models.notification import Notification


def get_notifications(
    *, client: Client, page: Optional[int] = None,
) -> Union[Notifications]:
    url = "{}/v0b/notifications".format(client.base_url)

    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page

    response = httpx.get(url=url, headers=client.get_headers(), params=params)
    if response.status_code == 200:
        return Notifications.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())


def get_notification(*, client: Client, id: str) -> Union[Notification]:
    url = "{}/v0b/notifications/{id}".format(client.base_url, id=id)
    response = httpx.get(url=url, headers=client.get_headers())

    if response.status_code == 200:
        return Notification.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())


def delete_notification(*, client: Client, id: str) -> bool:
    url = "{}/v0b/notifications/{id}".format(client.base_url, id=id)
    response = httpx.delete(url=url, headers=client.get_headers())

    if response.status_code == 204:
        return True
    raise ApiResponseError(code=response.status_code, detail=response.json())


def create_notification(
    *, client: Client, resources: str, target: str, medium: str, destination: str
) -> Notification:
    url = "{}/v0b/notifications".format(client.base_url)
    response = httpx.post(
        url=url,
        headers=client.get_headers(),
        json={
            "resources": resources,
            "target": target,
            "medium": medium,
            "destination": destination,
        },
    )
    print(url)

    if response.status_code == 201:
        return Notification.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())
