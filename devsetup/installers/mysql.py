from rich.console import Console

from devsetup.core.checks import command_exists
from devsetup.core.prompt import ask_password, ask_text
from devsetup.core.shell import run_command

console = Console()


def setup_mysql() -> None:
    console.print("[bold green]Configurando MySQL...[/bold green]")

    if not command_exists("mysql"):
        run_command("sudo apt install -y mysql-server")
    else:
        console.print("[green]MySQL já está instalado.[/green]")

    run_command("sudo service mysql start")

    db_name = ask_text("Nome do banco de dados", "db_app")
    db_user = ask_text("Nome do usuário", "user_app")
    db_password = ask_password("Senha do usuário", "Senha@123")

    create_database_command = (
        f"""sudo mysql -e "CREATE DATABASE IF NOT EXISTS {db_name};" """
    )

    create_user_command = (
        "sudo mysql -e "
        f""""CREATE USER IF NOT EXISTS '{db_user}'@'localhost' """
        f"""IDENTIFIED BY '{db_password}';" """
    )

    grant_privileges_command = (
        "sudo mysql -e "
        f""""GRANT ALL PRIVILEGES ON {db_name}.* """
        f"""TO '{db_user}'@'localhost';" """
    )

    run_command(create_database_command)
    run_command(create_user_command)
    run_command(grant_privileges_command)
    run_command("""sudo mysql -e "FLUSH PRIVILEGES;" """)

    console.print("[bold green]MySQL configurado com sucesso.[/bold green]")
