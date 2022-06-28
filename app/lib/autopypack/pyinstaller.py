from asyncio import subprocess
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from LIB.ios.iostream import sanitize_string


@dataclass
class FileContainer(ABC):
    """Represents a file data container."""

    __slots__ = ["_filename", "_path", "_data"]

    @abstractmethod
    def validate_path(self) -> bool:
        """Checks if the given Path is valid or not."""

    @abstractmethod
    def validate_filename(self) -> bool:
        """Checks if the given filename is valid or not."""

    @abstractmethod
    def write(self) -> bool:
        """Create a new file."""


@dataclass
class SpecFile(FileContainer):
    """Represents a spec file."""

    __slots__ = ["_main_module", "_hidden_imports", "_pathex" "_icon", "_spec_str"]

    def __init__(self, filename: str, main_module: str = "main.py", pathexe: Path = "", data: tuple = ('', '.'), hidden_imports: Optional[tuple[str]] = (), use_console: bool = True, icon: Optional[Path|str] = "") -> None:
        if not filename.endswith('.spec'):
            filename + '.spec'
        if not main_module.endswith('.py'):
            main_module + '.py'
        self._main_module = main_module
        self._pathex = pathexe
        self._hidden_imports = hidden_imports
        if icon != "" and not icon.endswith('.ico'):
            icon = ""
        if use_console:
            self._use_console: str = "True"
        else:
            self._use_console: str = "False"
        self._icon = icon
        self._spec = None
        super.__init__(filename, pathexe, data)

    def write(self) -> bool:
        """Write a spec str on a .spec file."""
        if not self._spec:
            return False
        with open(self._path, 'w') as file:
            file.write(self._spec)
        return True

    def build_spec_str(self) -> str:
        """Generate a spec str."""
        self._spec = f"""
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['{self._main_module}'],
             pathex=['{self._pathex}'],
             binaries=[],
             datas={self._data},
             hiddenimports={self._hidden_imports},
             hookspath=[],
             hooksconfig={{}},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          module_name='{self._module_name}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console={self._use_console},
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='{str(self._icon)}')
          """
        return self._spec


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
            result = subprocess.run(
                ['pyinstaller', f'{self.__spec._filename()}'])
            # res = os.system(f'cmd /c pyinstaller {self._module_name}.spec')
        except ExeBuildFromSpecFileError:
            return -1
        else:
            if result:
                return -1
            return 0
