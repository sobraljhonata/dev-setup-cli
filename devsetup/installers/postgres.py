from rich.console import Console

from devsetup.core.checks import command_exists
from devsetup.core.prompt import ask_password, ask_text
from devsetup.core.shell import run_command

console = Console()


def setup_postgres() -> None:
    console.print("[bold green]Configurando PostgreSQL...[/bold green]")

    if not command_exists("psql"):
        run_command("sudo apt install -y postgresql postgresql-contrib")
    else:
        console.print("[green]PostgreSQL já está instalado.[/green]")

    run_command("sudo service postgresql start")

    db_name = ask_text("Nome do banco de dados", "db_app")
    db_user = ask_text("Nome do usuário", "user_app")
    db_password = ask_password("Senha do usuário", "Senha@123")

    database_exists_command = (
        "sudo -u postgres psql -tc "
        f""""SELECT 1 FROM pg_database WHERE datname = '{db_name}'" """
        f"| grep -q 1 || sudo -u postgres createdb {db_name}"
    )

    user_exists_command = (
        "sudo -u postgres psql -tc "
        f""""SELECT 1 FROM pg_roles WHERE rolname = '{db_user}'" """
        "| grep -q 1 || "
        "sudo -u postgres psql -c "
        f""""CREATE USER {db_user} WITH PASSWORD '{db_password}';" """
    )

    grant_privileges_command = (
        "sudo -u postgres psql -c "
        f""""GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};" """
    )

    run_command(database_exists_command)
    run_command(user_exists_command)
    run_command(grant_privileges_command)

    console.print("[bold green]PostgreSQL configurado com sucesso.[/bold green]")
