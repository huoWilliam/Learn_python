# list

# 建立一个list，存储班级同学
classmates = ['Jane', 'Tommy', 'Tomas', 'Mike']

# 获取list内的元素格式
size = len(classmates)

# 访问list中的元素
print(classmates[1]) # 索引位置为1的元素
print(classmates[-1])   # 最后一个元素

# 在末尾追加一个元素
classmates.append('Curry')

# 删除索引位置为1的元素
classmates.pop(1)

# 在索引位置为1处，插入一个元素
classmates.insert(1, 'Liiard')

print(classmates)
print(classmates)

# 修改元素
classmates[1] = 'James'
print(classmates)

# list中存储的元素类型可以不同
L = ['mark', 111, 12.3, [13, 14, 15]]
print(L)
