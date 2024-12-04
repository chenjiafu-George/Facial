# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['data_utils.py', 'detect_face.py', 'face_replace_MTCNN.py', 'Facial.py', 'plant_identify_1.py', '爬取图片.py', '图片界面.py', '图片界面3.py'],
             pathex=['E:\\Python\\python code\\Facial'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='data_utils',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon1.ico')
