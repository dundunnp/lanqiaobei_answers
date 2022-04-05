import os
import sys
import math

# 请在此输入您的代码
def is_prime(n):
    if n <= 1: return False
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0: return False
    return True

min_diff = 1000000
prime_list = [i for i in range(100000) if is_prime(i)]
for num in prime_list:
    for diff in range(1, 1000):
        i = 1
        while i < 10 and is_prime(num + diff * i):
            i += 1
        if (i == 10 and not is_prime(num + diff * i)):
            min_diff = min(min_diff, diff)
print(min_diff)