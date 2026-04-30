import pytest

from devsetup.core import prompt


def test_ask_text_returns_user_input(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda message: "meu_valor")

    result = prompt.ask_text("Digite algo", "default")

    assert result == "meu_valor"


def test_ask_text_returns_default_when_input_is_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda message: "")

    result = prompt.ask_text("Digite algo", "default")

    assert result == "default"


def test_ask_password_returns_user_input(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(prompt, "getpass", lambda message: "senha_segura")

    result = prompt.ask_password("Digite a senha")

    assert result == "senha_segura"


def test_ask_password_returns_default_when_input_is_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(prompt, "getpass", lambda message: "")

    result = prompt.ask_password("Digite a senha", "default_password")

    assert result == "default_password"


def test_confirm_returns_true_when_auto_yes_is_enabled() -> None:
    prompt.set_auto_yes(True)

    assert prompt.confirm("Confirma?") is True

    prompt.set_auto_yes(False)


def test_confirm_returns_true_when_user_answers_s(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    prompt.set_auto_yes(False)
    monkeypatch.setattr("builtins.input", lambda message: "s")

    assert prompt.confirm("Confirma?") is True


def test_confirm_returns_false_when_user_answers_n(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    prompt.set_auto_yes(False)
    monkeypatch.setattr("builtins.input", lambda message: "n")

    assert prompt.confirm("Confirma?") is False


def test_confirm_returns_false_when_user_answers_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    prompt.set_auto_yes(False)
    monkeypatch.setattr("builtins.input", lambda message: "")

    assert prompt.confirm("Confirma?") is False