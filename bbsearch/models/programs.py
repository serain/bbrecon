from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .program import Program


@dataclass
class Programs:
    """  """

    data: List[Program]
    next_page: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        next_page = self.next_page

        return {
            "data": data,
            "nextPage": next_page,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Programs:
        data = []
        for data_item_data in d["data"]:
            data_item = Program.from_dict(data_item_data)

            data.append(data_item)

        next_page = d.get("nextPage")

        return Programs(data=data, next_page=next_page,)
