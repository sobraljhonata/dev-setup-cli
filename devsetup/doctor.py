from rich.console import Console
from rich.table import Table

from devsetup.config.requirements import SIMPLE_REQUIREMENTS, VERSION_REQUIREMENTS
from devsetup.core.checks import command_exists, get_command_output
from devsetup.core.version import Version, is_version_compatible, parse_version

console = Console()


def get_version_output(command: str, args: list[str]) -> str:
    if not command_exists(command):
        return "-"

    output = get_command_output(args)

    if not output:
        return "Versão não identificada"

    return output.splitlines()[0]


def check_min_version(
    command: str,
    version_command: list[str],
    minimum: Version,
) -> tuple[str, str]:
    if not command_exists(command):
        return "[red]Ausente[/red]", "-"

    output = get_command_output(version_command)

    if not output:
        return "[yellow]Indefinido[/yellow]", "Versão não identificada"

    raw_version = output.splitlines()[0]
    parsed_version = parse_version(raw_version)

    if parsed_version is None:
        return "[yellow]Indefinido[/yellow]", raw_version

    if is_version_compatible(parsed_version, minimum):
        return "[green]OK[/green]", raw_version

    return "[red]Desatualizado[/red]", raw_version


def check_service(service_name: str) -> str:
    output = get_command_output(["service", service_name, "status"])

    if output and "running" in output.lower():
        return "Rodando"

    return "Parado ou não encontrado"


def check_python_module(module: str) -> bool:
    output = get_command_output(["python3", "-m", module, "--help"])
    return output is not None


def run_doctor() -> None:
    console.print("[bold green]Diagnóstico do ambiente[/bold green]")

    table = Table(title="Ferramentas")

    table.add_column("Ferramenta", style="cyan")
    table.add_column("Status")
    table.add_column("Versão/Detalhe")
    table.add_column("Versão mínima")
    table.add_column("Sugestão")

    for name, command, version_command, minimum, suggestion in VERSION_REQUIREMENTS:
        status, version = check_min_version(command, version_command, minimum)

        fix = "-"
        if "Ausente" in status or "Desatualizado" in status:
            fix = suggestion

        table.add_row(
            name,
            status,
            version,
            f">= {minimum}",
            fix,
        )

    for name, command, version_command, suggestion in SIMPLE_REQUIREMENTS:
        installed = command_exists(command)
        status = "[green]OK[/green]" if installed else "[red]Ausente[/red]"
        version = get_version_output(command, version_command)
        fix = "-" if installed else suggestion

        table.add_row(name, status, version, "-", fix)

    console.print(table)

    services_table = Table(title="Serviços")

    services_table.add_column("Serviço", style="cyan")
    services_table.add_column("Status")
    services_table.add_column("Sugestão")

    mysql_status = check_service("mysql")
    postgres_status = check_service("postgresql")

    services_table.add_row(
        "MySQL",
        mysql_status,
        "-" if mysql_status == "Rodando" else "sudo service mysql start",
    )

    services_table.add_row(
        "PostgreSQL",
        postgres_status,
        "-" if postgres_status == "Rodando" else "sudo service postgresql start",
    )

    console.print(services_table)
