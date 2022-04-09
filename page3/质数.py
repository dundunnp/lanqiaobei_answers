import os
import sys
import math

# 请在此输入您的代码
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
i = 0
n = 2
while True:
    if (is_prime(n)):
        i += 1
        if i == 2019:
            break
    n += 1
print(n)