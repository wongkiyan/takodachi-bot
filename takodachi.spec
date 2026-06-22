# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\takodachi_bot\\takodachi.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/icon_logo.png', 'assets'),
        ('src/takodachi_bot/library/logger_exe.conf', 'library')
    ],
    hiddenimports=['comtypes', 'pycaw', 'pystray._win32', 'psutil'],
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
    a.binaries,
    a.datas,
    [],
    name='takodachi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
