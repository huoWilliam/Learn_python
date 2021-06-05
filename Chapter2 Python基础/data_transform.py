# 数据类型转换
# [],(),None,{},空set，0都会被转为False
print(bool([]))
print(bool(set()))
print(bool({}))
print(bool(()))
print(bool(None))
print(bool(0))

# int
print(int('12')) # 12
# print(int('12.8')) # 将str转为int时，str中不能含有除数字以外的其他符号
print(int(12.8)) # 12
print(int(False)) # 0

# float
print(float(12)) # 12.0
print(float('12.88')) # 12.88
print(float(False))   # 0.0

# str
print(str(12.8)) # '12.8'
print(str(11)) # '11'
print(str([1,2,3])) # '[1, 2, 3]'
print(str((1,2,3))) # '(1,2,3)'
print(str({1:1,2:2})) # '{1:1,2:2}'
