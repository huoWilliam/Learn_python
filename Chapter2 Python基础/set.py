# set

# 创建一个set
l = [1,2,3]
s = set(l)
print(s)
print(type(s))


# 添加元素，重复元素自动过滤
s.add(4)
s.add(1)
print(s)

# 删除元素
s.remove(4)
print(s)

# set中的元素必须是不可变对象
# 而元素[2,3]是一个列表，会发生变化
# s1 = set((1,[2,3]))
print(s1)