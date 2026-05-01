from rich.console import Console

from devsetup.core.checks import command_exists
from devsetup.core.shell import run_command

console = Console()


def setup_java() -> None:
    console.print("[bold green]Configurando Java 21 e Maven...[/bold green]")

    if not command_exists("java"):
        run_command("sudo apt install -y openjdk-21-jdk")
    else:
        console.print("[green]Java já está instalado.[/green]")

    if not command_exists("mvn"):
        run_command("sudo apt install -y maven")
    else:
        console.print("[green]Maven já está instalado.[/green]")

    run_command("java -version", check=False)
    run_command("mvn -version", check=False)

    console.print("[bold green]Java configurado com sucesso.[/bold green]")
