from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ProgramScope:
    """  """

    type: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        value = self.value

        return {
            "type": type,
            "value": value,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> ProgramScope:
        type = d["type"]

        value = d["value"]

        return ProgramScope(type=type, value=value,)
