```python
# 导入time模块
import time

# 设置专注时长（分钟）
focus_time = 25

# 设置休息时长（分钟）
break_time = 5

# 设置专注次数
focus_count = 4

# 定义一个计时器函数
def timer(minute):
# 将分钟转换为秒
second = minute * 60
# 循环计时
while second > 0:
# 打印剩余时间
print(f"{second // 60}:{second % 60}")
# 每秒减一
second -= 1
# 延迟一秒
time.sleep(1)

# 定义一个专注时钟函数
def focus_clock():
# 初始化专注次数
count = 0
# 循环专注和休息
while count < focus_count:
# 开始专注
print("开始专注")
timer(focus_time)
# 增加专注次数
count += 1
# 判断是否完成所有专注
if count == focus_count:
# 结束程序
print("恭喜你完成了所有专注")
break
# 开始休息
print("开始休息")
timer(break_time)

# 调用专注时钟函数
focus_clock()
```