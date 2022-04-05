import os
import sys

"""
方式一：
"""
# 请在此输入您的代码
def count_day(year, month):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


# 星期一为1， 星期日为7
on_Monday = 6
distance = 0
for y in range(2000, 2021):
    month = 12 if y != 2020 else 10
    for m in range(1, month + 1):
        day = 1 if (y == 2020 and m == 10) else count_day(y, m)
        for d in range(1, day + 1):
            if on_Monday == 1 or d == 1:
                distance += 2
            else:
                distance += 1
            on_Monday = (on_Monday % 7) + 1

print(distance)

"""
方式二：
"""
import datetime

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 10, 1)
days = datetime.timedelta(days=1)
result = 0

while start <= end:
    if start.day == 1 or start.weekday() == 0:
        result += 2
    else:
        result += 1
    start += days

print(result)