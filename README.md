# Dev Setup CLI

CLI para automatizar a configuração inicial de ambientes de desenvolvimento em distribuições Linux (WSL).

---

## 🎯 Objetivo

Centralizar scripts de instalação e configuração usados no setup de ambientes de desenvolvimento, evitando execução manual repetitiva e reduzindo inconsistências entre máquinas.

---

## 🚀 Recursos

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

---

## ⚙️ Requisitos

- Linux / WSL
- Python 3.10+
- `pip`
- Permissão para executar comandos com `sudo`

---

## 📦 Instalação

### Local (modo desenvolvimento)

```bash
git clone https://github.com/sobraljhonata/dev-setup-cli
cd dev-setup-cli
pip install -e ".[dev]"
```

---

## ▶️ Uso

```bash
devsetup --help
```

---

## 🧩 Comandos

### Sistema

```bash
devsetup system
```

### Python

```bash
devsetup python
devsetup venv
```

### Node.js

```bash
devsetup node
```

### Java

```bash
devsetup java
```

### Git

```bash
devsetup git
```

### Banco de dados

```bash
devsetup mysql
devsetup postgres
```

### Criar projeto Python

```bash
devsetup project minha-poc
```

O projeto será criado em:

```bash
~/Projetos/minha-poc
```

Estrutura:

```text
minha-poc/
├── main.py
└── .venv/
```

---

## 🩺 Diagnóstico do ambiente

```bash
devsetup doctor
```

O comando verifica:

- Ferramentas instaladas
- Versões mínimas
- Status de serviços

---

## 📊 Versões mínimas

| Ferramenta  | Versão mínima |
|------------|--------------:|
| Python     | 3.10.0 |
| Node.js    | 22.0.0 |
| Java       | 21.0.0 |
| Maven      | 3.8.0 |
| Git        | 2.34.0 |
| MySQL      | 8.0.0 |
| PostgreSQL | 14.0.0 |

---

## ⚡ Opções globais

### Dry-run

Mostra os comandos sem executar:

```bash
devsetup --dry-run system
devsetup --dry-run --yes all
```

### Yes

Confirma automaticamente ações interativas:

```bash
devsetup --yes system
devsetup -y system
```

---

## 🏁 Setup completo

```bash
devsetup all
```

Executa:

```text
system
python
node
java
git
mysql
postgres
```

---

## 🧪 Testes

Instalar dependências:

```bash
pip install -e ".[dev]"
```

Rodar testes:

```bash
pytest
```

Cobertura:

```bash
pytest --cov --cov-report=term-missing
```

---

## 🏗️ Estrutura do projeto

```text
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
```

---

## 🔒 Segurança

Este CLI executa comandos com `sudo`.

Recomendado usar:

```bash
devsetup --dry-run <comando>
```

Exemplo:

```bash
devsetup --dry-run mysql
```

---

## 🛣️ Roadmap

- [ ] Testes para installers
- [ ] Testes para CLI com Typer CliRunner
- [ ] Melhorias no `doctor`
- [ ] Suporte a Docker
- [ ] Suporte a SDKMAN
- [ ] Criação de projetos Java/Spring Boot
- [ ] Criação de projetos Node.js/TypeScript
- [ ] Configuração via `.devsetup.toml`

---

## 🤝 Contribuição

Veja o arquivo `CONTRIBUTING.md`.

---

## 📄 Licença

MIT
