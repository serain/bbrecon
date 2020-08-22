from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass
class Domain:
    domain: str
    program: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "program": self.program,
            "createdAt": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Domain:
        return Domain(
            domain=d["domain"],
            program=d["program"],
            created_at=datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ"),
        )
