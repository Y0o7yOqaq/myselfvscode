# range()函数：用于生成一个整数序列
# 创建range对象的三种方式
# 1.range(stop) 创建一个(0，stop)之间的整数序列，步长(两个数之间相差的数)为1
# 2.range(start,stop) 创建一个(start，stop)之间的整数序列，步长为1
# 3.range(start,stop,step) 创建一个(start，stop)之间的整数序列，步长为step
# 返回值是一个迭代器对象
# 优点：无论range对象表示的整数序列有多长，所有的range对象占用的内存空间都是相同的，因为仅需要存储start,stop,step,只有当用到range对象的时侯，才会去计算序列中的相关元素
# in与not in判断整数序列中是否存在(不存在)指定的整数

r1 = range(10)
print(r1)        # r为迭代器对象，无法直接输出，需使用list()函数,来查看全部对象
print(list(r1))  # 到10结束，不包括10
print('\t')

r2 = range(1, 10)
print(r2)
print(list(r2))
print('\t')

r3 = range(1, 10, 3)
print(r3)
print(list(r3))
print('\t')

# 判断某一整数是否在序列中
print(10 in r1)
print(10 not in r1)
