from pathlib import Path
from typing_extensions import Annotated, Optional
import typer

from pwshc._compile import compile

_InputFile = Annotated[Path, typer.Argument(help="The PowerShell file to compile.")]
_OutputPath = Annotated[
    Optional[Path],
    typer.Option(
        "--output",
        "-o",
        help="The output path for the compiled .cmd file. If not provided, the compiled file will be saved in the same directory as the input file.",
    ),
]
_DeleteTempFileFlag = Annotated[
    bool,
    typer.Option(
        help="Delete the temporary .ps1 file after .cmd execution.",
        show_default=True,
        is_flag=True,
    ),
]


def main(
    input: _InputFile,
    output: _OutputPath = None,
    del_temp_file: _DeleteTempFileFlag = True,
):
    compile(input, output, del_temp_file)
