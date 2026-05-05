from devsetup.config.validator import validate_config


def test_validate_config_returns_empty_list_for_valid_config() -> None:
    config = {
        "profile": {
            "backend": {"tools": ["system", "git", "python", "node", "postgres"]}
        }
    }

    assert validate_config(config) == []


def test_validate_config_returns_error_when_profile_is_not_dict() -> None:
    config = {"profile": ["backend"]}

    errors = validate_config(config)

    assert errors == ["A seção [profile] deve ser um objeto TOML válido."]


def test_validate_config_returns_error_when_profile_config_is_not_dict() -> None:
    config = {"profile": {"backend": ["system"]}}

    errors = validate_config(config)

    assert "O profile 'backend' deve ser uma tabela TOML." in errors


def test_validate_config_returns_error_when_tools_is_missing() -> None:
    config = {"profile": {"backend": {}}}

    errors = validate_config(config)

    assert "O profile 'backend' precisa declarar 'tools'." in errors


def test_validate_config_returns_error_when_tools_is_not_list() -> None:
    config = {"profile": {"backend": {"tools": "python"}}}

    errors = validate_config(config)

    assert "O campo 'tools' do profile 'backend' deve ser uma lista." in errors


def test_validate_config_returns_error_when_tools_is_empty() -> None:
    config = {"profile": {"backend": {"tools": []}}}

    errors = validate_config(config)

    assert "O profile 'backend' não pode ter lista de tools vazia." in errors


def test_validate_config_returns_error_when_tool_is_not_string() -> None:
    config = {"profile": {"backend": {"tools": ["python", 123]}}}

    errors = validate_config(config)

    assert "O profile 'backend' possui uma tool inválida: 123." in errors


def test_validate_config_returns_error_when_tool_is_not_supported() -> None:
    config = {"profile": {"backend": {"tools": ["docker"]}}}

    errors = validate_config(config)

    assert "Tool 'docker' não suportada no profile 'backend'." in errors
