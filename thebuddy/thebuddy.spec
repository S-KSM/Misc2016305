# -*- mode: python -*-

block_cipher = None


a = Analysis(['thebuddy.py'],
             pathex=['C:\\Users\\Shobeir\\Desktop\\Fiverr\\20160305\\thebuddy'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='thebuddy',
          debug=False,
          strip=False,
          upx=True,
          console=True )
