import os
import validators
from bbrecon import BugBountyRecon, models


bb = BugBountyRecon(
    token=os.environ.get("BBRECON_KEY"), base_url="https://api.bugbountyrecon.com",
)


def test_get_programs():
    programs = bb.programs()
    program = next(programs)
    assert isinstance(program, models.Program)
    assert validators.url(program.url)
