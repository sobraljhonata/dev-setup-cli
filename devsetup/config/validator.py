from typing import Any

SUPPORTED_TOOLS = {
    "system",
    "git",
    "python",
    "node",
    "java",
    "mysql",
    "postgres",
}


def validate_config(config: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    profiles = config.get("profile", {})

    if not isinstance(profiles, dict):
        return ["A seção [profile] deve ser um objeto TOML válido."]

    for profile_name, profile_config in profiles.items():
        if not isinstance(profile_config, dict):
            errors.append(f"O profile '{profile_name}' deve ser uma tabela TOML.")
            continue

        tools = profile_config.get("tools")

        if tools is None:
            errors.append(f"O profile '{profile_name}' precisa declarar 'tools'.")
            continue

        if not isinstance(tools, list):
            errors.append(
                f"O campo 'tools' do profile '{profile_name}' deve ser uma lista."
            )
            continue

        if not tools:
            errors.append(
                f"O profile '{profile_name}' não pode ter lista de tools vazia."
            )
            continue

        for tool in tools:
            if not isinstance(tool, str):
                errors.append(
                    f"O profile '{profile_name}' possui uma tool inválida: {tool}."
                )
                continue

            if tool not in SUPPORTED_TOOLS:
                errors.append(
                    f"Tool '{tool}' não suportada no profile '{profile_name}'."
                )

    return errors
