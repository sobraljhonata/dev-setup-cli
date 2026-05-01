from typer.testing import CliRunner

from devsetup.cli import app

runner = CliRunner()


def test_cli_help() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "CLI para setup" in result.stdout


def test_cli_system_command(monkeypatch) -> None:
    called = {"executed": False}

    def fake_setup_system():
        called["executed"] = True

    monkeypatch.setattr("devsetup.cli.setup_system", fake_setup_system)
    monkeypatch.setattr("devsetup.cli.confirm", lambda msg: True)

    result = runner.invoke(app, ["system"])

    assert result.exit_code == 0
    assert called["executed"] is True


def test_cli_project_command(monkeypatch) -> None:
    called = {"name": None}

    def fake_create_project(name: str):
        called["name"] = name

    monkeypatch.setattr(
        "devsetup.cli.create_python_project",
        fake_create_project,
    )

    result = runner.invoke(app, ["project", "meu-app"])

    assert result.exit_code == 0
    assert called["name"] == "meu-app"


def test_cli_doctor_command(monkeypatch) -> None:
    called = {"executed": False}

    def fake_doctor():
        called["executed"] = True

    monkeypatch.setattr("devsetup.cli.run_doctor", fake_doctor)

    result = runner.invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert called["executed"] is True


def test_cli_yes_flag_skips_confirmation(monkeypatch) -> None:
    called = {"executed": False}

    def fake_setup_system():
        called["executed"] = True

    monkeypatch.setattr("devsetup.cli.setup_system", fake_setup_system)

    result = runner.invoke(app, ["--yes", "system"])

    assert result.exit_code == 0
    assert called["executed"] is True
