from typing import Optional, List, Generator
from pydantic import HttpUrl
from datetime import datetime

from .client import AuthenticatedClient
from .api.programs import get_programs, get_program
from .api.domains import get_domains
from .models import Program, Domain


class BugBountyRecon:
    def __init__(
        self, token: str, *, base_url: HttpUrl = "https://api.bugbountyrecon.com"
    ):
        self.client = AuthenticatedClient(base_url=base_url, token=token)

    def _paginate(self, api_function, **kwargs):
        page = 0
        while page is not None:
            response = api_function(client=self.client, page=page, **kwargs)
            for target in response.data:
                yield target
            page = response.next_page

    def program(self, slug: str) -> Program:
        return get_program(client=self.client, slug=slug)

    def programs(
        self,
        *,
        name: Optional[str] = None,
        types: Optional[List[str]] = None,
        platforms: Optional[List[str]] = None,
        exclude_platforms: Optional[List[str]] = None,
        rewards: Optional[List[str]] = None,
        created_since: Optional[datetime] = None,
    ) -> Generator[Program, None, None]:
        for program in self._paginate(
            get_programs,
            name=name,
            types=types,
            platforms=platforms,
            exclude_platforms=exclude_platforms,
            rewards=rewards,
            created_since=created_since,
        ):
            yield program

    def domains(
        self,
        *,
        programs: Optional[List[str]] = None,
        created_since: Optional[datetime] = None,
    ) -> Generator[Domain, None, None]:
        for domain in self._paginate(
            get_domains, programs=programs, created_since=created_since
        ):
            yield domain
