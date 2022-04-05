import os
import sys

# 请在此输入您的代码
count = sum([str(num).count('2') for num in range(1, 2021)])
print(count)