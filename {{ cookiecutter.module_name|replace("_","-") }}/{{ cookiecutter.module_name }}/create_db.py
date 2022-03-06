"""Initializes the database for the given environment with the {{ cookiecutter.project_name }} schema.
"""
import click

from {{ cookiecutter.module_name }}.models import Base
from {{ cookiecutter.module_name }}.database import Database as Db

@click.command()
@click.argument("environment", default="DEFAULT")
@click.confirmation_option(prompt="Are you sure you want to drop and re-"
    + "create the database schema?")
def __main__(environment):
    """Re-runs the ORM schema creation on the database in the given environment."""
    Db.init(environment, echo=True)
    Base.metadata.create_all(Db.engine)

