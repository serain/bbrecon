import os
from bbrecon import BugBountyRecon, models


bb = BugBountyRecon(
    token=os.environ.get("BBRECON_KEY"), base_url="https://api.bugbountyrecon.com",
)


def test_get_alerts():
    alerts = bb.alerts()
    alert = next(alerts)
    assert isinstance(alert, models.Alert)
