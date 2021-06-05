# 变量

# 变量赋值的过程
a = 'hello world' # 开拓一块内存，放入'hello world'.a指向它
b = a # b 指向 'hello world'这块内容
a = 'Kobe' # a 指向新的内容'Kobe'

# 结果：a->'Kobe',b->'hello world'
print(a, b, sep = '---')
