from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .notification import Notification


@dataclass
class Notifications:
    data: List[Notification]
    next_page: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)
        next_page = self.next_page

        return {"data": data, "nextPage": next_page}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Notifications:
        data = []
        for data_item_data in d["data"]:
            data_item = Notification.from_dict(data_item_data)
            data.append(data_item)
        next_page = d.get("nextPage")

        return Notifications(data=data, next_page=next_page)
