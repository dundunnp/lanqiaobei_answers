import os
import sys

# 请在此输入您的代码
n = int(input())
n1 = 0
n2 = 0
for _ in range(n):
    score = int(input())
    if score >= 85:
        n2 += 1
    if score >= 60:
        n1 += 1
print("{}%".format(round(n1 / n * 100)))
print("{}%".format(round(n2 / n * 100)))
