from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Domain:
    domain: str
    program: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "program": self.program,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Domain:
        return Domain(domain=d["domain"], program=d["program"],)
