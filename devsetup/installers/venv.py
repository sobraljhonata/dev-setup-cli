from rich.console import Console

from devsetup.core.shell import run_command

console = Console()


def setup_venv() -> None:
    console.print("[bold green]Configurando python3-venv...[/bold green]")

    run_command("sudo apt update -y")
    run_command("sudo apt install -y python3-venv")

    console.print("[bold green]python3-venv configurado com sucesso.[/bold green]")