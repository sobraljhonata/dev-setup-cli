import subprocess

import pytest

from devsetup.core import shell


def test_run_command_executes_subprocess(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {}

    def fake_run(*args, **kwargs):
        called["args"] = args
        called["kwargs"] = kwargs
        return subprocess.CompletedProcess(args=args, returncode=0)

    monkeypatch.setattr(subprocess, "run", fake_run)

    shell.set_dry_run(False)
    shell.run_command("echo test")

    assert called["args"][0] == "echo test"
    assert called["kwargs"]["shell"] is True
    assert called["kwargs"]["check"] is True
    assert called["kwargs"]["executable"] == "/bin/bash"


def test_run_command_does_not_execute_when_dry_run_is_enabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    called = False

    def fake_run(*args, **kwargs):
        nonlocal called
        called = True

    monkeypatch.setattr(subprocess, "run", fake_run)

    shell.set_dry_run(True)
    shell.run_command("echo test")

    assert called is False

    shell.set_dry_run(False)


def test_run_command_exits_when_command_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(*args, **kwargs):
        raise subprocess.CalledProcessError(returncode=1, cmd="invalid")

    monkeypatch.setattr(subprocess, "run", fake_run)

    shell.set_dry_run(False)

    with pytest.raises(SystemExit) as error:
        shell.run_command("invalid")

    assert error.value.code == 1
