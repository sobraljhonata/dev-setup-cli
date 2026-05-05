from collections.abc import Callable
from typing import Any

from rich.console import Console

from devsetup.config.loader import load_config
from devsetup.installers.git import setup_git
from devsetup.installers.java import setup_java
from devsetup.installers.mysql import setup_mysql
from devsetup.installers.node import setup_node
from devsetup.installers.postgres import setup_postgres
from devsetup.installers.python import setup_python
from devsetup.installers.system import setup_system

console = Console()

Installer = Callable[[], None]

PROFILE_MAP: dict[str, Installer] = {
    "system": setup_system,
    "git": setup_git,
    "python": setup_python,
    "node": setup_node,
    "java": setup_java,
    "mysql": setup_mysql,
    "postgres": setup_postgres,
}

DEFAULT_PROFILES: dict[str, list[str]] = {
    "backend": ["system", "git", "python", "node", "java", "postgres"],
    "frontend": ["system", "git", "node"],
    "fullstack": ["system", "git", "python", "node", "java", "mysql", "postgres"],
    "python": ["system", "git", "python"],
}


def get_config_profiles(config: dict[str, Any]) -> dict[str, list[str]]:
    profiles = config.get("profile", {})

    if not isinstance(profiles, dict):
        return {}

    parsed_profiles: dict[str, list[str]] = {}

    for profile_name, profile_config in profiles.items():
        if not isinstance(profile_config, dict):
            continue

        tools = profile_config.get("tools", [])

        if not isinstance(tools, list):
            continue

        parsed_profiles[profile_name] = [
            tool for tool in tools if isinstance(tool, str)
        ]

    return parsed_profiles


def get_profile_tools(profile_name: str) -> list[str]:
    config = load_config()
    config_profiles = get_config_profiles(config)

    if profile_name in config_profiles:
        return config_profiles[profile_name]

    if profile_name in DEFAULT_PROFILES:
        return DEFAULT_PROFILES[profile_name]

    available_profiles = sorted(
        set(DEFAULT_PROFILES.keys()) | set(config_profiles.keys())
    )

    raise ValueError(
        f"Profile '{profile_name}' não encontrado. "
        f"Profiles disponíveis: {', '.join(available_profiles)}"
    )


def validate_tools(tools: list[str]) -> None:
    unsupported_tools = [tool for tool in tools if tool not in PROFILE_MAP]

    if unsupported_tools:
        supported_tools = ", ".join(sorted(PROFILE_MAP.keys()))
        invalid_tools = ", ".join(unsupported_tools)

        raise ValueError(
            f"Tool(s) não suportada(s): {invalid_tools}. "
            f"Tools suportadas: {supported_tools}"
        )


def run_profile(profile_name: str) -> None:
    tools = get_profile_tools(profile_name)

    validate_tools(tools)

    console.print(f"[bold green]Executando profile {profile_name}...[/bold green]")

    for tool in tools:
        console.print(f"[cyan]Executando etapa:[/cyan] {tool}")
        installer = PROFILE_MAP[tool]
        installer()


def setup_backend_profile() -> None:
    run_profile("backend")


def setup_frontend_profile() -> None:
    run_profile("frontend")


def setup_fullstack_profile() -> None:
    run_profile("fullstack")


def setup_python_profile() -> None:
    run_profile("python")
