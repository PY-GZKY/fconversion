import click
from colorama import init

from .file_core import FileEngine
from .version import __version__

init(autoreset=True)


@click.command("fc")
@click.version_option(__version__, '-V', '--version', prog_name='fc')
@click.option('--type')
@click.option('--ord', default=None, help="")
@click.option('--tar', is_flag=True, help="")
def cli(*, type: str = '', ord: str, tar: str):
    f_ = FileEngine()


if __name__ == '__main__':
    cli()
