# 列表生成式

# 生成列表[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L1 = list(range(1, 11))
L2 = [x for x in range(1, 11)]
print(L1)
print(L2)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L3 = [x * x for x in range(1, 11)]
print(L3)

# 偶数的平方
L4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L4)   

# 两层循环
L5 = [m + n for m in 'ABC' for n in 'XYZ']
print(L5)

# 使用两个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L6 = [k + '=' + v for k, v in d.items()]
print(L6)

# 在一个列表生成式中，for前面的if ... else是表达式，
# 而for后面的if是过滤条件，不能带else。
L7 = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L7)

L = ['apple', 'pear', 18, 'banana']
L8 = [s.upper() for s in L if isinstance(s, str)]
print(L8)


