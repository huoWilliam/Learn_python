# 函数的参数

# 计算x^n的函数

# 位置参数实现
def power(x, n): # x, n都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
    return x ** n

print(power(2, 3))

# 默认参数
def power1(x, n = 2): # 默认计算x的平方
    return x ** n

print(power1(2))
print(power1(2, 3))
print(power1(n = 3, x = 2)) # 不按顺序提供默认参数时，要提供参数名

# 默认参数一定要指向不变对象
def add_end(L = []):
    L.append('End')
    return L
print(add_end([1, 2, 3])) # 正常表现
print(add_end())  # 正常表现
print(add_end()) # 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，
# 默认参数的内容就变了，不再是函数定义时的[]了。

# 依据原理，对此进行修改
def add_end(L = None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end())
print(add_end())
print(add_end())

# 可变参数
# 计算a2 + b2 + c2 + ……。
def calc(*nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum

print(calc(1,2,3))
# 使用list进行传参
print(calc(*[1,2,3,4]))
print(calc(*(1,2,3,4)))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('liyang', 23, gender = 'male', city = 'BJ')
# 使用dict进行传参
info = {'gerder': 'female', 'city': 'NY'}
person('hao', 24, **info)

# 命名关键字参数
def person1(name, age, *, city, job): # 只能传入city和job两个关键字参数
    print(name, age, city, job)

person1('Jack', 24, city='Beijing', job='Engineer')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了。
def person2(name, age, *args, city, job):
    print(name, age, city, job)

# 命名关键字参数必须传入参数名
person2('Tomas', 34, city = 'Lonton', job = 'gang')


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 设计接收一个或多个数并计算乘积的函数
def mul(x, *nums):
    # 判断x类型
    if not isinstance(x, (int, float)):
        return -1
    ans = x
    for n in nums:
        # 判断n的类型
        if not isinstance(n, (int, float)):
            return -1
        ans *= n
    return ans
    
print(mul(1, 2, 3))

