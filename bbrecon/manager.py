from typing import Optional, List, Generator
from pydantic import HttpUrl

from .client import AuthenticatedClient
from .api.programs import get_programs, get_program
from .models import Program


class BugBountyRecon:
    def __init__(
        self, token: str, *, base_url: HttpUrl = "https://api.bugbountyrecon.com"
    ):
        self.client = AuthenticatedClient(base_url=base_url, token=token)

    def _paginate(self, api_function, **kwargs):
        page = 0
        while page is not None:
            targets = api_function(client=self.client, page=page, **kwargs)
            for target in targets.data:
                yield target
            page = targets.next_page

    def program(self, slug: str) -> Program:
        return get_program(client=self.client, slug=slug)

    def programs(
        self,
        *,
        name: Optional[str] = "",
        types: Optional[List[str]] = [],
        platforms: Optional[List[str]] = [],
        exclude_platforms: Optional[List[str]] = [],
        rewards: Optional[List[str]] = [],
    ) -> Generator[Program, None, None]:
        for program in self._paginate(
            get_programs,
            name=name,
            types=types,
            platforms=platforms,
            exclude_platforms=exclude_platforms,
            rewards=rewards,
        ):
            yield program
