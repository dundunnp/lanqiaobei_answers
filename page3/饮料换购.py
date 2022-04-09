import os
import sys

# 请在此输入您的代码
n = int(input())
# n饮料数 m瓶盖数
def f(n, m):
    if n + m > 2:
        return n + f((m + n) // 3, (m + n) % 3)    
    else:
        return n
print(f(n, 0))