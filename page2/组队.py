import os
import sys

# 请在此输入您的代码
s1 = [97, 92, 0, 0, 89, 82, 0, 0, 0, 95, 0, 0, 94, 0, 0, 0, 98, 93, 0, 0]
s2 = [90, 90, 85, 0, 0, 83, 86, 0, 97, 0, 99, 0, 0, 91, 83, 0, 0, 83, 87, 0, 99]
s3 = [0, 96, 0, 0, 97, 0, 0, 96, 89, 0, 96, 0, 0, 87, 98, 0, 99, 92, 0, 96]
s4 = [0, 0, 0, 80, 0, 0, 87, 0, 0, 0, 97, 93, 0, 0, 97, 93, 98, 96, 89, 95]
s5 = [0, 0, 93, 86, 0, 0, 90, 0, 0, 0, 0, 98, 0, 0, 98, 86, 81, 98, 92, 81]
n = len(s1)
max_score = 0
# 记录得分
score = 0
# 记录已上场球员编号
number = []
for i1 in range(n):
    if s1[i1] != 0:
        # 记录得分
        score += s1[i1]
        # 记录已上场球员编号
        number.append(i1)
        for i2 in range(n):
            if s2[i2] != 0 and i2 not in number:
                score += s2[i2]
                number.append(i2)
                for i3 in range(n):
                    if s3[i3] != 0 and i3 not in number:
                        score += s3[i3]
                        number.append(i3)  
                        for i4 in range(n):
                            if s4[i4] != 0 and i4 not in number:
                                score += s4[i4]
                                number.append(i4)  
                                for i5 in range(n):
                                    if s5[i5] != 0 and i5 not in number:
                                        max_score = max(max_score, score + s5[i5])
                                score -= s4[i4]
                                number.pop(-1)
                        score -= s3[i3]
                        number.pop(-1)
                score -= s2[i2]
                number.pop(-1)
        score -= s1[i1]
        number.pop(-1)
print(max_score)