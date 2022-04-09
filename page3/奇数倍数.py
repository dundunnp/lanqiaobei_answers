import os
import sys

# 请在此输入您的代码
st = {'1', '3', '5', '7', '9'}
for i in range(1, 1000000):
    x = 2019 * i
    s_x = str(x)
    n = len(s_x)
    m = 0
    for s in s_x:
        if s in st:
            m += 1
        else:
            break
    if (n == m):
        break
print(x)
        