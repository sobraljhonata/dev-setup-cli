import subprocess
import sys

from rich.console import Console

console = Console()

DRY_RUN = False


def set_dry_run(value: bool) -> None:
    global DRY_RUN
    DRY_RUN = value


def run_command(command: str, check: bool = True) -> None:
    console.print(f"[bold blue]Executando:[/bold blue] {command}")

    if DRY_RUN:
        console.print("[yellow]Dry-run ativo. Comando não executado.[/yellow]")
        return

    try:
        subprocess.run(
            command,
            shell=True,
            check=check,
            executable="/bin/bash",
        )
    except subprocess.CalledProcessError as error:
        console.print(f"[bold red]Erro ao executar comando:[/bold red] {command}")
        console.print(f"[red]Código de saída:[/red] {error.returncode}")
        sys.exit(error.returncode)
