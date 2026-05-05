from pathlib import Path
from typing import Any

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # Python 3.10 fallback


CONFIG_FILE_NAME = ".devsetup.toml"


def load_config(config_path: Path | None = None) -> dict[str, Any]:
    path = config_path or Path.cwd() / CONFIG_FILE_NAME

    if not path.exists():
        return {}

    with path.open("rb") as file:
        return tomllib.load(file)
