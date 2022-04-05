import os
import sys

# 请在此输入您的代码
dic = {}
for i in range(10):
    dic[str(i)] = 2021

flag = False

for i in range(1, 20210):
    for j in str(i):
        if dic.get(j) == 0:
            print(i - 1)
            flag = True
            break
        dic[j] -= 1
    if flag:
        break
