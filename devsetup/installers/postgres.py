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

    run_command(
        f"""sudo -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = '{db_name}'" | grep -q 1 || sudo -u postgres createdb {db_name}"""
    )

    run_command(
        f"""sudo -u postgres psql -tc "SELECT 1 FROM pg_roles WHERE rolname = '{db_user}'" | grep -q 1 || sudo -u postgres psql -c "CREATE USER {db_user} WITH PASSWORD '{db_password}';" """
    )

    run_command(
        f"""sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};" """
    )

    console.print("[bold green]PostgreSQL configurado com sucesso.[/bold green]")