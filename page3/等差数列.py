import os
import sys

# 请在此输入您的代码
n = int(input())
A = list(map(int, input().split()))
A.sort()
# 找到相邻两数字的最小差值
diff = A[1] - A[0]
result = (A[n-1] - A[0]) // diff + 1
print(result)


