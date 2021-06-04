# 计算1到50的累加和

# for...in循环
sum1 = 0
for x in range(1, 51):
    sum1 += x
print(sum1)

# while循环
n = 1
sum2 = 0
while n < 51:
    sum2 += n
    n += 1
print(sum2)

# break和continue的使用

# 当迭代10次后，退出循环, break
iter = 1
while True:
    if(iter > 10):
        break
    print('iter = {0}'.format(iter))
    iter += 1

# 输出1~20之间的奇数，continue
for n in range(1, 21):
    if(n % 2 == 0):
        continue
    print(n)
