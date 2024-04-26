## 程序概览

直接运行dist文件夹下的main.exe即可

![image-20240426170937446](G:\JetBrains\jetBrain_WorkSpeace\PychamProjects\clock\README\image-20240426170937446.png)

## 程序功能

![image-20240426164916784](G:\JetBrains\jetBrain_WorkSpeace\PychamProjects\clock\README\image-20240426164916784.png)

### Ctrl+T切换至计时功能

![image-20240426164929932](G:\JetBrains\jetBrain_WorkSpeace\PychamProjects\clock\README\image-20240426164929932.png)

### Ctrl+S暂停 

![image-20240426164945004](G:\JetBrains\jetBrain_WorkSpeace\PychamProjects\clock\README\image-20240426164945004.png)

### Ctrl+Q关闭



## 需求环境:

python3.8及以上

## 打包指南

1. 安装PyInstaller：确保已安装PyInstaller库。如果没有安装，可以使用pip进行安装

```python
   pip install pyinstaller
```

2. 准备相关文件：

- 确保存在名为main.py的源代码文件，这是您要打包的主程序。
- 确保存在名为i12.ico的图标文件，用于作为打包后可执行文件的图标

3. 运行打包脚本：

```python
python build_executable.py
```
