import os
import sys

# 请在此输入您的代码
# 根据题目意思可得(x * 2021 + 8)整除1000000007
# 也即 x * 2021 + 8 = n * 1000000007
# 而x的取值范围为1-1000000007
# 可以根据上面等式得
# n的取值范围为(1, 2021)

for n in range(2, 2021):
    target = n * 1000000007 - 8
    if target % 2021 == 0:
        print(target // 2021)
        break
    