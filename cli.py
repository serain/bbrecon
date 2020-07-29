import os
import re
import json
import typer
from enum import Enum
from tabulate import tabulate
from click_spinner import spinner
from typing import List, Optional
from datetime import datetime, timedelta

from bbrecon import BugBountyRecon, Program


if (API_KEY := os.environ.get("BBRECON_KEY")) is None:
    print("No BBRECON_KEY in environment, see '--help'.")
    exit(1)

if (BASE_URL := os.environ.get("BBRECON_URL")) is None:
    BASE_URL = "https://api.bugbountyrecon.com/"


bb = BugBountyRecon(token=API_KEY, base_url=BASE_URL)

app = typer.Typer(
    help="""bbrecon

CLI for the Bug Bounty Recon API.

Requires a Bug Bounty Recon API key set in the 'BBRECON_KEY' environment variable.
Head over to https://bugbountyrecon.com to fetch a key.

Please use https://github.com/bugbountyrecon/bbrecon to report issues.
"""
)
get = typer.Typer(help="Fetch resources.")
app.add_typer(get, name="get")


class InvalidDateInputError(Exception):
    pass


class OutputFormat(str, Enum):
    narrow = "narrow"
    wide = "wide"
    json_ = "json"


def get_datetime_from_input(date_input: str) -> datetime:
    if date_input == "yesterday":
        days = 1
    elif date_input == "last-week":
        days = 7
    elif date_input == "last-month":
        days = 31
    elif date_input == "last-year":
        days = 365
    elif matches := re.match(r"last-(\d+)-days", date_input):
        days = matches[1]
    return datetime.today() - timedelta(days=days)


def output_json_programs_table(programs: List[Program]):
    typer.echo(json.dumps([program.to_dict() for program in programs], indent=4))


def output_narrow_programs_table(programs: List[Program]):
    headers = ["SLUG", "PLATFORM", "REWARDS", "TYPES"]
    data = []
    for program in programs:
        rewards = ",".join([reward for reward in program.rewards])
        types = ",".join([type_ for type_ in program.types])
        data.append([program.slug, program.platform, rewards, types])
    typer.echo(tabulate(data, headers, tablefmt="plain"))


def output_wide_programs_table(programs: List[Program]):
    headers = [
        "SLUG",
        "PLATFORM",
        "CREATED",
        "REWARDS",
        "SCOPES",
        "TYPES",
    ]
    data = []
    for program in programs:
        rewards = ",".join([reward for reward in program.rewards])
        types = ",".join([type_ for type_ in program.types])
        created_at = program.bounty_created_at.strftime("%Y-%m-%d")
        data.append(
            [
                program.slug,
                program.platform,
                created_at,
                rewards,
                len(program.in_scope),
                types,
            ]
        )
    typer.echo(tabulate(data, headers, tablefmt="plain"))


@get.command("programs")
def programs_get(
    program_slugs: Optional[List[str]] = typer.Argument(None),
    output: OutputFormat = typer.Option(
        OutputFormat.wide, "--output", "-o", help="Output format."
    ),
    name: str = typer.Option(None, "--name", "-n", help="Filter by name."),
    types: List[str] = typer.Option(
        None, "--types", "-t", help="Filter by scope types. Can be used multiple times."
    ),
    rewards: List[str] = typer.Option(
        None, "--rewards", "-r", help="Filter by reward types.",
    ),
    platforms: List[str] = typer.Option(
        None, "--platforms", "-p", help="Filter by platforms."
    ),
    exclude_platforms: List[str] = typer.Option(
        None,
        "--exclude-platforms",
        help="Exclude specific platforms. Ignored if --platforms was passed.",
    ),
    created_since: str = typer.Option(
        None,
        "--since",
        "-s",
        help="""
Filter by bounties created after a certain date. A specific date in the
format '%Y-%m-%d' can be supplied. Alternatively, the following keywords are supported:
'yesterday', 'last-week', 'last-month', 'last-year' as well as 'last-X-days'
(where 'X' is an integer).
    """,
    ),
):
    """
    Display one or many bug bounty programs, in a table or as JSON.

    If a list of slugs is provided is CLI arguments, this command will fetch the
    specified programs. Alternatively, the command will search through all programs
    using the supplied filters.

    CLI option filters are ignored if slugs are provided.
    """

    if created_since:
        try:
            created_since = get_datetime_from_input(created_since)
        except InvalidDateInputError:
            typer.echo(f"Invalid date input '{created_since}', see '--help'.")

    with spinner():
        if program_slugs:
            programs = (bb.program(slug) for slug in program_slugs)
        else:
            programs = bb.programs(
                name=name,
                types=types,
                platforms=platforms,
                exclude_platforms=exclude_platforms,
                rewards=rewards,
                created_since=created_since,
            )
    globals()[f"output_{output}_programs_table"](programs)


if __name__ == "__main__":
    app()
