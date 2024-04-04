# -*- encoding: utf-8 -*-
__date__ = '2023/12/04 13:00:32'

import tkinter as tk
import time


class ClockWindow(tk.Tk):
    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)

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

    def mytimer(self, event):
        current_time = time.strftime("%Y-%m-%d%H:%M:%S")
        self.time_label.config(text=current_time)
        # self.time_label.after(1000, self.update_time)

    def __init__(self):
        super().__init__()
        self.overrideredirect(1)  # 去除窗口边框
        self.wm_attributes("-alpha", 0.8)  # 设置透明度
        self.wm_attributes("-topmost", True)  # 始终处于顶层
        self.title('个性化时钟')
        self.geometry('400x133')
        self.configure(bg='black')
        self.time_label = tk.Label(self, text='', font=('Arial', 66), fg='white', bg='black')
        self.time_label.pack(expand=True)

        self.update_time()
        self.bind("<ButtonPress-1>", self.StartMove)  # 监听左键按下操作响应函数
        self.bind("<ButtonRelease-1>", self.StopMove)  # 监听左键松开操作响应函数
        self.bind("<B1-Motion>", self.OnMotion)  # 监听鼠标移动操作响应函数
        self.bind("<Control-q>", self.myquit)  # 关闭
        self.bind("<Control-t>", self.mytimer)  # 切换为倒计时


if __name__ == "__main__":
    app = ClockWindow()
    app.mainloop()

    # def start_timer(self):
    #     if self.current_window == "timer":
    #         self.timer_start_time = time.time()
    #         self.update_timer()
    #
    # def update_timer(self):
    #     if self.current_window == "timer":
    #         elapsed_time = int(time.time() - self.timer_start_time)
    #         self.label.config(text=f"计时器: {elapsed_time} 秒")
    #         self.root.after(1000, self.update_timer)
