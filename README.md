# PowerShell Compiler

compile any `.ps1` file to `.cmd` file so you can execute them by just double click in windows.

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

