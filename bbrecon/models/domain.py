from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass
class Domain:
    name: str
    program: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "program": self.program,
            "createdAt": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Domain:
        return Domain(
            name=d["name"],
            program=d["program"],
            created_at=datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ"),
        )
