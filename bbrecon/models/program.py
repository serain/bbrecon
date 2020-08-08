from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

from .program_scope import ProgramScope


@dataclass
class Program:
    url: str
    name: str
    platform: str
    rewards: List[str]
    types: List[str]
    in_scope: List[ProgramScope]
    out_scope: List[ProgramScope]
    bounty_created_at: datetime
    created_at: datetime
    updated_at: datetime
    slug: str
    live: bool
    minimum_bounty: int
    maximum_bounty: int
    average_bounty: int

    def to_dict(self) -> Dict[str, Any]:
        in_scope = []
        for in_scope_item_data in self.in_scope:
            in_scope_item = in_scope_item_data.to_dict()

            in_scope.append(in_scope_item)

        out_scope = []
        for out_scope_item_data in self.out_scope:
            out_scope_item = out_scope_item_data.to_dict()

            out_scope.append(out_scope_item)

        return {
            "url": self.url,
            "name": self.name,
            "platform": self.platform,
            "rewards": self.rewards,
            "types": self.types,
            "in_scope": in_scope,
            "out_scope": out_scope,
            "bountyCreatedAt": self.bounty_created_at.isoformat(),
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat(),
            "slug": self.slug,
            "live": self.live,
            "minimumBounty": self.minimum_bounty,
            "maximumBounty": self.maximum_bounty,
            "averageBounty": self.average_bounty,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Program:
        in_scope = []
        for in_scope_item_data in d["inScope"]:
            in_scope_item = ProgramScope.from_dict(in_scope_item_data)
            in_scope.append(in_scope_item)

        out_scope = []
        for out_scope_item_data in d["outScope"]:
            out_scope_item = ProgramScope.from_dict(out_scope_item_data)
            out_scope.append(out_scope_item)

        return Program(
            url=d["url"],
            name=d["name"],
            platform=d["platform"],
            rewards=d["rewards"],
            types=d["types"],
            in_scope=in_scope,
            out_scope=out_scope,
            bounty_created_at=datetime.strptime(
                d["bountyCreatedAt"], "%Y-%m-%dT%H:%M:%SZ"
            ),
            created_at=datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ"),
            updated_at=datetime.strptime(d["updatedAt"], "%Y-%m-%dT%H:%M:%SZ"),
            slug=d["slug"],
            live=d["live"],
            minimum_bounty=d["minimumBounty"],
            maximum_bounty=d["maximumBounty"],
            average_bounty=d["averageBounty"],
        )
