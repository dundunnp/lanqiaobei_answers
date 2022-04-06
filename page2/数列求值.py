import os
import sys

# 请在此输入您的代码
dp1 = 1
dp2 = 1
dp3 = 1
for i in range(3, 20190324):
    tmp = (dp1 + dp2 + dp3) % 10000
    dp1 = dp2
    dp2 = dp3
    dp3 = tmp
print(dp3)