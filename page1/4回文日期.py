import os
import sys

"""
方法一：
"""
# 请在此输入您的代码
date = input()
# 表示年的个位和十位
year2 = int(date[2:4])
# 表示年的百位和千位
year1 = int(date[:2])
month = int(date[4:6])
day = int(date[6:])
# 对应year2的每个合法取值，并按时间训练排序
month_list = [str(i)[::-1] if i > 9 else str(i) + "0" for i in range(1, 13)]
month_list.sort(key=lambda x: int(x))
# 对应year1的每个合法取值，并按时间训练排序
day_list = [str(i)[::-1] if i > 9 else str(i) + "0" for i in range(1, 32)]
day_list.sort(key=lambda x: int(x))
# 细节：由于每个月份的是不同的日，所以还要判断
def legal(year, month, day):
    if month == "02":
        if (int(year) % 100) != 0 and (int(year) % 4) == 0:
            return True if 1 <= int(day) <= 29 else False
        else:
            return True if 1 <= int(day) <= 28 else False
    elif month in ["01", "03", "05", "07", "08", "10", "12"]:
        return True if 1 <= int(day) <= 31 else False
    elif month in ["04", "06", "09", "11"]:
        return True if 1 <= int(day) <= 30 else False
    else:
        return False


# 打印回文日期
for i in day_list:
    ### 比较优先级由大到小 year1 -> year2 -> month -> day
    # 比较year前两位
    # 如果相等
    if int(i) == year1:
        # 如果此时year2对应的month大于当前的month
        if int(date[2:4][::-1]) > month and legal(i + date[2:4], date[2:4][::-1], i[::-1]):
            print(i + date[2:4] + date[2:4][::-1] + i[::-1])
            break
        # 如果此时year2对应的month等于当前的month
        # year1对应的day大于当前的day
        elif (
            (int(date[2:4][::-1]) == month) and (int(i[::-1]) > day) and legal(i + date[2:4], date[2:4][::-1], i[::-1])
        ):
            print(i + date[2:4] + date[2:4][::-1] + i[::-1])
            break
        # 否则需要修改year2
        else:
            flag = False
            # 找到比当前year2大的
            for j in month_list:
                if int(j) > year2 and legal(i + j, j[::-1], i[::-1]):
                    flag = True
                    print(i + j + j[::-1] + i[::-1])
                    break
            if flag:
                break
    # 如果大于，year2直接取最小即可
    elif int(i) > year1 and legal(i + month_list[0], month_list[0][::-1], i[::-1]):
        print(i + month_list[0] + month_list[0][::-1] + i[::-1])
        break

# 打印ABABBABA型的回文日期
# 候选日期只有month_list
for j in month_list:
    if int(j) == year1:
        if (int(j) > year2) and legal(j + j, j[::-1], j[::-1]):
            print(j + j + j[::-1] + j[::-1])
            break
        elif int(j) == year2:
            if (int(j[::-1]) > month) and legal(j + j, j[::-1], j[::-1]):
                print(j + j + j[::-1] + j[::-1])
                break
            elif (int(j[::-1]) == month and int(j[::-1]) > day) and legal(j + j, j[::-1], j[::-1]):
                print(j + j + j[::-1] + j[::-1])
                break
    elif int(j) > year1 and legal(j + j, j[::-1], j[::-1]):
        print(j + j + j[::-1] + j[::-1])
        break
    
    
"""
方式二：
"""
import datetime

now_time = input()
time = datetime.datetime(int(now_time[:4]), int(now_time[4:6]), int(now_time[6:]))
days = datetime.timedelta(days=1)
# 是否打印出回文数
flag_result1 = False
# 是否打印出ABABBABA型的回文日期
flag_result2 = False

# 给小于10的整数补0的函数
def my_str(n):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)
  
while not flag_result1 or not flag_result2:
    time += days
    if (str(time.year)[::-1] == (my_str(time.month) + my_str(time.day))):
        if not flag_result1:
            flag_result1 = True
            print(str(time.year) + str(time.year)[::-1])
        if (str(time.year)[0] == str(time.year)[2] and str(time.year)[1] == str(time.year)[3]):
            if not flag_result2:
                flag_result2 = True
                print(str(time.year) + str(time.year)[::-1])