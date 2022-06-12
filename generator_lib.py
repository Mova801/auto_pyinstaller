from dataclasses import dataclass
import os


@dataclass
class Generator:
    main: str = None
    pathex: str = None
    pathspec: str = None
    datas: list = None
    hiddenimports: list = None
    name: str = None
    icon: str = None
    spec: str = None

    def __init__(self, main: str,  name: str, **opt: dict) -> None:
        self.main = main + ".py"
        self.pathex = opt.get("pathex", None)
        self.pathspec = opt.get("pathspec", None)
        self.datas = opt.get("datas", [tuple(('', '.'))])
        self.hiddenimports = opt.get("hidden_imports", [])
        self.name = name
        icon = opt.get("icon", "")
        if icon != "":
            self.icon = f",\n icon = '{icon}.ico'"
        else:
            self.icon = ""

    def get_main(self) -> str:
        return self.main

    def get_pathex(self) -> str:
        return self.pathex

    def get_pathspec(self) -> str:
        return self.pathspec

    def get_datas(self) -> list:
        return self.datas()

    def get_hiddenimports(self) -> list:
        return self.hiddenimports

    def get_name(self) -> str:
        return self.name

    def get_icon_name(self):
        return self.icon

    def get_spec(self) -> str:
        return self.spec

    def set_main(self, main: str) -> None:
        self.main = main

    def set_pathex(self) -> None:
        self.pathex = os.path.dirname(os.path.realpath(__file__))
        self.pathex = self.pathex.split('\\')
        self.pathex = [x + '\\\\' for x in self.pathex]
        self.pathex = "".join(self.pathex)

    def spec(self) -> None:
        self.set_pathex()
        self.spec = f"""
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['{self.main}'],
             pathex=['{self.pathex}'],
             binaries=[],
             datas={self.datas},
             hiddenimports={self.hiddenimports},
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
          name='{self.name}',
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
          entitlements_file=None{str(self.icon)} )
          """
        return self.spec

    def exe(self) -> bool:
        try:
            res = os.system(f'cmd /c pyinstaller {self.name}.spec')
            if res == 1:
                return -1
            return 0
        except:
            return -1
