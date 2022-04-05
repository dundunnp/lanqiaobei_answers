import os
import sys

# 请在此输入您的代码
# dp保存第i行第i列的数字
dp = [0 for _ in range(21)]
dp[1] = 1
for i in range(2, 21):
    dp[i] = dp[i-1] + ((i - 2) * 2 + 1) // 2 + (i - 1) * 2 + ((i - 1) * 2 + 1) // 2 + 1 
print(dp[20])