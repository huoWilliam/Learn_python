# 生成器

# 创建一个generator
# 法1：把列表生成式的[]改成()
g = (x * x for x in range(1, 10))
print(g)

# 法2：函数中包含yield
# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'
f = fib(6)
print(f)



# 打印生成器内的元素
# 法1.next()
print(next(g))
print(next(g))

# 法2.迭代，生成器也是可迭代对象
from collections.abc import Iterable
print(isinstance(g, Iterable))
for n in g:
    print(n)

for n in fib(6):
    print(n)
