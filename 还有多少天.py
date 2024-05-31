from datetime import datetime, timedelta

# 定义目标日期
target_dates = {
    "预报名开始": datetime(2024, 9, 24),
    "正式报名开始": datetime(2024, 10, 8),
    "初试开始": datetime(2024, 12, 23),
}

# 获取当前日期
today = datetime.now()

# 计算并显示倒计时
for event, date in target_dates.items():
    days_left = (date - today).days
    if days_left > 0:
        print(f"距离{event}还有 {days_left} 天")
    elif days_left == 0:
        print(f"{event} 今天进行")
    else:
        print(f"{event} 已经结束")

