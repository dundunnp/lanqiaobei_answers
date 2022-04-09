import os
import sys
from itertools import permutations

# 请在此输入您的代码
n = int(input())
# 固定行号1-n选可能组合的列数
candid_col = list(permutations(range(n)))
result = len(candid_col)
for i in candid_col:
    flag = True
    for row1 in range(n):
        for row2 in range(row1 + 1, n):
            if abs(i[row1] - i[row2]) == abs(row1 - row2) and abs(row1 - row2) < 3:
                flag = False
                break
        if not flag:
            break
    if not flag:
        result -= 1
print(result)