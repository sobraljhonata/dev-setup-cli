import subprocess

import pytest

from devsetup.core import checks


def test_command_exists_returns_true_when_command_is_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(checks.shutil, "which", lambda command: f"/usr/bin/{command}")

    assert checks.command_exists("python3") is True


def test_command_exists_returns_false_when_command_is_not_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(checks.shutil, "which", lambda command: None)

    assert checks.command_exists("unknown") is False


def test_get_command_output_returns_stdout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(*args, **kwargs):
        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout="Python 3.12.3\n",
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert checks.get_command_output(["python3", "--version"]) == "Python 3.12.3"


def test_get_command_output_returns_stderr_when_stdout_is_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(*args, **kwargs):
        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout="",
            stderr='openjdk version "21.0.5"\n',
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert checks.get_command_output(["java", "-version"]) == 'openjdk version "21.0.5"'


def test_get_command_output_returns_none_on_exception(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(*args, **kwargs):
        raise RuntimeError("error")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert checks.get_command_output(["invalid"]) is None
