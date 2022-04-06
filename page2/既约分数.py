import os
import sys
import math

# 请在此输入您的代码
# 保存既约分数的列表
target_list = []
# 判断是否是既约分数
"""
方式一：辗转相除法
"""
def is_target1(i, j):
    if (j > i):
        i, j = j, i
    while (j != 0):
        tmp = i % j
        i = j
        j = tmp
    return i == 1
"""
方式二：调用math.gcd直接返回最大公约数
"""
def is_target2(i, j):
    return True if math.gcd(i, j) == 1 else False
# 分子
for i in range(1, 2021):
    # 分母
    for j in range(1, 2021):
        if is_target2(i, j):
            target_list.append(i / j)
print(len(set(target_list)))