from typing import Any


class AutoPyinstallerException(Exception):
    """Generic AutoPyinstaller exception."""

    def __init__(self, msg: str, value: Any) -> None:
        super().__init__()
        self.msg = msg
        self.value = value

    def __str__(self) -> str:
        return f"{self.msg}:{self.value}"


class ExeBuildFromSpecFileError(AutoPyinstallerException):
    """Exception raised when a pyinstaller exe build fails."""

    def __init__(self, msg: str = "An error occurred during the build.", value: Any = None) -> None:
        super().__init__(msg, value)
