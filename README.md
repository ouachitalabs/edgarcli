# edgarcli

A CLI wrapper around [edgartools](https://github.com/dgunning/edgartools) by Dwight Gunning - access SEC EDGAR data from the command line.

## Installation

```bash
pip install edgarcli
```

## Quick Start

```bash
# Set your identity (required by SEC)
edgarcli config set-identity "Your Name your.email@example.com"

# Get company info
edgarcli company AAPL

# View recent filings
edgarcli filings AAPL --form 10-K --limit 5

# Get a specific filing
edgarcli filing AAPL --form 10-K --latest

# Get financial statements
edgarcli statements AAPL --form 10-Q --statement income

# Interactive mode (drop into IPython REPL)
edgarcli company AAPL -i
```

## Commands

- `config` - Manage configuration (identity, paths)
- `company` - Get company information by ticker/CIK
- `filing` - Get specific SEC filing(s)
- `filings` - List historical filings for a company
- `statements` - Get financial statements from filings

All commands support `--help` for detailed options and `-i` for interactive mode.

## Configuration

Identity can be set via config file (`~/.config/edgarcli/config.json`), environment variable (`EDGAR_IDENTITY`), or `--identity` flag.

## Credits

Built on [edgartools](https://github.com/dgunning/edgartools) by Dwight Gunning.

## License

MIT
