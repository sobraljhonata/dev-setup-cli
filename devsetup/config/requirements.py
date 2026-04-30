from devsetup.core.version import Version


VERSION_REQUIREMENTS = [
    ("Python", "python3", ["python3", "--version"], Version(3, 10, 0), "devsetup python"),
    ("Node.js", "node", ["node", "-v"], Version(22, 0, 0), "devsetup node"),
    ("Java", "java", ["java", "-version"], Version(21, 0, 0), "devsetup java"),
    ("Maven", "mvn", ["mvn", "-version"], Version(3, 8, 0), "devsetup java"),
    ("Git", "git", ["git", "--version"], Version(2, 34, 0), "devsetup git"),
    ("MySQL", "mysql", ["mysql", "--version"], Version(8, 0, 0), "devsetup mysql"),
    ("PostgreSQL", "psql", ["psql", "--version"], Version(14, 0, 0), "devsetup postgres"),
]


SIMPLE_REQUIREMENTS = [
    ("Pip", "pip3", ["pip3", "--version"], "devsetup python"),
    ("NPM", "npm", ["npm", "-v"], "devsetup node"),
    ("VS Code CLI", "code", ["code", "--version"], "Instale o VS Code e habilite o comando code"),
]