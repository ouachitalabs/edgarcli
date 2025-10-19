"""Company lookup commands."""

import click
from edgar import Company
from rich import print as rprint
from edgarcli.config import ensure_identity
from edgarcli.utils import handle_edgar_error, maybe_interactive


@click.command()
@click.argument("ticker_or_cik")
@click.option(
    "-i", "--interactive",
    is_flag=True,
    help="Drop into interactive REPL after displaying company info",
)
@click.pass_context
@handle_edgar_error
def company(ctx, ticker_or_cik, interactive):
    """Get company information by ticker or CIK.

    TICKER_OR_CIK can be:
      - Ticker symbol (e.g., AAPL, MSFT)
      - CIK number (e.g., 320193 or 0000320193)

    Examples:
        edgarcli company AAPL
        edgarcli company 320193
        edgarcli company TSLA -i
    """
    ensure_identity(ctx)
    ctx.obj["interactive"] = interactive

    # Look up company
    comp = Company(ticker_or_cik)

    # Display company info with Rich formatting
    rprint(comp)

    # Enter interactive mode if requested
    maybe_interactive(ctx, comp, "Company object")
