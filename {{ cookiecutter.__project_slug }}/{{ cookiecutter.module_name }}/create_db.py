"""Initializes the database for the given environment with the {{ cookiecutter.project_name }} schema."""

import io
from pathlib import Path
from typing import Annotated

import typer

from {{ cookiecutter.module_name }}.database import get_db
from {{ cookiecutter.module_name }}.models import init_schema


def main(
    settings: Annotated[
        Path, typer.Option(exists=True, file_okay=True, dir_okay=False)
    ],
):
    """Re-run the ORM schema creation on the database in the given environment."""
    confirm = typer.confirm(
        "Are you sure you want to drop and re-create the database schema?"
    )
    if not confirm:
        raise typer.Abort

    settings_file = io.FileIO(settings, "r")
    init_schema(get_db(settings_file))
    typer.echo("Database is now ready to use.")


if __name__ == "__main__":
    typer.run(main)
