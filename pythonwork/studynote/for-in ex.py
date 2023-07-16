""" 计算1到100之间的偶数和 """
# 方法一
sum = 0                                 # sum必须初始化
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print('1到100之间的偶数和为：', sum)
print('\t')

# 方法二
sum = 0
for item in range(0, 101, 2):
    sum += item
print('1到100之间的偶数和为：', sum)
print('\t')

""" 计算100到999之间的水仙花数 """
for item in range(100, 1000):
    ge = item % 10
    shi = item//10 % 10
    bai = item//100
    if (ge**3+shi**3+bai**3 == item):
        print(item)
