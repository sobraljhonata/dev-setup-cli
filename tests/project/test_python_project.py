from pathlib import Path

import pytest

from devsetup.project import python_project


def test_create_python_project_creates_project_structure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)

    executed_commands: list[str] = []

    def fake_run_command(command: str, check: bool = True) -> None:
        executed_commands.append(command)

    monkeypatch.setattr(python_project, "run_command", fake_run_command)

    python_project.create_python_project("minha-poc")

    project_dir = tmp_path / "Projetos" / "minha-poc"
    main_file = project_dir / "main.py"

    assert project_dir.exists()
    assert main_file.exists()
    assert 'print("Hello, world!")' in main_file.read_text(encoding="utf-8")

    assert f"python3 -m venv {project_dir}/.venv" in executed_commands
    assert f"code {project_dir}" in executed_commands


def test_create_python_project_does_not_overwrite_existing_main_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)

    project_dir = tmp_path / "Projetos" / "minha-poc"
    project_dir.mkdir(parents=True)

    main_file = project_dir / "main.py"
    main_file.write_text("print('conteudo existente')", encoding="utf-8")

    monkeypatch.setattr(python_project, "run_command", lambda command, check=True: None)

    python_project.create_python_project("minha-poc")

    assert main_file.read_text(encoding="utf-8") == "print('conteudo existente')"


def test_create_python_project_creates_projects_directory_when_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.setattr(python_project, "run_command", lambda command, check=True: None)

    python_project.create_python_project("app")

    assert (tmp_path / "Projetos").exists()
    assert (tmp_path / "Projetos" / "app").exists()