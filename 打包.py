import PyInstaller.__main__

PyInstaller.__main__.run([
    '4.py',
    '--onefile',  # 打包成一个单独的可执行文件
    '--noconsole',  # 不显示控制台窗口（对于GUI应用程序）
    '--icon=i11.ico'
])
# pyinstaller 4.py --onefile --noconsole --icon=i12.ico
