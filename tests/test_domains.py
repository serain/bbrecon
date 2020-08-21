import os
from bbrecon import BugBountyRecon, models


bb = BugBountyRecon(
    token=os.environ.get("BBRECON_KEY"), base_url="https://api.bugbountyrecon.com",
)


def test_get_programs():
    domains = bb.domains(programs=["statuspage"])
    domain = next(domains)
    assert isinstance(domain, models.Domain)
