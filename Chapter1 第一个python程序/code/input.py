# input()

a = input('input: ')
print(a)

# input()的返回类型是string
print(type(a))


# 使用input()接收多个值
a, b, c = (input('请输入三角形的三边的长:').split())
a = int(a)
b = int(b)
c = int(c)

p=(a+b+c)/2 #计算三角形的半周长p
s=(p*(p-a)*(p-b)*(p-c))**0.5 #计算三角形的面积s
print("三角形面积为：",format(s,'.2f')) #输出三角形的面积