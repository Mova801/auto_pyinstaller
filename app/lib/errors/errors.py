from typing import Optional
from lib.autopypack.file import SpecFile

class PyinstallerException(Exception):
    ...


class ExeBuildFromSpecFileError(PyinstallerException):
    """Exception raised when a pyinstaller exe build fails."""

    def __init__(
        self,
        message: str,
        spec_file: Optional[SpecFile],
    ) -> None:
        super().__init__(message)
        self.message = message
        self.spec_file = spec_file
