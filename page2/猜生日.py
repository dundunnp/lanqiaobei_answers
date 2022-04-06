import os
import sys

# 请在此输入您的代码
flag = False
month = '06'
for y in range(1912, 2012):
    for d in range(1, 31):
        str_d = '0' + str(d) if d < 10 else str(d)
        num = int(str(y) + month + str_d)
        if (num % 2012 == 0 and num % 3 == 0 and num % 12 == 0):
            print(str(y) + month + str_d)
            flag = True
            break
    if flag: break
