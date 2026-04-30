# Dev Setup CLI

CLI para automatizar a configuração inicial de ambiente de desenvolvimento em distribuições Linux dentro do WSL.

## Objetivo

Este projeto centraliza scripts de instalação e configuração usados no setup de ambientes de desenvolvimento, evitando execução manual repetitiva e reduzindo inconsistências entre máquinas.

## Recursos atuais

- Atualização de pacotes do sistema
- Instalação/configuração de Python
- Instalação de `python3-venv`
- Instalação/configuração de Node.js 22
- Instalação/configuração de Java 21 e Maven
- Instalação/configuração de Git
- Instalação/configuração de MySQL
- Instalação/configuração de PostgreSQL
- Criação de projeto Python com `.venv` e `main.py`
- Diagnóstico do ambiente com `doctor`
- Suporte a `--dry-run`
- Suporte a `--yes`

## Requisitos

- Linux/WSL
- Python 3.10+
- `pip`
- Permissão para executar comandos com `sudo`

## Instalação local

```bash
git clone https://github.com/sobraljhonata/dev-setup-cli
cd dev-setup-cli
pip install -e ".[dev]"
```
## Uso
devsetup --help
Comandos disponíveis
Atualizar sistema
devsetup system
Configurar Python
devsetup python
Instalar apenas o venv
devsetup venv
Configurar Node.js
devsetup node
Configurar Java
devsetup java
Configurar Git
devsetup git
Configurar MySQL
devsetup mysql
Configurar PostgreSQL
devsetup postgres
Criar projeto Python
devsetup project minha-poc

## O projeto será criado em:
```bash
~/Projetos/minha-poc
```

## Com a estrutura inicial:

minha-poc/
├── main.py
└── .venv/

## Diagnosticar ambiente
```bash
devsetup doctor
```
### O comando verifica ferramentas, versões mínimas e serviços.

## Versões mínimas atuais:

```text
Ferramenta	Versão mínima
Python	3.10.0
Node.js	22.0.0
Java	21.0.0
Maven	3.8.0
Git	2.34.0
MySQL	8.0.0
PostgreSQL	14.0.0
Opções globais
Dry-run
```

## Mostra os comandos sem executar:

devsetup --dry-run system
devsetup --dry-run --yes all
Yes

Confirma automaticamente ações interativas:

devsetup --yes system

Atalho:

devsetup -y system
Setup completo
devsetup all

Esse comando executa:

system
python
node
java
git
mysql
postgres
Testes

Instalar dependências de desenvolvimento:

pip install -e ".[dev]"

Rodar testes:

pytest

Rodar testes com cobertura:

pytest --cov --cov-report=term-missing
Estrutura do projeto
dev-setup-cli/
├── devsetup/
│   ├── cli.py
│   ├── doctor.py
│   ├── config/
│   │   └── requirements.py
│   ├── core/
│   │   ├── checks.py
│   │   ├── prompt.py
│   │   ├── shell.py
│   │   └── version.py
│   ├── installers/
│   │   ├── git.py
│   │   ├── java.py
│   │   ├── mysql.py
│   │   ├── node.py
│   │   ├── postgres.py
│   │   ├── python.py
│   │   ├── system.py
│   │   └── venv.py
│   └── project/
│       └── python_project.py
├── tests/
├── pyproject.toml
└── README.md
Segurança

Este CLI executa comandos com sudo.

Antes de executar comandos sensíveis, recomenda-se usar:

devsetup --dry-run <comando>

Exemplo:

devsetup --dry-run mysql
Roadmap
Testes para installers
Testes para CLI com Typer CliRunner
Melhorias no doctor
Suporte a Docker
Suporte a SDKMAN
Suporte a criação de projetos Java/Spring Boot
Suporte a criação de projetos Node.js/TypeScript
Configuração via arquivo .devsetup.toml