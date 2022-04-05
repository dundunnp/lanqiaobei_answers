import os
import sys

# 请在此输入您的代码
n = int(input())
max_score = 0
min_score = 100
sum_score = 0
for _ in range(n):
    score = int(input())
    max_score = max(score, max_score)
    min_score = min(score, min_score)
    sum_score += score
print(max_score)
print(min_score)
print("%.2f" % (sum_score / n))
