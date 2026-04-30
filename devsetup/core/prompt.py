from getpass import getpass

AUTO_YES = False


def set_auto_yes(value: bool) -> None:
    global AUTO_YES
    AUTO_YES = value


def ask_text(message: str, default: str) -> str:
    value = input(f"{message} [{default}]: ").strip()
    return value or default


def ask_password(message: str, default: str = "") -> str:
    value = getpass(f"{message}: ").strip()
    return value or default


def confirm(message: str) -> bool:
    if AUTO_YES:
        return True

    answer = input(f"{message} (s/n): ").strip().lower()
    return answer == "s"