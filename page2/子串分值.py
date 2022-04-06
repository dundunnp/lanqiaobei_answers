import os
import sys

# 请在此输入您的代码
"""
方式一：
"""
S = input()
sumvalue = 0
for i in range(0, len(S)):
    numleft = 0
    numright = 0
    temp = S[i]  # 也就是第i个字符的
    loc = i - 1
    while loc >= 0 and S[loc] != temp:
        loc -= 1
        numleft += 1
    loc = i + 1
    while loc < len(S) and S[loc] != temp:
        loc += 1  # 一直往上加
        numright += 1
    sumvalue += (numleft + 1) * (numright + 1)  # 也就是

print(sumvalue)
"""
方式二：
超时
"""
sumvalue = 0
S = input()
n = len(S)

for i in range(n):
    visit = [0 for _ in range(26)]
    value = 0
    for j in range(i, n):
        if not visit[ord(S[j]) - 97]:
            value += 1
            visit[ord(S[j]) - 97] += 1
        elif visit[ord(S[j]) - 97] == 1:
            value -= 1
            visit[ord(S[j]) - 97] += 1
        sumvalue += value
print(sumvalue)
