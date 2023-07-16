# else语句
# 1.if条件表达式不成立时执行else语句
"""
if 条件表达式:
    条件执行体1
else:
    条件执行体2
"""
# 2.没有碰到break时执行else语句
"""
while 条件表达式：
    条件执行体1(循环体)
else:
    条件执行体2
"""
"""
for 自定义的变量 in 可迭代对象：
    循环体
else：
    条件执行体
"""
""" """ """ """ """ """  """ """ """ """ """ """

for item in range(3):
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次均输入错误')
# break后不执行第二个else的内容
print('\t')
""" """ """ """ """ """ """  """ """ """ """ """ """ """
a = 0
while a < 3:
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次均输入错误')
