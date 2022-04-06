import os
import sys

# 不会写
# 请在此输入您的代码
n = 0
sum = 0
tot = 0
ans = 0
cnt = [0] * 5
for _ in range(6):
    tmp = list(input().split())
    n += int(tmp[0])
    equip = tmp[1:]
    for i in equip:
        cnt[int(i)] += 1
m = int(input())
Lv = [0] * (m + 1)
p = [0] * (m + 1)
w = [[0] * 8 for _ in range(m + 1)]
for i in range(1, m + 1):
    decorative = input().split()
    Lv[i] = int(decorative[0])
    p[i] = int(decorative[1])
    for j in range(1, p[i] + 1):
        w[i][j] = int(decorative[j + 1])

dp = [[0] * (n + 1) for _ in range(n + 1)]

for L in range(4, 0, -1):
    sum += cnt[L]
    for i in range(1, m + 1):
        if Lv[i] == L:
            tot += 1
            for k in range(sum + 1):
                dp[tot][k] = dp[tot - 1][k]
            for j in range(1, p[i] + 1):
                dp[tot][k] = max(dp[tot][k], dp[tot - 1][k - j] + w[i][j])

ans = max([dp[tot][i] for i in range(sum + 1)])
print(ans)

