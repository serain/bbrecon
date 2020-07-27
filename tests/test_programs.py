import os
import validators
from bbsearch import BugBountySearch, models


bb = BugBountySearch(os.environ.get("BBSEARCH_API_KEY"))


def test_get_programs():
    programs = bb.programs()
    program = next(programs)
    assert isinstance(program, models.Program)
    assert validators.url(program.program_url)
