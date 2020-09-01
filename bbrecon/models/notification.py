from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Union


@dataclass
class Notification:
    resources: str
    target: Union[str, None]
    medium: str
    destination: str
    id: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "resources": self.resources,
            "target": self.target,
            "medium": self.medium,
            "destination": self.destination,
            "id": self.id,
            "createdAt": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Notification:
        return Notification(
            resources=d["resources"],
            target=d["target"],
            created_at=datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ"),
            medium=d["medium"],
            destination=d["destination"],
            id=d["id"],
        )
