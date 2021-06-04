# 数据类型

# 1. 整数
# 十六进制表示整数
a = 0xffff # 65535
print(a)
# 八进制表示整数
b = 0o17  # 15
print(b)
# 二进制表示整数
c = 0b1111  # 15
print(c)

# 2. 浮点数
d = 1.23e9 # 科学计数法
print(d)

print(5 // 3) #整数运算永远是精确的

# 3. 字符串
print('I am ok')
print('i am \'ok\'') # 使用转义字符
print(r'i am \'ok\'') # 忽视字符串中的转义字符

# 用'''...'''的格式表示多行内容
print('''hello
world
nice''')

# 4. 布尔值
print(1 < 2) # True
print(1 > 2) # False
print(False and True) # False

# 布尔值经常用在条件判断中
if True:
    print('Tommy Shelby')