# -*- mode: python ; coding: utf-8 -*-

import wcwidth

block_cipher = None


a = Analysis(['iart-export.py', 'iart-export.spec'],
             pathex=['/Users/edd/PythonVenvs/rep-tool/PyInstaller/export'],
             binaries=[],
             datas=[
                 (os.path.dirname(wcwidth.__file__), 'wcwidth')                 
                 ],
             hiddenimports=['wcwidth'],
             hookspath=[],
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
          name='iart-export',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
