# -*- encoding: utf-8 -*-
__date__ = '2023/12/04 13:00:32'

import tkinter as tk
import time


class ClockWindow(tk.Tk):
    def update_time(self):

        # 获取当前时间的Unix时间戳（精确到秒），再转换成毫秒
        timestamp_ms = int(time.time() * 1000)
        # 格式化输出当前时间（不含微秒精度，通常不直接展示）
        local_time = time.localtime(timestamp_ms / 1000)

        formatted_time = time.strftime("%H:%M:%S", local_time)

        # current_time = f"{formatted_time}:{(timestamp_ms % 1000) // 10 :02d}"
        current_time = f"{formatted_time}"

        self.time_label.config(text=current_time)
        # self.time_label.after(10, self.update_time)
        self.time_label.after(1000, self.update_time)


    # def mytimer(self, event):


    def StartMove(self, event):
        global x, y
        x = event.x
        y = event.y

    def StopMove(self, event):
        global x, y
        x = None
        y = None

    def OnMotion(self, event):
        global x, y
        deltax = event.x - x
        deltay = event.y - y
        self.geometry("+%s+%s" % (self.winfo_x() + deltax, self.winfo_y() + deltay))
        self.update()
        # print(event.x,event.y,self.winfo_x(),self.winfo_y(),self.winfo_width(),self.winfo_height())

    def myquit(self, *args):
        self.destroy()

    def __init__(self):
        super().__init__()
        self.overrideredirect(1)  # 去除窗口边框
        self.wm_attributes("-alpha", 0.8)  # 设置透明度
        self.wm_attributes("-topmost", True)  # 始终处于顶层
        self.title('个性化时钟')
        self.geometry('400x133')
        self.configure(bg='white')
        self.time_label = tk.Label(self, text='', font=('Arial', 66), fg='black', bg='white')
        self.time_label.pack(expand=True)

        self.update_time()
        self.bind("<ButtonPress-1>", self.StartMove)  # 监听左键按下操作响应函数
        self.bind("<ButtonRelease-1>", self.StopMove)  # 监听左键松开操作响应函数
        self.bind("<B1-Motion>", self.OnMotion)  # 监听鼠标移动操作响应函数
        self.bind("<Control-q>", self.myquit)  # 关闭
        # self.bind("<Control-t>", self.mytimer)  # 切换为倒计时


if __name__ == "__main__":
    app = ClockWindow()
    app.mainloop()

