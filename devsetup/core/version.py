import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    major: int
    minor: int = 0
    patch: int = 0

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def parse_version(output: str) -> Version | None:
    match = re.search(r"(\d+)(?:\.(\d+))?(?:\.(\d+))?", output)

    if not match:
        return None

    major = int(match.group(1))
    minor = int(match.group(2) or 0)
    patch = int(match.group(3) or 0)

    return Version(major, minor, patch)


def is_version_compatible(current: Version, minimum: Version) -> bool:
    return (
        current.major,
        current.minor,
        current.patch,
    ) >= (
        minimum.major,
        minimum.minor,
        minimum.patch,
    )
