# 字符串

# python以unicode编码字符串，故python的字符串支持多语言
print('你好')

# ord()
# ord()以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
print(ord('a'))
print(ord('中'))

# chr()
# chr()用一个整数作参数，返回一个对应的字符。
print(chr(97))

# encode()
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
# str中包含中文字符，不能用ascii编码，因为超过了ascii的表示范围
print('中'.encode('utf-8'))


# decode()
# 要把bytes变为str，就需要用decode()方法
print(b'\xe4\xb8\xad'.decode('utf-8'))

# len()
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
A = 'hello'  # 5个字符
print(len(A))
B = '中'.encode('utf-8') # 3个字节
print(len(B))

# 不可变对象
s = 'hello'
print(s.replace('h', 'H')) # 返回一个新的对象
print(s) 
