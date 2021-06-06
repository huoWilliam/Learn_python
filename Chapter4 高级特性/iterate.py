# 迭代

# 对list进行迭代
L = list(range(0, 10))
for n in L:
    print(n, end = ' ')
print()

# 对dict进行迭代
D = {'name':'A', 'city':'DD', 'country':'UUU'}
# 默认情况下，dict迭代的是key
for key in D:
    print(key)
    
# 如果要迭代value需要借助values()函数
for value in D.values():
    print(value)

# 要同时迭代value和key，借助于items()函数
for key,value in D.items():
    print(key, '--', value)

# 如何判断一个对象是迭代对象
from collections.abc import Iterable
print(isinstance('abc', Iterable)) # str可是迭代对象

# 要对list实现下标循环，借助于enumurate()函数
# 把一个list变成索引-元素对
for i, value in enumerate(['A', 'B']):
    print(i, value)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    max_n = L[0]
    min_n = L[0]
    for n in L:
        if n <= min_n:
            min_n = n
        if n >= max_n:
            max_n = n
    return min_n, max_n

print(findMinAndMax([7, 1, 3, 9, 5]))