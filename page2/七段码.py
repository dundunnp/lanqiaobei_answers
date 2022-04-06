import os
import sys
import copy

# 请在此输入您的代码
result = []
dic = {'a':{'b','f'}, 'b':{'a','g','c'}, 'c':{'b','g','d'}, 'd':{'e','c'} \
    , 'e':{'d','g','f'}, 'f':{'e','g','a'}, 'g':{'f','e','b','c'}}
def f(num, candidset, ans):
    if len(ans) == num:
        tmp = copy.copy(ans)
        if tmp not in result:
            result.append(tmp)
        return
    for i in candidset:
        if i not in ans:
            ans.add(i)
            f(num, candidset | dic[i], ans)
            ans.remove(i)
           
for i in range(2, 7):
    for k in dic.keys():
        f(i, {k}, set())

print(len(result) + 7 + 1) 