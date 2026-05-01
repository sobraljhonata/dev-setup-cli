import pytest

from devsetup import doctor


def test_check_min_version_returns_absent_when_command_does_not_exist(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(doctor, "command_exists", lambda command: False)

    status, version = doctor.check_min_version(
        "node",
        ["node", "-v"],
        doctor.Version(22, 0, 0),
    )

    assert "Ausente" in status
    assert version == "-"


def test_check_min_version_returns_ok_when_version_is_compatible(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(doctor, "command_exists", lambda command: True)
    monkeypatch.setattr(doctor, "get_command_output", lambda command: "v22.11.0")

    status, version = doctor.check_min_version(
        "node",
        ["node", "-v"],
        doctor.Version(22, 0, 0),
    )

    assert "OK" in status
    assert version == "v22.11.0"


def test_check_min_version_returns_outdated_when_version_is_lower(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(doctor, "command_exists", lambda command: True)
    monkeypatch.setattr(doctor, "get_command_output", lambda command: "v20.9.0")

    status, version = doctor.check_min_version(
        "node",
        ["node", "-v"],
        doctor.Version(22, 0, 0),
    )

    assert "Desatualizado" in status
    assert version == "v20.9.0"


def test_check_python_module_returns_true_when_module_is_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        doctor,
        "get_command_output",
        lambda command: "usage: venv [-h]",
    )

    assert doctor.check_python_module("venv") is True


def test_check_python_module_returns_false_when_module_is_not_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(doctor, "get_command_output", lambda command: None)

    assert doctor.check_python_module("venv") is False


def test_check_service_returns_running_when_service_is_running(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        doctor,
        "get_command_output",
        lambda command: "mysql is running",
    )

    assert doctor.check_service("mysql") == "Rodando"


def test_check_service_returns_stopped_when_service_is_not_running(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        doctor,
        "get_command_output",
        lambda command: "mysql is stopped",
    )

    assert doctor.check_service("mysql") == "Parado ou não encontrado"
