# 定义函数
import math

# 请定义一个函数quadratic(a, b, c)，接收3个参数，
# 返回一元二次方程 ax^2+bx+c=0的两个解。

# 1. 确定参数名及参数个数
def quadratic(a, b, c):
    d = b**2 - 4 * a * c
    if a == 0:
        print('this function is linear equation')
        return -1
    elif d < 0:
        print('no solution')
        return -1
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2 # 函数可以同时返回多个值，但其实就是一个tuple。


print('quadratic(0, 3, 1) =', quadratic(0, 3, 1))

