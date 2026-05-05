import typer

from devsetup.core.prompt import confirm, set_auto_yes
from devsetup.core.shell import set_dry_run
from devsetup.doctor import run_doctor
from devsetup.installers.git import setup_git
from devsetup.installers.java import setup_java
from devsetup.installers.mysql import setup_mysql
from devsetup.installers.node import setup_node
from devsetup.installers.postgres import setup_postgres
from devsetup.installers.python import setup_python
from devsetup.installers.system import setup_system
from devsetup.installers.venv import setup_venv
from devsetup.profiles.profiles import (
    run_profile,
    setup_backend_profile,
    setup_frontend_profile,
    setup_fullstack_profile,
    setup_python_profile,
)
from devsetup.project.python_project import create_python_project

app = typer.Typer(help="CLI para setup de ambiente de desenvolvimento no WSL/Linux.")
profile_app = typer.Typer(help="Profiles de setup por tipo de ambiente.")
app.add_typer(profile_app, name="profile")


@app.callback()
def main(
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Mostra os comandos sem executar.",
    ),
    yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Confirma automaticamente as ações.",
    ),
) -> None:
    set_dry_run(dry_run)
    set_auto_yes(yes)


@app.command()
def system() -> None:
    if confirm("Deseja atualizar pacotes do sistema?"):
        setup_system()


@app.command()
def python() -> None:
    setup_python()


@app.command()
def node() -> None:
    setup_node()


@app.command()
def java() -> None:
    setup_java()


@app.command()
def git() -> None:
    setup_git()


@app.command()
def mysql() -> None:
    if confirm("Deseja instalar/configurar o MySQL?"):
        setup_mysql()


@app.command()
def postgres() -> None:
    if confirm("Deseja instalar/configurar o PostgreSQL?"):
        setup_postgres()


@app.command()
def project(name: str) -> None:
    create_python_project(name)


@app.command()
def doctor() -> None:
    """Diagnostica o ambiente de desenvolvimento."""
    run_doctor()


@app.command()
def venv() -> None:
    """Instala o pacote python3-venv."""
    setup_venv()


@profile_app.command("backend")
def profile_backend() -> None:
    """Configura ambiente backend."""
    if confirm("Deseja executar o profile backend?"):
        setup_backend_profile()


@profile_app.command("frontend")
def profile_frontend() -> None:
    """Configura ambiente frontend."""
    if confirm("Deseja executar o profile frontend?"):
        setup_frontend_profile()


@profile_app.command("fullstack")
def profile_fullstack() -> None:
    """Configura ambiente fullstack."""
    if confirm("Deseja executar o profile fullstack?"):
        setup_fullstack_profile()


@profile_app.command("python")
def profile_python() -> None:
    """Configura ambiente Python."""
    if confirm("Deseja executar o profile python?"):
        setup_python_profile()


@profile_app.command("run")
def profile_run(name: str) -> None:
    """Executa um profile pelo nome, usando .devsetup.toml ou fallback padrão."""
    if confirm(f"Deseja executar o profile {name}?"):
        run_profile(name)


@app.command()
def all() -> None:
    if not confirm("Deseja executar o setup completo?"):
        return

    setup_system()
    setup_python()
    setup_node()
    setup_java()
    setup_git()
    setup_mysql()
    setup_postgres()


if __name__ == "__main__":
    app()
