import os
import sys

# 请在此输入您的代码
n = int(input())
sumvalue = 0
for i in range(1, n + 1):
    if '2' in str(i) or '0' in str(i) or '1' in str(i) or '9' in str(i):
        sumvalue += i
print(sumvalue) 