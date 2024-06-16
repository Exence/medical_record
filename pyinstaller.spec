# build_script.spec

# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_all

current_working_directory = os.getcwd()

block_cipher = None

a = Analysis(['main.py'],
             pathex=['current_working_directory'],
             binaries=[],
             datas=[('static', 'static'), ('templates', 'templates'), ('medical_record.db','.')],
             hiddenimports=['main', 'uvicorn', 'fastapi'],
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
          exclude_binaries=True,
          name='MedicalRecord',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MedicalRecord')
