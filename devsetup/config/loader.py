from pathlib import Path
from typing import Any

import tomllib

CONFIG_FILE_NAME = ".devsetup.toml"


def load_config(config_path: Path | None = None) -> dict[str, Any]:
    path = config_path or Path.cwd() / CONFIG_FILE_NAME

    if not path.exists():
        return {}

    with path.open("rb") as file:
        return tomllib.load(file)
