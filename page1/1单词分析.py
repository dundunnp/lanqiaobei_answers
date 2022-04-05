import os
import sys

# 请在此输入您的代码
string = input()
dic = {}
for ch in string:
    dic[ch] = dic.get(ch, 0) + 1

max_ch = sorted(dic, key=lambda x: (dic[x], -ord(x)))[-1]
print(max_ch)
print(dic.get(max_ch))
