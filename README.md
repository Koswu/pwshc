# PowerShell Compiler

[![PyPI](https://img.shields.io/pypi/v/pwshc?label=pypi%20package)](https://pypi.org/project/pwshc/)

Compile any `.ps1` file into a `.cmd` file so that you can execute it with a double-click in Windows.

## Usage

Install this package by pipx:

```powershell
pipx install pwshc
```


Compile your `.ps1` file:

```powershell
pwshc hello_world.ps1 -o hello_world.cmd 
# -o is optional
```

