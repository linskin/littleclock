## 3.0新增
![img.png](img.png)

迷你小时钟，适合coding时使用

直接运行dist文件夹下的clock_3_0.exe即可

## 2.0新增
![image](https://github.com/linskin/littleclock/assets/110439527/b49c61b7-e5ae-48c1-accd-16e533b2bf86)

直接运行dist文件夹下的clock_2_0.exe即可

### 如何自定义
![image](https://github.com/linskin/littleclock/assets/110439527/2580bae2-fecc-4eac-93f2-0f88c096670b)


更改clock_2_0.py中图示位置代码即可


## 程序概览

直接运行dist文件夹下的main.exe即可

![image-20240426170937446](https://github.com/linskin/littleclock/assets/110439527/682e42cd-6502-49c1-b7d4-1be0445ee2f3)

## 程序功能

![image](https://github.com/linskin/littleclock/assets/110439527/f9a76ec1-f6b3-4cc6-98e1-05de479dbb8c)

### Ctrl+T切换至计时功能

![image-20240426164929932](https://github.com/linskin/littleclock/assets/110439527/00579085-0ae0-4cb1-b9f3-9bca1bdb767f)

### Ctrl+S暂停 

![image-20240426164945004](https://github.com/linskin/littleclock/assets/110439527/c0600003-e4e7-4cac-b530-593948078faa)

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
