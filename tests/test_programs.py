import os
import validators
from bbsearch import BugBountySearch, models


bb = BugBountySearch(os.environ.get("BBSEARCH_API_KEY"))


def test_get_program():
    program = bb.get_program("gate-io-exchange")
    assert isinstance(program, models.Program)
    assert validators.url(program.program_url)
    assert program.platform == "hackenproof"
    assert "web" in program.types
    assert len(program.in_scope) > 0


def test_get_programs():
    programs = bb.get_programs()
    program = next(programs)
    assert isinstance(program, models.Program)
