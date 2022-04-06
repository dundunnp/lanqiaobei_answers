import os
import sys

# 请在此输入您的代码
n, m = [int(i) for i in input().split()]
w = [[int(i) for i in input().split()] for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = w[0][0]
# 初始化
for i in range(1, n):
    dp[i][0] = max([dp[i-x][0] for x in range(1, 4) if i - x > -1]) + w[i][0]
for j in range(1, m):
    dp[0][j] = max([dp[0][j-y] for y in range(1, 4) if j - y > -1]) + w[0][j]

for i in range(1, n):
    for j in range(1, m):
        max_w = -1e6
        for x in range(4):
            for y in range(4):
                if -1 < i - x < n and -1 < j - y < m and \
                    (x != i or y != j) and x + y <= 3:
                    max_w = max(max_w, dp[i-x][j-y])
        dp[i][j] = max_w + w[i][j]
print(dp[n-1][m-1])