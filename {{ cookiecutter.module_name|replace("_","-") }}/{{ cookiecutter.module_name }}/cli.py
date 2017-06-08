"""Command line interface for {{ cookiecutter.project_name }}."""
import click

@click.command()
def cli():
    """Default entry point when running the {{ cookiecutter.module_name|replace('_','-') }} command."""
    click.echo("Hello World")
