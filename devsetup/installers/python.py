from rich.console import Console

from devsetup.core.checks import command_exists
from devsetup.core.shell import run_command
from devsetup.installers.venv import setup_venv

console = Console()


def setup_python() -> None:
    console.print("[bold green]Configurando Python...[/bold green]")

    if not command_exists("python3"):
        run_command("sudo apt install -y python3")
    else:
        console.print("[green]Python 3 já está instalado.[/green]")

    run_command("sudo apt install -y python3-pip")

    setup_venv()

    run_command("touch ~/.bash_aliases")

    alias_command = (
        "grep -qxF \"alias python='python3'\" ~/.bash_aliases "
        "|| echo \"alias python='python3'\" >> ~/.bash_aliases"
    )

    run_command(alias_command)

    console.print("[bold green]Python configurado com sucesso.[/bold green]")
