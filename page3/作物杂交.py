import os
import sys

# 请在此输入您的代码
# n作物种类总数（编号1至n），m初始拥有种子类型数，k杂交方案数，t目标种子编号
n, m, k, t = list(map(int, input().split()))
# i作物的种植时间
time = [0] + list(map(int, input().split())) 
# 表示已拥有的种子类型
M = set(map(int, input().split()))
# 表示得到i作物的杂交方案
K = [[] for _ in range(n+1)]
for _ in range(k):
    A, B, C = list(map(int, input().split()))
    K[C].append([A, B])
# 表示得到i作物的杂交时间
Time = [0 for _ in range(n+1)]
# 表示总杂交时间
h_t = 0
# 用递归
def f(t):
    global M
    if t in M: return time[t]
    for pair in K[t]:
        max(f(pair[0]), f(pair[1]))
    