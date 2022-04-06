import os
import sys

# 请在此输入您的代码
result_list = []
# 2019 / 3 - 1 = 672
for i in range(1, 672):
    if ('2' in str(i) or '4' in str(i)):
        continue
    # (2019 - 1) / 2 - 1 = 1008
    for j in range(i + 1, 1009):
        if ('2' in str(j) or '4' in str(j)):
            continue
        k = 2019 - i - j
        if ('2' not in str(k)) and ('4' not in str(k)) and k != j and k != i:
            result = sorted([i, j, k])
            if result not in result_list:
                result_list.append(result)
print(len(result_list))