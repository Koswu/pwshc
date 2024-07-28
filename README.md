# PowerShell Compiler

[![PyPI](https://img.shields.io/pypi/v/pwshc?label=pypi%20package)](https://pypi.org/project/pwshc/)

Compile any `.ps1` file into a `.cmd` file so that you can execute it with a double-click in Windows.

## Usage

Install this package by pipx:

```shell
pipx install pwshc
```


Compile your `.ps1` file:

```shell
pwshc hello_world.ps1 -o hello_world.cmd 
# -o is optional
```

### Auto elevate

You can add auto elevate (run as admin) code to your .cmd file:

```shell
pwshc hello_world.ps1 --auto-elevate
```

