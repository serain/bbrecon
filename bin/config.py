import os
import typer
from pathlib import Path, PurePath


if (API_TOKEN := os.environ.get("BBRECON_KEY")) is None:
    try:
        with open(PurePath.joinpath(Path.home(), ".bbrecon/token")) as f:
            API_TOKEN = f.read().strip()
    except FileNotFoundError:
        typer.secho(
            "No BBRECON_KEY in environment, and no key configured in your home path.",
            fg=typer.colors.YELLOW,
        )


if (BASE_URL := os.environ.get("BBRECON_URL")) is None:
    BASE_URL = "https://api.bugbountyrecon.com/"
