from rich.console import Console

from devsetup.core.checks import command_exists, get_command_output
from devsetup.core.shell import run_command

console = Console()


def setup_node() -> None:
    console.print("[bold green]Configurando Node.js 22...[/bold green]")

    if command_exists("node"):
        version = get_command_output(["node", "-v"])

        if version:
            major_version = int(version.replace("v", "").split(".")[0])

            if major_version >= 22:
                console.print(f"[green]Node.js já está instalado na versão {version}.[/green]")
                return

            console.print(f"[yellow]Node.js {version} encontrado. Atualizando...[/yellow]")

    run_command("curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -")
    run_command("sudo apt install -y nodejs")

    run_command("node -v", check=False)
    run_command("npm -v", check=False)

    console.print("[bold green]Node.js configurado com sucesso.[/bold green]")