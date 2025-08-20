import logging

import click

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--name",
    help="The person to greet.",
)
def hello(name: str) -> None:
    """Say hello to NAME."""
    click.echo(f"Hello {name}!")
    logger.log(logging.INFO, "✅ Hello executed.")


if __name__ == "__main__":
    hello()
