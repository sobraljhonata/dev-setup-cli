from rich.console import Console

from devsetup.core.shell import run_command

console = Console()


def setup_system() -> None:
    console.print("[bold green]Atualizando sistema...[/bold green]")

    run_command("sudo apt update -y")
    run_command("sudo apt upgrade -y")
    run_command(
        "sudo apt install -y curl wget unzip zip build-essential software-properties-common ca-certificates gnupg lsb-release"
    )

    console.print("[bold green]Sistema atualizado com sucesso.[/bold green]")