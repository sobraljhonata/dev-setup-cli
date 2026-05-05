# Dev Setup CLI

![CI](https://github.com/sobraljhonata/dev-setup-cli/actions/workflows/ci.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/dev-setup-cli-jhonata)
![Python](https://img.shields.io/pypi/pyversions/dev-setup-cli-jhonata)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## 🔗 Links

- PyPI: https://pypi.org/project/dev-setup-cli-jhonata
- GitHub: https://github.com/sobraljhonata/dev-setup-cli

---

## 📌 Status

🚧 Em evolução ativa  
✔ CLI funcional  
✔ Publicado no PyPI  
✔ Pipeline de CI/CD configurado  

---

## 🚀 Por que usar?

Provisionar ambiente de desenvolvimento manualmente é lento, inconsistente e propenso a erro.

❌ 1–2 horas de setup manual  
✔ em poucos minutos com um comando

```bash
devsetup profile backend
```

---

## ⚡ Quickstart

### Instalar

```bash
pip install dev-setup-cli-jhonata
```

Ou com pipx (recomendado):

```bash
pipx install dev-setup-cli-jhonata
```

### Executar

```bash
devsetup profile backend
```

---

## 🧠 Profiles (principal feature)

```bash
devsetup profile backend
devsetup profile frontend
devsetup profile fullstack
devsetup profile python
```

### 📊 O que cada profile faz

| Profile   | Instala/configura                                |
|----------|------------------------------------------------|
| backend  | system, git, python, node, java, postgres        |
| frontend | system, git, node                                |
| fullstack| system, git, python, node, java, mysql, postgres |
| python   | system, git, python                              |

---

## 🎯 Casos de uso

### Backend Developer
```bash
devsetup profile backend
```

### Frontend Developer
```bash
devsetup profile frontend
```

### Fullstack Developer
```bash
devsetup profile fullstack
```

### Ensino / Bootcamps
Ambiente padronizado para turmas e onboarding.

---

## 🧩 Comandos

```bash
devsetup system
devsetup python
devsetup node
devsetup java
devsetup git
devsetup mysql
devsetup postgres
```

---

## 🏗️ Criar projeto Python

```bash
devsetup project minha-poc
```

Estrutura:

```text
~/Projetos/minha-poc
├── main.py
└── .venv/
```

---

## 🩺 Diagnóstico do ambiente

```bash
devsetup doctor
```

---

## ⚡ Flags globais

```bash
devsetup --dry-run <comando>
devsetup --yes <comando>
```

---

## 📊 Versões mínimas

| Ferramenta  | Versão mínima |
|------------|--------------:|
| Python     | 3.10 |
| Node.js    | 22 |
| Java       | 21 |
| Maven      | 3.8 |
| Git        | 2.34 |
| MySQL      | 8 |
| PostgreSQL | 14 |

---

## 🧪 Testes

```bash
pytest
pytest --cov --cov-report=term-missing
```

---

## 🏗️ Arquitetura

- Core desacoplado (execução, validação)
- Installers isolados
- Profiles como orquestração
- CLI baseado em Typer

---

## 🔒 Segurança

Este CLI executa comandos com sudo.

```bash
devsetup --dry-run <comando>
```

---

## 🛣️ Roadmap

- [ ] Profiles configuráveis via `.devsetup.toml`
- [ ] Testes para installers
- [ ] Suporte a Docker
- [ ] Templates de projetos

---

## 🤝 Contribuição

Veja `CONTRIBUTING.md`.

---

## 📄 Licença

MIT
