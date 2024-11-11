import tkinter as tk
import time
from datetime import datetime

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
        self.paused_time = 0  # 暂停时的时间
        self.x = self.y = 0  # 初始化鼠标位置
        self.bind("<ButtonPress-1>", self.StartMove)  # 监听左键按下操作响应函数
        self.bind("<ButtonRelease-1>", self.StopMove)  # 监听左键松开操作响应函数
        self.bind("<B1-Motion>", self.OnMotion)  # 监听鼠标移动操作响应函数
        self.bind("<Control-q>", self.myquit)  # 关闭
        self.bind("<Control-t>", self.toggle_mode)  # 切换模式
        self.bind("<Control-s>", self.toggle_timer)  # 暂停/继续计时器

        # 定义目标日期
        self.target_dates = {
            "预报名": datetime(2024, 10, 9),
            "正式报名": datetime(2024, 10, 15),
            "初试开始": datetime(2024, 12, 20),
        }

    def update_time(self):
        timestamp_ms = int(time.time() * 1000)
        local_time = time.localtime(timestamp_ms / 1000)
        formatted_time = time.strftime("%H:%M:%S", local_time)
        if self.mode == 'clock':
            self.time_label.config(text=formatted_time, font=('Helvetica', 48))
        elif self.mode == 'timer':
            if self.timer_running:
                current_time = timestamp_ms if self.paused_time == 0 else self.paused_time
                elapsed_time = current_time - self.timer_start_time
                hours, remainder = divmod(elapsed_time // 1000, 3600)
                minutes, seconds = divmod(remainder, 60)
                formatted_timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                self.time_label.config(text=formatted_timer, font=('Helvetica', 48))
        elif self.mode == 'countdown':
            self.update_countdown()
        self.time_label.after(1000, self.update_time)

    def update_countdown(self):
        today = datetime.now()
        countdown_texts = []
        for event, date in self.target_dates.items():
            days_left = (date - today).days + 1
            if days_left > 0:
                countdown_texts.append(f"距离{event} 还有 {days_left} 天")
            elif days_left == 0:
                countdown_texts.append(f"{event} 今天进行")
            else:
                countdown_texts.append(f"{event} 已经结束")
        self.time_label.config(text="\n".join(countdown_texts), font=('KaiTi', 19), justify='left')

    def toggle_mode(self, event):
        if self.mode == 'clock':
            self.mode = 'timer'
            self.timer_running = True  # 开始计时
            self.timer_start_time = int(time.time() * 1000)  # 记录开始时间
        elif self.mode == 'timer':
            self.mode = 'countdown'
        else:
            self.mode = 'clock'
            self.timer_running = False  # 停止计时
        self.update_time()  # 更新显示

    def toggle_timer(self, event):
        if self.timer_running:
            self.paused_time = int(time.time() * 1000)
            self.timer_running = False
        else:
            if self.paused_time != 0:
                self.timer_start_time += int(time.time() * 1000) - self.paused_time
                self.paused_time = 0
            else:
                self.timer_start_time = int(time.time() * 1000)
            self.timer_running = True
        self.update_time()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        self.geometry("+%s+%s" % (self.winfo_x() + deltax, self.winfo_y() + deltay))

    def myquit(self, *args):
        self.destroy()

app = ClockWindow()
app.mainloop()
