import tkinter as tk
import time


class DesktopClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Clock")
        self.current_window = None

        # 创建按钮
        self.time_button = tk.Button(root, text="显示时间", command=self.show_time)
        self.time_button.pack(pady=10)
        self.countdown_button = tk.Button(root, text="倒计时", command=self.show_countdown)
        self.countdown_button.pack(pady=10)
        self.timer_button = tk.Button(root, text="计时器", command=self.show_timer)
        self.timer_button.pack(pady=10)

        # 创建标签
        self.label = tk.Label(root, font=("Arial", 24))
        self.label.pack()

    def show_time(self):
        self.label.config(text="")
        self.current_window = "time"
        self.update_time()

    def show_countdown(self):
        self.label.config(text="")
        self.current_window = "countdown"
        self.update_countdown(60)

    def show_timer(self):
        self.label.config(text="")
        self.current_window = "timer"
        self.start_timer()

    def update_time(self):
        if self.current_window == "time":
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.label.config(text=current_time)
            self.root.after(1000, self.update_time)

    def update_countdown(self, seconds):
        if self.current_window == "countdown":
            if seconds >= 0:
                self.label.config(text=f"倒计时: {seconds} 秒")
                self.root.after(1000, self.update_countdown, seconds - 1)

    def start_timer(self):
        if self.current_window == "timer":
            self.timer_start_time = time.time()
            self.update_timer()

    def update_timer(self):
        if self.current_window == "timer":
            elapsed_time = int(time.time() - self.timer_start_time)
            self.label.config(text=f"计时器: {elapsed_time} 秒")
            self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    clock = DesktopClock(root)
    root.mainloop()
