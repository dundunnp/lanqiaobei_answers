from configparser import LegacyInterpolation
import os
import sys

# 请在此输入您的代码
n = int(input())

left_ms = n % (24 * 60 * 60 * 1000)
hour = left_ms // (60 * 60 * 1000)
left_ms %= (60 * 60 * 1000)
min = left_ms // (60 * 1000)
left_ms %= (60 * 1000)
s = left_ms // 1000
def adjust(n):
    if n < 10:
        return '0' + str(n)
    return str(n)
print(adjust(hour) + ":" + adjust(min) + ":" + adjust(s))