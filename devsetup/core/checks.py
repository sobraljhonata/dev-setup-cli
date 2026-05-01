import shutil
import subprocess


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def get_command_output(command: list[str]) -> str | None:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout.strip() or result.stderr.strip()

        return output or None
    except Exception:
        return None
