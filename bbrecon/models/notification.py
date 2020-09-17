from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Union


@dataclass
class Notification:
    resources: str
    program: Union[str, None]
    webhook: str
    id: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "resources": self.resources,
            "program": self.program,
            "webhook": self.webhook,
            "id": self.id,
            "createdAt": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Notification:
        return Notification(
            resources=d["resources"],
            program=d["program"],
            created_at=datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ"),
            webhook=d["webhook"],
            id=d["id"],
        )
