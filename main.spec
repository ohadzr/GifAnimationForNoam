# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Ohad\\PycharmProjects\\PagmarNoamReuven'],
             binaries=[('C:\\Users\\Ohad\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\opencv_ffmpeg410_64.dll','.')],
             datas=[('C:\\Users\\Ohad\\PycharmProjects\\PagmarNoamReuven\\config.py','.')],
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
          name='PagmarNoamReuven',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
