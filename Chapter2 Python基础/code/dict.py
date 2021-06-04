# dict，字典

# 建立一个字典，存储学生的成绩和姓名
classmates = {'Jane':60, 'Lisi':70, 'Ermazi':80}
print(classmates)

# 添加一个元素，使用key添加
classmates['Yello'] = 90
print(classmates)

# 多次对一个key放入value，后面的值会把前面的值冲掉
classmates['Jane'] = 44
print(classmates)

# 判断key是否存在，如果不存在会报错
# 使用in
if 'Jane' in classmates:
    print(classmates['Jane'])
# 使用get()
print(classmates.get('Lerb', -1)) # 如果key不存在，返回-1

# 删除key对应的元素
classmates.pop('Jane')
print(classmates)

# key必须是不可变对象
# D = {[1]:0, 'Jane':40} # list是可变对象，不能作为key
# print(D)