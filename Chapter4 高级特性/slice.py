# 切片

L = list(range(0, 10)) # [0, 10)
print(L)

# 取前3个元素
print(L[:3])
print(L[0:3])  # [0, 3)的范围

# 取后3个元素
print(L[-3:])

# 取第2~5个数
print(L[1:6])

# 复制L
L_copy = L[:]
print(L_copy)

# 取奇数
odd = L[1::2]   # 最后一个数字表示步长
print(odd)

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
# 注意不要调用str的strip()方法
def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    return s

print(trim('  hello  '))
