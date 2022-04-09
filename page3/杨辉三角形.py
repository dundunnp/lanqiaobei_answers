import os
import sys

# 请在此输入您的代码
# 我尽力了只能做到10的8次方，到10的9次方就超时了
# 学会放弃
# 如果想看通过的代码请看下面文章https://blog.csdn.net/lishuaigell/article/details/122948697
n = int(input())

def C(n, m):
    result = 1
    while (n > 0):
        result *= (m / n)
        m -= 1
        n -= 1
    return result

# 先找到从哪列开始和结束可能存在n
# 开始很好找因为C(n//2, n)很大
# 而结束不好找因为C(2, n)很小
# 所以对于结束列用二分查找
if n == 1: print(1)
else:
    start_row = 0
    end_row = 0
    for row in range(1, 1000000001):
        if C(row//2, row) >= n:
            start_row = row
            break

    left, right = 0, 1000000000
    while (left < right):
        mid = left + (right - left) // 2
        if C(2, mid - 1) <= n <= C(2, mid):
            end_row = mid
            break
        elif C(2, mid) > n:
            right = mid - 1
        else:
            left = mid + 1
    end_row = mid
    print(end_row)
    # 再对start_row到end_row每一行用二分查找找到n
    col = 0
    while (col == 0 and start_row <= end_row):
        left = 0
        right = start_row // 2
        while (left <= right):
            mid = (left + right) // 2
            if C(mid, start_row) == n:
                col = mid
                break
            elif C(mid, start_row) > n:
                right = mid - 1
            else:
                left = mid + 1
        start_row += 1

    if start_row - 1 > end_row:
        print((n + 1) * n // 2 + 2)
    else:
        print((start_row - 1) * start_row // 2 + col + 1)

