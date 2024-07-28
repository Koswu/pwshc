from pathlib import Path
from typing import Optional
from jinja2 import Environment, PackageLoader, select_autoescape
import chardet

_env = Environment(
    loader=PackageLoader("pwshc", "templates"),
    autoescape=select_autoescape(),
)
_cmd_template = _env.get_template("out.cmd.jinja")


def compile(input: Path, output: Optional[Path] = None, delete_temp_file: bool = True):
    if not input.exists() or not input.is_file():
        raise FileNotFoundError(f"Input file not found: {input}")
    if output is None:
        output = input.with_suffix(".cmd")
    if output.is_dir():
        output = output / input.with_suffix(".cmd").name
    if not output.parent.exists():
        raise FileNotFoundError(f"Output directory not found: {output.parent}")
    # guess input encoding with chardet
    guessed_encoding = chardet.detect(input.read_bytes())["encoding"]
    script = input.read_text(encoding=guessed_encoding)
    output.write_text(
        _cmd_template.render(script=script, delete_temp_file=delete_temp_file)
    )
