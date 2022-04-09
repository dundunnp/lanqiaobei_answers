import os
import sys

# 请在此输入您的代码
N = int(input())
Weight = list(map(int, input().split()))
sum_weight = []
n = 0
i = 1
while n < N:
    sum_weight.append(sum(Weight[n:n+i]))
    n += i
    i *= 2
max_weight = max(sum_weight)
print(sum_weight.index(max_weight) + 1)