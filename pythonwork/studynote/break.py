# break语句 用于结束循环结构，通常与分支结构if一起使用
# 在二重循环中，跳出本层循环
"""
for ... in ... :
    ......
    if ... :
        break
"""
"""
while ...:
    ......
    if ...:
        break
 """
# 一旦满足某个条件就使用break跳出循环

"""从键盘中录入密码，最多3次，如果正确就结束循环"""
for _ in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

print('\t')
""" """ """ """ """ """  """ """ """ """ """ """
a = 0
while a < 3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a += 1
