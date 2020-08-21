from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .domain import Domain


@dataclass
class Domains:
    data: List[Domain]
    next_page: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)
        next_page = self.next_page

        return {"data": data, "nextPage": next_page}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Domains:
        data = []
        for data_item_data in d["data"]:
            data_item = Domain.from_dict(data_item_data)
            data.append(data_item)
        next_page = d.get("nextPage")

        return Domains(data=data, next_page=next_page)
