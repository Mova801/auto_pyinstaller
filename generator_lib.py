from dataclasses import dataclass
import os


@dataclass
class Pyinstaller:

    __spec__: str
    
    def __init__(self, main_module: str,  module_name: str, **kwargs: dict) -> None:
        self._main_module = main_module + ".py"
        self._pathex = kwargs.get("pathex", None)
        self._pathspec = kwargs.get("pathspec", None)
        self._datas = kwargs.get("datas", [tuple(('', '.'))])
        self._hiddenimports = kwargs.get("hidden_imports", [])
        self._module_name = module_name
        icon = kwargs.get("icon", "")
        if icon != "":
            self._icon = f",\n icon = '{icon}.ico'"
        else:
            self._icon = ""

    @property
    def main_module(self) -> str:
        return self._main_module

    @property
    def pathex(self) -> str:
        return self._pathex

    @property
    def pathspec(self) -> str:
        return self._pathspec

    @property
    def datas(self) -> list:
        return self._datas()

    @property
    def hiddenimports(self) -> list:
        return self._hiddenimports

    @property
    def module_name(self) -> str:
        return self._module_name

    @property
    def icon_module_name(self):
        return self._icon

    @property
    def spec(self) -> str:
        return self._spec

    @main_module.setter
    def main_module(self, main_module: str) -> None:
        self._main_module = main_module

    @pathex.setter
    def pathex(self) -> None:
        self._pathex = os.path.dirname(os.path.realpath(__file__))
        self._pathex = self._pathex.split('\\')
        self._pathex = [x + '\\\\' for x in self._pathex]
        self._pathex = "".join(self._pathex)

    def build_spec(self) -> None:
        self._set_pathex()
        self._spec = f"""
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['{self._main_module}'],
             pathex=['{self._pathex}'],
             binaries=[],
             datas={self._datas},
             hiddenimports={self._hiddenimports},
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
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None{str(self._icon)} )
          """
        return self._spec

    def build_exe(self) -> bool:
        try:
            res = os.system(f'cmd /c pyinstaller {self._module_name}.spec')
            if res == 1:
                return -1
            return 0
        except:
            return -1
