from devsetup.core.version import Version, is_version_compatible, parse_version


def test_parse_version_with_major_minor_patch() -> None:
    result = parse_version("Python 3.12.3")

    assert result == Version(3, 12, 3)


def test_parse_version_with_node_version() -> None:
    result = parse_version("v22.11.0")

    assert result == Version(22, 11, 0)


def test_parse_version_with_java_output() -> None:
    result = parse_version('openjdk version "21.0.5" 2024-10-15')

    assert result == Version(21, 0, 5)


def test_parse_version_with_only_major() -> None:
    result = parse_version("version 22")

    assert result == Version(22, 0, 0)


def test_parse_version_returns_none_when_no_version_found() -> None:
    result = parse_version("version unknown")

    assert result is None


def test_version_is_compatible_when_greater_than_minimum() -> None:
    current = Version(22, 1, 0)
    minimum = Version(22, 0, 0)

    assert is_version_compatible(current, minimum) is True


def test_version_is_compatible_when_equal_to_minimum() -> None:
    current = Version(3, 10, 0)
    minimum = Version(3, 10, 0)

    assert is_version_compatible(current, minimum) is True


def test_version_is_not_compatible_when_minor_is_lower() -> None:
    current = Version(3, 9, 9)
    minimum = Version(3, 10, 0)

    assert is_version_compatible(current, minimum) is False


def test_version_is_not_compatible_when_major_is_lower() -> None:
    current = Version(20, 9, 0)
    minimum = Version(22, 0, 0)

    assert is_version_compatible(current, minimum) is False


def test_version_is_compatible_when_patch_is_greater() -> None:
    current = Version(21, 0, 5)
    minimum = Version(21, 0, 0)

    assert is_version_compatible(current, minimum) is True
