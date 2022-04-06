import os
import sys
import math

# 请在此输入您的代码
dp = [float('inf') for _ in range(2022)]
# 最小公倍数的计算：a * b / math.gcd(a, b)
dp[1] = 0
for i in range(1, 2022):
    for j in range(i + 1, i + 22):
        if j > 2021:
            break
        # 因为距离取最小公倍数，所以到当前结点的最短路径一定来自于前21个结点
        dp[j] = min(dp[j], dp[i] + i * j // math.gcd(i, j))
# 10266837
print(dp[2021])