from rich.console import Console

from devsetup.core.checks import command_exists
from devsetup.core.shell import run_command

console = Console()


def setup_git() -> None:
    console.print("[bold green]Configurando Git...[/bold green]")

    if not command_exists("git"):
        run_command("sudo apt install -y git")
    else:
        console.print("[green]Git já está instalado.[/green]")

    username = input("Digite seu nome para o Git: ").strip()
    email = input("Digite seu e-mail para o Git: ").strip()

    if username:
        run_command(f'git config --global user.name "{username}"')

    if email:
        run_command(f'git config --global user.email "{email}"')

    run_command("git config --global init.defaultBranch main")
    run_command("git config --global core.editor 'code --wait'")
    run_command("git config --global pull.rebase false")
    status_alias_command = "git config --global alias.s '!git status -s'"

    commit_alias_command = (
        'git config --global alias.c "!git add --all && git commit -m"'
    )

    log_alias_command = (
        "git config --global alias.l "
        '"!git log --pretty=format:'
        "'%C(blue)%h%C(red)%d %C(white)%s - %C(cyan)%cn, %C(green)%cr'\""
    )

    run_command(status_alias_command)
    run_command(commit_alias_command)
    run_command(log_alias_command)

    console.print("[bold green]Git configurado com sucesso.[/bold green]")
