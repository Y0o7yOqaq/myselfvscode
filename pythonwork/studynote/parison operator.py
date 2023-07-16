# 比较运算符
# 对变量或表达式的结果进行大小、真假等比较
# >,>=,<,<=,!=
# ==            对象 值(value) 的比较
# is, is not    对象 内存地址(id) 的比较

a, b = 10, 20
print('a=', a, type(a))
print('b=', b, type(b))
print('a>b吗?', a > b)
print('a>=b吗?', a >= b)
print('a<b吗?', a < b)
print('a<=b吗?', a <= b)
print('a和b相等', a == b)
print('a和b不等', a != b)
print('a、b的地址相同', a is b)
print('a、b的地址不同', a is not b)

print('\r')
c = d = 10
print('c=', c, 'd=', d)
print('c和d相等', c == d)
print('c和d的地址相同', c is d)
print('c和d的地址不同', c is not d)
print('\r')

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1))
print(id(list2))
