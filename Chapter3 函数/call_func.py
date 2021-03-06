# 调用函数

# abs() 函数返回数字的绝对值。
# 参数：x -- 数值表达式。
print(abs(-10)) # 10
print(abs(-11.31)) # 11.31

# max() 方法返回给定参数的最大值，参数可以为序列。
a = max(1,2,3,4,5)
print(a)
 
d = {1:2, 2:2, 3:1, 4:'aa'}  #比较字典里面的最大值，会输出最大的键值
print(max(d))

# hex()函数把一个整数转换成十六进制表示的字符串
print(hex(255))
print(hex(1000))

# oct()函数把一个整数转换成八进制表示的字符串
print(oct(255))
print(oct(1000))

# 为函数起一个别名
my_hex = hex
print(my_hex(255))