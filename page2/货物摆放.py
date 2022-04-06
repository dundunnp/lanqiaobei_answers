import os
import sys
import math

# 请在此输入您的代码
n = 2021041820210418
# 找到n的所有因子
factors = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0: 
        factors.append(i)
        factors.append(n / i)
# 这里排序是为了后面的遍历优化
factors.sort()
result = 0
for l in factors: 
    for w in factors:
        if l * w > n:
            break
        for h in factors:
            if l * w * h == n:
                result += 1
            if l * w * h > n:
                break
print(result)