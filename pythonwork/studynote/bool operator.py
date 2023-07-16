# 布尔运算符
# and(两个运算数都为Ture时，结果才为Ture)
# or(只要有一个运算数为Ture,结果就为Ture)
# not(如果运算数都为Ture,结果就为False;若都为False,结果就为Ture)
# in()
# not in()

a, b = 1, 2
print(a == 1 and b == 2)  # Ture
print(a == 1 and b < 2)   # False 一假为假
print('\r')
print(a == 1 or b == 2)
print(a < 1 or b == 2)
print(a < 1 or b < 2)     # 全假为假
print('\r')
f1 = True
f2 = False
print(not f1)       # 非真
print(not f2)       # 非假
print('\r')
s = 'hello world'
print('w' in s)     # 'w'在s中
print('i' in s)
print('w'not in s)  # 'w'不在s中
print('i'not in s)
