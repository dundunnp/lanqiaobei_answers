import os
import sys

# 请在此输入您的代码
# 返回字符串s冒泡排序的总交换次数
def sort_bubble_count(s):
    n = len(s)
    s = list(s)
    count = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                count += 1
    return count

# 考虑冒泡排序最坏情况，n个字符需要n*(n-1)/2次
# 因此100次交换至少要15个字符
# 因此最短的肯定为15个字符
# 如果要字典序最小肯定是在a-z前15个字符
s = ''
for i in range(ord('o'), ord('a') - 1, -1):
    s += chr(i)
# 此时s的交换次数是15 * 14 / 2 = 105次
# 因为按字典序排，所以尽量将字典序小的那个字母往前移
# 因此选择将j移到最前面
print('jonmlkihgfedcba')