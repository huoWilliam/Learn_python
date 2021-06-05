# tuple

# 在定义tuple的时候，tuple的元素必须被确定下来
t = (1, 2)
print(t)

# tuple一旦初始化，就不能修改
# t[1] = 3 # 'tuple' object does not support item assignment

# 定义一个只有1个元素的tuple
t1 = (1,)
t2 = (1) # 这么写的话，t1是一个数字
print('t1\'s type: {0}, t2\'s type: {1}'.format(type(t1), type(t2)))

# 一个‘可变的’tuple
t3 = ('a', 'b', ['A', 'B'])
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)
'''
表面上看，tuple的元素确实变了，
但其实变的不是tuple的元素，而是list的元素。tuple一开始指向
的list并没有改成别的list，所以，tuple所谓的“不变”是说，
tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
指向一个list，就不能改成指向其他对象，但指向的这个list本身
是可变的！
'''

