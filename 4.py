import tkinter as tk
import time

class ClockWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(1)  # 去除窗口边框
        self.wm_attributes("-alpha", 0.9)  # 设置透明度
        self.wm_attributes("-topmost", True)  # 始终处于顶层
        self.title('个性化时钟')
        self.geometry('400x133')
        self.configure(bg='#2C3E50')  # 设置背景颜色
        self.mode = 'clock'  # 初始模式为时钟模式
        self.time_label = tk.Label(self, text='', font=('Helvetica', 48), fg='#ECF0F1', bg='#2C3E50')  # 设置字体和颜色
        self.time_label.pack(expand=True)
        self.update_time()
        self.timer_running = False  # 计时器状态
        self.timer_start_time = 0  # 计时器开始时间
        self.bind("<ButtonPress-1>", self.StartMove)  # 监听左键按下操作响应函数
        self.bind("<ButtonRelease-1>", self.StopMove)  # 监听左键松开操作响应函数
        self.bind("<B1-Motion>", self.OnMotion)  # 监听鼠标移动操作响应函数
        self.bind("<Control-q>", self.myquit)  # 关闭
        self.bind("<Control-t>", self.toggle_mode)  # 切换模式

    def update_time(self):
        timestamp_ms = int(time.time() * 1000)
        local_time = time.localtime(timestamp_ms / 1000)
        formatted_time = time.strftime("%H:%M:%S", local_time)
        if self.mode == 'clock':
            self.time_label.config(text=formatted_time)
        elif self.mode == 'timer':
            if self.timer_running:
                elapsed_time = timestamp_ms - self.timer_start_time
                hours, remainder = divmod(elapsed_time // 1000, 3600)
                minutes, seconds = divmod(remainder, 60)
                formatted_timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                self.time_label.config(text=formatted_timer)
        self.time_label.after(1000, self.update_time)

    def toggle_mode(self, event):
        if self.mode == 'clock':
            self.mode = 'timer'
            self.timer_running = True  # 开始计时
            self.timer_start_time = int(time.time() * 1000)  # 记录开始时间
        else:
            self.mode = 'clock'
            self.timer_running = False  # 停止计时
        self.update_time()  # 更新显示

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

    def myquit(self, *args):
        self.destroy()

app = ClockWindow()
app.mainloop()
