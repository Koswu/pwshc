#!/usr/bin/env python3

import typer
from pwshc._cmd import main


def cli():
    typer.run(main)


if __name__ == "__main__":
    cli()
