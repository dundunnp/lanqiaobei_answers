import os
import sys

# 请在此输入您的代码
# 向左下走的次数与向右下走的次数相差不能超过 1
# 表示最后只能走到第N行的中间的那个数（如果N为奇数则为两个数，如果为偶数就为一个数）
n = int(input())
dp = []
for _ in range(n):
    dp.append([int(i) for i in input().split()])
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
if n % 2 == 0:
    result = max(dp[n - 1][n // 2], dp[n - 1][n // 2 - 1])
else:
    result = dp[n - 1][n // 2]
print(result)
