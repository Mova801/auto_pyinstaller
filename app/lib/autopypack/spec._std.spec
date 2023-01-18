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
          