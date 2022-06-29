from dataclasses import dataclass
from typing import Optional


def write_file_to_disk(file_name: str, data: str | list) -> bool:
    """Write data into a file."""
    if not file_name:
        return False
    with open(file_name, "w") as file:
        file.write(data)
    return True


@dataclass
class SpecFile:
    """Represents a spec file."""

    _file_name: str = ".py"
    _main_module: str = "main.py"
    _pathex: str = ""
    _data: tuple[str, str] = ("", ".")
    _hidden_imports: tuple = ()
    _icon: Optional[str] = ""
    _spec: str = None 

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
