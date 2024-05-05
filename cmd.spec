# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.utils.hooks import collect_submodules

datas = [('bin/_internal/audio', 'audio'), ('bin/_internal/font', 'font'), ('bin/_internal/image', 'image'), ('bin/_internal/app', 'app'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\ursina', 'usina/'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\ursina-7.0.0.dist-info', 'ursina-7.0.0.dist-info'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\panda3d', 'panda3d'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\panda3d-1.10.14.dist-info', 'panda3d-1.10.14.dist-info'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\panda3d_tools', 'panda3d_tools'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\direct', 'direct'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\pipeline', 'pipeline'), ('C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\pipeline-0.1.0.dist-info', 'pipeline-0.1.0.dist-info')]
binaries = []
hiddenimports = []
datas += collect_data_files('panda3d')
datas += collect_data_files('ursina')
datas += collect_data_files('panda3d-1.10.14.dist-info')
datas += collect_data_files('ursina-7.0.0.dist-info')
binaries += collect_dynamic_libs('panda3d')
binaries += collect_dynamic_libs('ursina')
binaries += collect_dynamic_libs('panda3d-1.10.14.dist-info')
binaries += collect_dynamic_libs('ursina-7.0.0.dist-info')
hiddenimports += collect_submodules('panda3d')
hiddenimports += collect_submodules('ursina')
hiddenimports += collect_submodules('panda3d-1.10.14.dist-info')
hiddenimports += collect_submodules('ursina-7.0.0.dist-info')


a = Analysis(
    ['C:\\Users\\leonm\\PycharmProjects\\leonsystem\\bin\\cmd.py'],
    pathex=['C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\panda3d', 'C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\ursina', 'C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\ursina-7.0.0.dist-info', 'C:\\Users\\leonm\\PycharmProjects\\leonsystem\\venv\\Lib\\site-packages\\panda3d-1.10.14.dist-info'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
    name='cmd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\leonm\\PycharmProjects\\leonsystem\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cmd',
)
