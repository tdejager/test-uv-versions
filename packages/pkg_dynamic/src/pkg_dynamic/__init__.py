"""Package that exposes a dynamic version via setuptools."""

VERSION = "0.3.1"


def dynamic_message() -> str:
    return f"Dynamic package version {VERSION}"
