import os
import sys

# 请在此输入您的代码
n = int(input())
# c = s + a
ce = []

for _ in range(n):
    data = input().split()
    ce.append([int(data[0]) + int(data[1]), int(data[2])])
    
ce.sort(key=lambda x:x[0] + x[1])
result = ce[0][0]
tmp = ce[0][0]
for i in range(n-1):
    tmp += ce[i][1] + ce[i+1][0]
    result += tmp
print(result)