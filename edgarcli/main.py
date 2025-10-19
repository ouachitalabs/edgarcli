"""Main CLI entry point for edgarcli."""

import click
from edgar import set_identity, get_identity
from edgarcli import __version__
from edgarcli.config import get_config, ensure_identity
from edgarcli.commands import company, filing, filings, statements
from edgarcli.commands import config as config_cmd


@click.group()
@click.version_option(version=__version__, prog_name="edgarcli")
@click.option(
    "--identity",
    envvar="EDGAR_IDENTITY",
    help="SEC EDGAR identity (Name email@example.com)",
)
@click.pass_context
def cli(ctx, identity):
    """edgarcli - CLI wrapper for SEC EDGAR data access.

    Provides command-line access to SEC filings, company information,
    and financial statements via the edgartools library.
    """
    ctx.ensure_object(dict)

    # Set identity from flag, config, or environment
    if identity:
        set_identity(identity)
        ctx.obj["identity"] = identity
    else:
        # Try to load from config
        config = get_config()
        if config.get("identity"):
            set_identity(config["identity"])
            ctx.obj["identity"] = config["identity"]
        else:
            ctx.obj["identity"] = None

    ctx.obj["interactive"] = False


# Register command groups
cli.add_command(config_cmd.config)
cli.add_command(company.company)
cli.add_command(filing.filing)
cli.add_command(filings.filings)
cli.add_command(statements.statements)


if __name__ == "__main__":
    cli()
