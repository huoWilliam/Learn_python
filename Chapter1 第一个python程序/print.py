# print()函数

# 输出1
print(1)

# 可以一次输出多个对象
print('hello', 'world')

# 默认多个对象间的间隔符为' ',修改为使用*-*作为间隔符
print('hello', 'world', '!', sep = '*_*')

# 修改默认结束符\n为^_^
print('hello', end = '^_^')
print('world')

# 格式化输出
s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('成绩提升了{0:.1f}%'.format(r * 100))
