from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

from .program_scope import ProgramScope


@dataclass
class Program:
    """  """

    program_url: str
    program_name: str
    platform: str
    rewards: List[str]
    types: List[str]
    in_scope: List[ProgramScope]
    out_scope: List[ProgramScope]
    bounty_created_at: datetime
    created_at: datetime
    updated_at: datetime
    slug: str

    def to_dict(self) -> Dict[str, Any]:
        program_url = self.program_url
        program_name = self.program_name
        platform = self.platform
        rewards = self.rewards

        types = self.types

        in_scope = []
        for in_scope_item_data in self.in_scope:
            in_scope_item = in_scope_item_data.to_dict()

            in_scope.append(in_scope_item)

        out_scope = []
        for out_scope_item_data in self.out_scope:
            out_scope_item = out_scope_item_data.to_dict()

            out_scope.append(out_scope_item)

        bounty_created_at = self.bounty_created_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        slug = self.slug

        return {
            "programUrl": program_url,
            "programName": program_name,
            "platform": platform,
            "rewards": rewards,
            "types": types,
            "in_scope": in_scope,
            "out_scope": out_scope,
            "bountyCreatedAt": bounty_created_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "slug": slug,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Program:
        program_url = d["programUrl"]

        program_name = d["programName"]

        platform = d["platform"]

        rewards = d["rewards"]

        types = d["types"]

        in_scope = []
        for in_scope_item_data in d["in_scope"]:
            in_scope_item = ProgramScope.from_dict(in_scope_item_data)

            in_scope.append(in_scope_item)

        out_scope = []
        for out_scope_item_data in d["out_scope"]:
            out_scope_item = ProgramScope.from_dict(out_scope_item_data)

            out_scope.append(out_scope_item)

        bounty_created_at = datetime.strptime(
            d["bountyCreatedAt"], "%Y-%m-%dT%H:%M:%SZ"
        )

        created_at = datetime.strptime(d["createdAt"], "%Y-%m-%dT%H:%M:%SZ")

        updated_at = datetime.strptime(d["updatedAt"], "%Y-%m-%dT%H:%M:%SZ")

        slug = d["slug"]

        return Program(
            program_url=program_url,
            program_name=program_name,
            platform=platform,
            rewards=rewards,
            types=types,
            in_scope=in_scope,
            out_scope=out_scope,
            bounty_created_at=bounty_created_at,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
        )
