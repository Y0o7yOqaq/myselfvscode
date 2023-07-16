""" 计算1到100之间的偶数和 """
print('方法一：')
a = 0                             # a和sum必须初始化
sum = 0
while a <= 100:
    sum += a
    a += 2
print('1到100之间的偶数和为', sum)

print('\t')

print('方法二：')
a = 0
sum = 0
while a <= 100:
    if a % 2 == 0:  # 条件可改为 not bool(a % 2)
        sum += a
    a += 1
print('1到100之间的偶数和为', sum)
