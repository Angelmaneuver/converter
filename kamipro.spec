# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('./converter/batch/translator/config', 'config'),
]

a = Analysis(['kamipro.py'],
             pathex=['C:\\Users\\angelmaneuver\\PycharmProjects\\converter'],
             binaries=[],
             datas=added_files,
             hiddenimports=['pkg_resources.py2_warn'],
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
          name='神プロ エピソード一覧作成',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
