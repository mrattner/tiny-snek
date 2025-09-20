"""
Initializes the database for the given environment with the {{ cookiecutter.project_name }} schema.
"""
import typer

from {{ cookiecutter.module_name }}.models import Base
from {{ cookiecutter.module_name }}.database import Database as Db


def main(environment: str = "DEFAULT"):
"""Re-runs the ORM schema creation on the database in the given environment."""
    confirm = typer.confirm("Are you sure you want to drop and re-create the database schema?")
    if not confirm:
        raise typer.Abort()
    Db.init(environment, echo=True)
    Base.metadata.create_all(Db.engine)
    typer.echo("Database is now ready to use.")


if __name__ == "__main__":
    typer.run(main)

