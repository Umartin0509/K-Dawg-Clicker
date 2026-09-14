# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['K_dawg.py'],
    pathex=[],
    binaries=[],
    datas=[('KDawg_pic.png', '.'), ('KDawg_pic.jpg', '.'), ('KDawg_pic.tif', '.'), ('KDawg_pic.jxr', '.'), ('KDawg_pic.heic', '.'), ('KDawg_pic.bmp', '.'), ('crash_screen.png', '.'), ('05. Loonboon.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='K_dawg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='K_dawg',
)
