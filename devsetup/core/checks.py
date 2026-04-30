import shutil
import subprocess
from typing import Optional


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def get_command_output(command: list[str]) -> Optional[str]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None