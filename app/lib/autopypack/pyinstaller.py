from asyncio import subprocess
from .file import SpecFile


class ExeBuildFromSpecFileError(Exception):
    """Exception raised when a pyinstaller exe build fails."""


class PyInstaller:
    """Allow to generate a .exe file from a .py."""

    __slots__ = ["__spec"]

    def __init__(self, spec: SpecFile) -> None:
        self.__spec: SpecFile = spec

    def build_exe_from_spec(self):
        """Generate a .exe file."""
        try:
            result = subprocess.run(["pyinstaller", f"{self.__spec._filename()}"])
            # res = os.system(f'cmd /c pyinstaller {self._module_name}.spec')
        except ExeBuildFromSpecFileError:
            return -1
        else:
            if result:
                return -1
            return 0
