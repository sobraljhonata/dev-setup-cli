from pathlib import Path

from rich.console import Console

from devsetup.core.shell import run_command

console = Console()


def create_python_project(project_name: str) -> None:
    home_dir = Path.home()
    projects_dir = home_dir / "Projetos"
    project_dir = projects_dir / project_name

    projects_dir.mkdir(exist_ok=True)
    project_dir.mkdir(exist_ok=True)

    main_file = project_dir / "main.py"

    if not main_file.exists():
        main_file.write_text(
            'def main():\n    print("Hello, world!")\n\n\nif __name__ == "__main__":\n    main()\n',
            encoding="utf-8",
        )

    run_command(f"python3 -m venv {project_dir}/.venv")
    
    gitignore = project_dir / ".gitignore"

    if not gitignore.exists():
        gitignore.write_text(
            "__pycache__/\n.venv/\n.env\n*.pyc\n",
            encoding="utf-8",
        )

    console.print(f"[bold green]Projeto criado em:[/bold green] {project_dir}")
    console.print("")
    console.print("Para ativar o ambiente virtual:")
    console.print(f"[bold cyan]cd {project_dir}[/bold cyan]")
    console.print("[bold cyan]source .venv/bin/activate[/bold cyan]")

    run_command(f"code {project_dir}", check=False)