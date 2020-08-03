import json
import typer
import urllib.request
from distutils.version import LooseVersion
from pkg_resources import get_distribution


def check():
    name = "bbrecon"
    installed_version = get_distribution("bbrecon").version

    pypi_url = f"https://pypi.org/pypi/{name}/json"
    response = urllib.request.urlopen(pypi_url).read().decode()
    latest_version = max(
        LooseVersion(s) for s in json.loads(response)["releases"].keys()
    )

    if installed_version < latest_version:
        typer.secho(
            f"""You are running an old version of bbrecon and things may not work.
Upgrade with `pip3 install bbrecon=={latest_version}`
""",
            fg=typer.colors.YELLOW,
            err=True,
        )
