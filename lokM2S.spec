# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['lokM2S.py'],
    pathex=[],
    binaries=[],
    datas=[("assets/mel_filters.npz", "whisper/assets"), ("assets/gpt2.tiktoken", "whisper/assets"), ("assets/multilingual.tiktoken", "whisper/assets")],
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
    a.binaries,
    a.datas,
    [],
    name='lokM2S',
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
